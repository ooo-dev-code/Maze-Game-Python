from collections import deque
import random

def find_position(maze, value):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == value:
                return (i, j)
    return None

def is_solvable(maze):
    start = find_position(maze, "A")
    end = find_position(maze, "B")
    if not start or not end:
        return False

    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and maze[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1 and random.random() < 0.3:
                maze[i][j] = 0
    maze[0][random.randint(0, (cols-2))] = "A"
    maze[rows-1][random.randint(0, (cols-2))] = "B"
    return maze

def generate_solveable(size):
    solvable = False
    while not solvable:
        maze = generate_maze(size, size)
        solvable = is_solvable(maze)
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print("Solvable:", is_solvable(maze))
    return maze
