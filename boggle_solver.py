"""
Name: Anijah Dancer
SID: 03096812
Boggle Solver Project
"""


class Boggle:
    def __init__(self, grid=None, dictionary=None):
        """Constructor for Boggle"""
        self.grid = []
        self.dictionary = set()
        self.prefixes = set()
        self.found_words = set()

        if grid:
            self.setGrid(grid)
        if dictionary:
            self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Setter for the Boggle grid (normalize to uppercase strings)"""
        self.grid = [[str(cell).upper() for cell in row] for row in grid]

    def setDictionary(self, dictionary):
        """Setter for the dictionary (normalize to uppercase words)"""
        self.dictionary = set(word.upper() for word in dictionary)
        self._build_prefixes()

    def _build_prefixes(self):
        """Build a set of all possible prefixes from dictionary"""
        self.prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    def getSolution(self):
        """Return all found words"""
        if not self.grid or not self.dictionary:
            return []

        self.found_words = set()
        rows, cols = len(self.grid), len(self.grid[0])

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, "", set())

        return sorted(list(self.found_words))

    def _dfs(self, r, c, current_word, visited):
        """Recursive DFS helper to explore the grid"""
        if (r, c) in visited:
            return

        current_word += self.grid[r][c]

        if not self._is_prefix(current_word):
            return

        if len(current_word) >= 3 and current_word in self.dictionary:
            self.found_words.add(current_word)

        visited.add((r, c))

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    self._dfs(nr, nc, current_word, visited.copy())

    def _is_prefix(self, prefix):
        """Fast prefix lookup"""
        return prefix in self.prefixes


def main():
    """Demo run for the Boggle solver"""
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

    grid2 = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "St", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary2 = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
        "ten", "went", "wet", "stont", "stqura"
    ]

    mygame2 = Boggle(grid2, dictionary2)
    print(mygame2.getSolution())


if __name__ == "__main__":
    main()
