import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_solution(filename):
    path = ROOT / "python" / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


class PythonSolutionTests(unittest.TestCase):
    def test_roman_to_integer(self):
        solution = load_solution("13_roman_to_integer.py")
        self.assertEqual(solution.romanToInt("III"), 3)
        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)

    def test_climbing_stairs(self):
        solution = load_solution("70_climbing_stairs.py")
        self.assertEqual(solution.climbStairs(1), 1)
        self.assertEqual(solution.climbStairs(5), 8)


if __name__ == "__main__":
    unittest.main()
