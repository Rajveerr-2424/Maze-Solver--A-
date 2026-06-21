import cv2
import numpy as np
import heapq
from collections import deque


# ==================================================
# HEURISTIC
# ==================================================

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ==================================================
# A* SEARCH
# ==================================================

def astar(grid, start, goal):

    rows, cols = grid.shape

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        for dx, dy in directions:

            nx = current[0] + dx
            ny = current[1] + dy

            if (
                0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == 0
            ):

                neighbor = (nx, ny)

                tentative_g = g_score[current] + 1

                if (
                    neighbor not in g_score
                    or tentative_g < g_score[neighbor]
                ):

                    g_score[neighbor] = tentative_g

                    f_score = (
                        tentative_g
                        + heuristic(neighbor, goal)
                    )

                    came_from[neighbor] = current

                    heapq.heappush(
                        open_set,
                        (f_score, neighbor)
                    )

    return None


# ==================================================
# FIND START
# ==================================================

def find_start(grid):

    rows, cols = grid.shape

    for c in range(cols):
        if grid[0][c] == 0:
            return (0, c)

    return None


# ==================================================
# FIND REACHABLE EXIT
# ==================================================

def find_reachable_exit(grid, start):

    rows, cols = grid.shape

    q = deque([start])
    visited = {start}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while q:

        x, y = q.popleft()

        if x == rows - 1:
            return (x, y)

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append((nx, ny))

    return None


# ==================================================
# PATH SIMPLIFICATION
# ==================================================

def simplify_path(path):

    if len(path) < 3:
        return path

    simplified = [path[0]]

    for i in range(1, len(path) - 1):

        prev = path[i - 1]
        curr = path[i]
        nxt = path[i + 1]

        d1 = (
            curr[0] - prev[0],
            curr[1] - prev[1]
        )

        d2 = (
            nxt[0] - curr[0],
            nxt[1] - curr[1]
        )

        if d1 != d2:
            simplified.append(curr)

    simplified.append(path[-1])

    return simplified


# ==================================================
# LOAD IMAGE
# ==================================================

img = cv2.imread("maze.png")

if img is None:
    print("maze.png not found")
    quit()

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

_, binary = cv2.threshold(
    gray,
    180,
    255,
    cv2.THRESH_BINARY
)

# resize for solving

binary = cv2.resize(
    binary,
    (300, 300),
    interpolation=cv2.INTER_NEAREST
)

# ==================================================
# CREATE GRID
# ==================================================

grid = np.where(binary > 200, 0, 1)

rows, cols = grid.shape

# ==================================================
# START & GOAL
# ==================================================

start = find_start(grid)

if start is None:
    print("No entrance found")
    quit()

goal = find_reachable_exit(
    grid,
    start
)

if goal is None:
    print("No reachable exit found")
    quit()

print("Start:", start)
print("Goal :", goal)

# ==================================================
# SOLVE
# ==================================================

path = astar(
    grid,
    start,
    goal
)

if path is None:
    print("No path found")
    quit()

print("Path Length:", len(path))

# ==================================================
# SIMPLIFY PATH
# ==================================================

smooth_path = simplify_path(path)

# ==================================================
# DRAW RESULT
# ==================================================

output = cv2.cvtColor(
    binary,
    cv2.COLOR_GRAY2BGR
)

# Draw thick smooth segments

# Create overlay
overlay = output.copy()

# Draw thick green route
for i in range(len(smooth_path) - 1):

    p1 = smooth_path[i]
    p2 = smooth_path[i + 1]

    cv2.line(
        overlay,
        (p1[1], p1[0]),
        (p2[1], p2[0]),
        (0, 255, 0),   # Green
        10             # Thickness
    )

# Apply transparency
alpha = 0.35

output = cv2.addWeighted(
    overlay,
    alpha,
    output,
    1 - alpha,
    0
)

# Start marker

cv2.circle(
    output,
    (start[1], start[0]),
    5,
    (0, 255, 0),
    -1
)

# Goal marker

cv2.circle(
    output,
    (goal[1], goal[0]),
    5,
    (255, 0, 0),
    -1
)

# upscale

output = cv2.resize(
    output,
    (1200, 1200),
    interpolation=cv2.INTER_NEAREST
)

cv2.imwrite(
    "solved_maze.png",
    output
)

print("Solved maze saved as solved_maze.png")