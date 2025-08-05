'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
'''

from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    
    # Directions for 8 possible movements
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Check if the start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Initialize BFS queue and visited set
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set((0, 0))
    
    while queue:
        r, c, path_length = queue.popleft()
        
        # If we have reached the end
        if r == n-1 and c == n-1:
            return path_length
        
        # Explore all 8 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                queue.append((nr, nc, path_length + 1))
                visited.add((nr, nc))
    
    # If we exhaust the queue without finding the end
    return -1
