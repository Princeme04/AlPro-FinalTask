# 🧠⚙️ Programming Algorithm



<img src="https://github.com/user-attachments/assets/487ddf74-3c79-4f83-9ce0-2584cd39370e" width="300"/>


![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![GitHub repo size](https://img.shields.io/github/repo-size/Princeme04/AlPro-FinalTask)
![GitHub last commit](https://img.shields.io/github/last-commit/Princeme04/AlPro-FinalTask)
![GitHub top language](https://img.shields.io/github/languages/top/Princeme04/AlPro-FinalTask)
![License](https://img.shields.io/github/license/Princeme04/AlPro-FinalTask)
## 🌐 Binary Search Tree and Dijkstra Algorithm

This repository contains the **final group project (UAS)** for the  
**Algoritma Pemrograman** course.

![Image](https://github.com/user-attachments/assets/5e350be0-415d-44f2-a718-86fdcf32ffdc)

The project focuses on the implementation, explanation, and comparison of two fundamental data structures and algorithms:

- 🌳 **Binary Search Tree (BST)**
- 🛣️ **Dijkstra’s Shortest Path Algorithm**

The goal of this project is not only to make the algorithms work, but to demonstrate a clear understanding of how they operate, when they should be used, and their computational characteristics.

---

## 🎯 Project Objectives

- 🧩 Implement a **Binary Search Tree** with standard operations  
- 🧭 Implement **Dijkstra’s Algorithm** to find the shortest path in a weighted graph  
- ⏱️ Analyze **time and space complexity**  
- 🧠 Apply algorithmic thinking and structured programming principles  
- 🤝 Practice teamwork and version control using **Git/GitHub**

---

## 🌳 Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a hierarchical data structure in which each node has at most two children and follows a strict ordering rule:

- Values in the **left subtree** are smaller than the parent node  
- Values in the **right subtree** are greater than the parent node  

This property allows efficient searching, insertion, and deletion operations.

### Implementation

        --- BST Menu ---
        1. Insert value
        2. Insert multiple values
        3. Display tree
        4. Clear tree
        5. Back to main menu
        Choose option (1-5): 2
        Enter values separated by space: 23 24 51 16 7 6 8
        Values inserted successfully!
        
        Current tree:    
             23     
            /  \    
          16    24   
         /        \  
        7         51  
       / \          
      6   8  


### ⚙️ Key Characteristics

- Tree-based data structure  
- Maintains data in **sorted order**  
- Average time complexity: **O(log n)**  
- Worst-case time complexity: **O(n)** (when the tree becomes unbalanced)

### 🔍 Supported Operations

- Insertion of nodes  
- Searching for a value  
- Deletion of nodes  
- Tree traversal:
  - Inorder  
  - Preorder  
  - Postorder  

### 🌍 Applications

- Searching and indexing data  
- Implementing ordered sets and maps  
- Database indexing  
- Expression parsing  

### ⚠️ Limitations

- Performance degrades if the tree becomes **unbalanced**  
- Requires balancing techniques (e.g., **AVL Tree**, **Red-Black Tree**) for guaranteed efficiency  

---

## 🛣️ Dijkstra Algorithm

**Dijkstra’s Algorithm** is used to find the **shortest path** from a starting node to all other nodes in a weighted graph with **non-negative edge weights**.

### Implementation
Table show how dijkstra flow from node A to D
    
    Available nodes: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    Enter start node: a
    Enter end node: d
    
    Step 0:
      Current node : A
      Distances    : {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf}
      Visited flags: {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
      Unvisited    : {'H', 'E', 'B', 'A', 'C', 'D', 'F', 'G'}
    
    Step 1:
      Current node : B
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': inf, 'E': inf, 'F': inf, 'G': 1, 'H': inf}
      Visited flags: {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
      Unvisited    : {'H', 'E', 'B', 'C', 'D', 'F', 'G'}
    
    Step 2:
      Current node : G
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 5, 'E': 6, 'F': inf, 'G': 1, 'H': inf}
      Visited flags: {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
      Unvisited    : {'H', 'E', 'C', 'D', 'F', 'G'}
    
    Step 3:
      Current node : H
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 5, 'E': 6, 'F': inf, 'G': 1, 'H': 2}
      Visited flags: {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0}
      Unvisited    : {'H', 'E', 'C', 'D', 'F'}
    
    Step 4:
      Current node : C
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 5, 'E': 6, 'F': 3, 'G': 1, 'H': 2}
      Visited flags: {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 1}
      Unvisited    : {'E', 'C', 'D', 'F'}
    
    Step 5:
      Current node : F
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 3, 'G': 1, 'H': 2}
      Visited flags: {'A': 1, 'B': 1, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 1}
      Unvisited    : {'E', 'D', 'F'}
    
    Step 6:
      Current node : D
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 3, 'G': 1, 'H': 2}
      Visited flags: {'A': 1, 'B': 1, 'C': 1, 'D': 0, 'E': 0, 'F': 1, 'G': 1, 'H': 1}
      Unvisited    : {'E', 'D'}
    
    Step 7:
      Current node : E
      Distances    : {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 3, 'G': 1, 'H': 2}
      Visited flags: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 1, 'G': 1, 'H': 1}
      Unvisited    : {'E'}
      
Table:

    Node | Vis | Dist | Prev
    -------------------------
      A   |  1  |     0 |  -
      B   |  1  |     1 |  A
      C   |  1  |     2 |  A
      D   |  1  |     4 |  C
      E   |  1  |     5 |  C
      F   |  1  |     3 |  H
      G   |  1  |     1 |  A
      H   |  1  |     2 |  G
Summary:

    Shortest path A -> D: ['A', 'C', 'D']
    Total distance: 4

### ⚙️ Key Characteristics

- Greedy algorithm  
- Uses a priority queue (or array) to select the nearest unvisited node  
- Guarantees optimal shortest path  

### 🌍 Applications

- Network routing  
- GPS and navigation systems  
- Transportation and logistics  

### ⚠️ Limitations

- Does not work with negative edge weights  

---

## 🧰 Technologies Used

- 💻 Programming Language: *(Python)*  
- 🛠️ Development Tools: Git, GitHub  
- 🖥️ Platform: Console-based application  

---

## ▶️ How to Run

1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/username/AlPro-FinalTask.git
