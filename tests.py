import unittest
from creation import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_small(self):
        num_cols = 5
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 50
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

class TestMaze(unittest.TestCase):
    def test_break_entrance_and_exit(self):
        # Create a test maze with the correct parameters
        test_maze = Maze(0, 0, 3, 3, 10, 10)
        
        # Call the method we're testing
        test_maze._break_entrance_and_exit()
        
        # Check that the top wall of the top-left cell is removed
        self.assertFalse(test_maze._cells[0][0].has_top_wall, 
                         "Entrance (top wall of top-left cell) should be removed")
        
        # Check that the bottom wall of the bottom-right cell is removed
        self.assertFalse(test_maze._cells[2][2].has_bottom_wall, 
                         "Exit (bottom wall of bottom-right cell) should be removed")
    
    def test_entrance_exit_different_sizes(self):
        # Test with a larger maze
        large_maze = Maze(0, 0, 5, 5, 10, 10)
        large_maze._break_entrance_and_exit()
    
        # Check entrance (top-left)
        self.assertFalse(large_maze._cells[0][0].has_top_wall,
                        "Entrance should be removed in large maze")
    
        # Check exit (bottom-right)
        self.assertFalse(large_maze._cells[4][4].has_bottom_wall,
                        "Exit should be removed in large maze")
    
        # Check that other walls remain intact
        self.assertTrue(large_maze._cells[0][0].has_right_wall,
                       "Right wall of entrance cell should remain intact")
        self.assertTrue(large_maze._cells[4][4].has_left_wall,
                       "Left wall of exit cell should remain intact")

    def test_entrance_exit_with_offset(self):
        # Test maze with an offset from origin
        offset_maze = Maze(10, 20, 3, 3, 10, 10)
        offset_maze._break_entrance_and_exit()
    
        # Check entrance (top-left)
        self.assertFalse(offset_maze._cells[0][0].has_top_wall,
                        "Entrance should be removed in offset maze")
    
        # Check exit (bottom-right)
        self.assertFalse(offset_maze._cells[2][2].has_bottom_wall,
                        "Exit should be removed in offset maze")
    
        # Verify the offset doesn't affect cell wall removal
        self.assertEqual(offset_maze.x1, 10, "X-offset should be preserved")
        self.assertEqual(offset_maze.y1, 20, "Y-offset should be preserved")

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 3, 3, 10, 10)

        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        maze._cells[2][2].visited = True
        
        maze._reset_cells_visited()

        for i in range(maze.num_cols):
            for j in range(maze.num_rows):
                self.assertFalse(maze._cells[i][j].visited)

    def test_reset_cells_visited_after_breaking_walls(self):
        maze = Maze(0, 0, 4, 4, 10, 10, seed=42)

        for i in range(maze.num_cols):
            for j in range(maze.num_rows):
                maze._cells[i][j].visited = True

        maze._reset_cells_visited()

        for i in range(maze.num_cols):
            for j in range(maze.num_rows):
                self.assertFalse(maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
