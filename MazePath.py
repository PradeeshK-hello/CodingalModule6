def is_safe(maze, x, y, visited):
    return (0 <= x < len(maze) and 
            0 <= y < len(maze[0]) and
            maze[x][y] == 1 and 
            not visited[x][y])
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []
    def backtrack(x, y):
        if not is_safe(maze, x, y, visited):
            return False
        path.append((x, y))
        visited[x][y] = True
        if x == rows - 1 and y == cols - 1:
            return True
        if (backtrack(x + 1, y) or
            backtrack(x, y + 1) or
            backtrack(x - 1, y) or
            backtrack(x, y - 1)):
            return True
        path.pop()
        visited[x][y] = False
        return False
    if backtrack(0, 0):
        return path
    else:
        return None
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
result = solve_maze(maze)
print("Path:", result)