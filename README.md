# AlPro Final Task

## Binary Search Tree and Dijkstra Algorithm

This repository contains the **final group project (UAS)** for the **Algoritma dan Pemrograman (AlPro)** course. The project focuses on the implementation, explanation, and comparison of two fundamental data structures and algorithms:

* **Binary Search Tree (BST)**
* **Dijkstra’s Shortest Path Algorithm**

The goal of this project is not only to make the algorithms work, but to demonstrate a clear understanding of how they operate, when they should be used, and their computational characteristics.

---

## Project Objectives

* Implement a **Binary Search Tree** with standard operations.
* Implement **Dijkstra’s Algorithm** to find the shortest path in a weighted graph.
* Analyze **time and space complexity** of each algorithm.
* Apply algorithmic thinking and structured programming principles.
* Practice teamwork and version control using **Git/GitHub**.

---

## Binary Search Tree (BST)

A **Binary Search Tree** is a hierarchical data structure where:

* Each node has at most two children.
* The left subtree contains values **less than** the parent node.
* The right subtree contains values **greater than** the parent node.

### Implemented Operations

* Insertion
* Searching
* Deletion (if included)
* Tree traversal:

  * Inorder
  * Preorder
  * Postorder

### Advantages

* Efficient searching and insertion on average.
* Maintains sorted data structure.

### Limitations

* Performance degrades to **O(n)** in the worst case (unbalanced tree).

---

## Dijkstra Algorithm

**Dijkstra’s Algorithm** is used to find the **shortest path** from a starting node to all other nodes in a weighted graph with **non-negative edge weights**.

### Key Characteristics

* Greedy algorithm
* Uses priority queue (or array) to select the nearest unvisited node
* Guarantees optimal shortest path

### Applications

* Network routing
* GPS and navigation systems
* Transportation and logistics

### Limitations

* Does not work with negative edge weights

---

## Technologies Used

* Programming Language: *(specify, e.g., C / C++ / Java / Python)*
* Development Tools: Git, GitHub
* Platform: Console-based application

---

## Project Structure

```
AlPro-FinalTask/
│── bst/
│   ├── bst_source_code
│   └── bst_test_cases
│
│── dijkstra/
│   ├── dijkstra_source_code
│   └── graph_examples
│
│── README.md
```

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/username/AlPro-FinalTask.git
   ```
2. Navigate to the project directory.
3. Compile or run the program according to the selected programming language.

---

## Contributors

* Group Member 1
* Group Member 2
* Group Member 3

---

## Conclusion

This project demonstrates the practical implementation of core algorithmic concepts taught in the AlPro course. By working with **Binary Search Trees** and **Dijkstra’s Algorithm**, we gain deeper insight into data organization, graph traversal, and efficiency considerations in software development.

---

**Course:** Algoritma dan Pemrograman (AlPro)
**Type:** Final Group Project (UAS)
