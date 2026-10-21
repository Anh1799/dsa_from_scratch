
import unittest
from dsa.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")
        self.graph.add_edge("B", "E")
        self.graph.add_edge("C", "E")

    def test_remove_edge(self):
        self.assertTrue(
            self.graph.remove_edge("A", "B")
        )
        self.assertNotIn("B", self.graph.adj["A"])
        self.assertNotIn("A", self.graph.adj["B"])

    def test_remove_missing_edge(self):
        self.assertFalse(
            self.graph.remove_edge("A", "D")
        )

    def test_has_path(self):
        self.assertTrue(
            self.graph.has_path("A", "D")
        )

    def test_no_path(self):
        self.graph.remove_edge("B", "D")
        self.assertFalse(
            self.graph.has_path("A", "D")
        )

    def test_shortest_path(self):
        self.assertEqual(
            self.graph.shortest_path("A", "D"),
            ["A", "B", "D"]
        )

    def test_shortest_path_missing(self):
        self.assertEqual(
            self.graph.shortest_path("A", "Z"),
            []
        )

    def test_same_start_and_end(self):
        self.assertEqual(
            self.graph.shortest_path("A", "A"),
            ["A"]
        )

    def test_remove_self_loop(self):
        self.graph.add_edge("A", "A")
        self.assertTrue(
            self.graph.remove_edge("A", "A")
        )
        self.assertNotIn("A", self.graph.adj["A"])


if __name__ == "__main__":
    unittest.main()
