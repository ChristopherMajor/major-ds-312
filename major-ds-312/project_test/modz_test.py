import unittest
from project.modz import enlarge


class TestMyMod(unittest.TestCase):
    def test_true(self):
        self.assertEqual(enlarge(3), 300)

if __name__ == "__main__":
    unittest.main()

# remember to run with this syntax when running a file that imports from another file. 
# python -m project_test.modz_test