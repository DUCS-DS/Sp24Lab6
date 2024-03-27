from maze import Maze

if __name__ == "__main__":
    maze = Maze()

    print("The original maze:")
    print(maze)

    dist = maze.shortestPath()

    print("The solved maze:")
    print(maze)

    print(f"A shortest path has length {dist}.")
