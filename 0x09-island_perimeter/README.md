# 0x09. Island Perimeter
`Algorithm`
`Python`

Concepts Needed:
- **2D Arrays (Matrices)**:

Accessing and iterating over elements in a 2D array.
Understanding how to navigate through adjacent cells (horizontally and vertically).

- **Conditional Logic**:

Applying conditions to determine whether a cell contributes to the perimeter of the island.
Counting Techniques:

Developing a method to count the edges that contribute to the island’s perimeter.

- **Problem-Solving Strategies**:

Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

- **Python Programming**:

Nested loops for iterating over grid cells.
Conditional statements to check the status of adjacent cells.

## Tasks

1. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:

`grid` is a list of list of integers:
- `0` represents water
- `1` represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally).
- grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$
```

Repo:

- GitHub repository: `alx-interview`
- Directory: `0x09-island_perimeter`
- File: `0-island_perimeter.py`
