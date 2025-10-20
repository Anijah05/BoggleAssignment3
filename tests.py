import unittest
import sys
from boggle_solver import Boggle

# Add path so unittest can find boggle_solver.py
sys.path.append("/home/codio/workspace/")


class TestSuiteAlgScalabilityCases(unittest.TestCase):
    """Tests for scalability with larger grids and dictionaries."""

    def test_normal_case_3x3(self):
        """Test a normal 3x3 grid with mixed words."""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "Ie"]
        ]
        dictionary = ["abc", "abdhie", "abie", "ef", "cfie", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhie", "cfie", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuiteSimpleEdgeCases(unittest.TestCase):
    """Simple edge test cases."""

    def test_square_grid_case_1x1(self):
        """Test a 1x1 grid (should find no words)."""
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_empty_grid_case_0x0(self):
        """Test an empty grid (no results)."""
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuiteCompleteCoverage(unittest.TestCase):
    """Comprehensive coverage tests."""

    def test_case_1(self):
        """Placeholder for complex cases."""
        self.assertEqual(True, True)


class TestSuiteQuAndSt(unittest.TestCase):
    """Tests for 'Qu' and 'St' combinations."""

    def test_case_1(self):
        """Placeholder for QU/ST-specific cases."""
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
