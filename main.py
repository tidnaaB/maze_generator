# Imports
from graphics import Window
from maze import Maze


# Main function
def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    # Create the window object
    window = Window(screen_x, screen_y)

    # Create a Maze object
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    # Call the wait_for_close() method on the window object
    window.wait_for_close()


# If the script is being run directly, call the main() function
if __name__ == "__main__":
    main()
