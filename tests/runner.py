import unittest
import os
import sys

# Ensure the `tests` directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'tests')))

# Discover and run all test cases
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
