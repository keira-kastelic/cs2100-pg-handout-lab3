import unittest
from src.q1 import triangular


class TestTriangular(unittest.TestCase):
    "Class to tests the triangulate method"

    "testing a small walue for triangular"
    def test_small_value(self) -> None:
        self.assertEqual(10, triangular(4))

    "testing a large value for triangular"
    def test_large_value(self) -> None:
        self.assertEqual(5050, triangular(100))
