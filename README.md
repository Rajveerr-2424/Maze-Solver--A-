# 🧩 Visual Maze Solver using A* Algorithm

A Python-based Visual Maze Solver that automatically detects the maze entrance and exit from an image, finds the shortest path using the **A* (A-Star) Search Algorithm**, and highlights the solution with a **translucent green overlay**.

---

## 📌 Features

- 📷 Solves mazes directly from image files
- 🤖 Uses the A* Search Algorithm for optimal pathfinding
- 🔍 Automatically detects maze entrance and exit
- 🛣 Finds the shortest valid route
- 🟢 Highlights the path using a translucent green overlay
- 🧹 Path simplification for cleaner visualization
- 💾 Saves the solved maze as an image

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- NumPy
- Heapq (Priority Queue)
- Collections (Deque)

---

## 📂 Project Structure

```text
Maze-Solver/
│
├── maze.png
├── maze_solver.py
├── solved_maze.png
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/maze-solver.git

cd maze-solver
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python numpy
```

---

## 🚀 Usage

### Step 1

Place your maze image in the project folder.

```text
maze.png
```

### Step 2

Run the solver.

```bash
python maze_solver.py
```

### Step 3

View the generated result.

```text
solved_maze.png
```

---

## 🧠 How It Works

### 1. Image Processing

The maze image is:

- Converted to grayscale
- Thresholded into a binary image
- Converted into a traversable grid

```text
White = Path
Black = Wall
```

### 2. Entrance Detection

The program scans the top border and detects the first valid opening.

```text
Start → Top Border Opening
```

### 3. Exit Detection

A Breadth-First Search (BFS) is performed to locate a reachable exit on the bottom border.

```text
Goal → Reachable Bottom Opening
```

### 4. A* Pathfinding

The shortest path is calculated using:

```math
f(n) = g(n) + h(n)
```

Where:

| Function | Meaning |
|-----------|----------|
| g(n) | Distance from start |
| h(n) | Manhattan heuristic |
| f(n) | Total estimated cost |

### 5. Path Visualization

The final path is:

- Simplified
- Smoothed
- Highlighted using a translucent green overlay

```text
Original Maze
      ↓
Path Detection
      ↓
A* Search
      ↓
Green Highlighted Solution
```

---

## 📸 Example

### Input Maze

```text
maze.png
```

### Output Maze

```text
solved_maze.png
```

The shortest route is highlighted with a semi-transparent green overlay while preserving visibility of the maze structure.

---

## 📈 Algorithm Complexity

### Time Complexity

```text
O(E log V)
```

### Space Complexity

```text
O(V)
```

Where:

- V = Number of cells
- E = Number of connections between cells

---

## 🎯 Applications

- Robotics Navigation
- Game AI
- Autonomous Vehicles
- Route Planning Systems
- Warehouse Automation
- Pathfinding Research

---

## 🔮 Future Improvements

- Interactive GUI
- Animated path visualization
- Multiple maze formats
- Real-time webcam maze solving
- Support for colored mazes
- Center-line skeleton path extraction
- Performance optimization for large mazes

---

## 📚 Learning Outcomes

Through this project, you will understand:

- Image Processing using OpenCV
- Graph Representation of Images
- Breadth-First Search (BFS)
- A* Search Algorithm
- Heuristic Functions
- Path Visualization Techniques

---

## 👨‍💻 Author

**Rajveerr Awachat**

B.Tech Computer Science Engineering  
Ramdeobaba University, Nagpur

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it for educational purposes.
