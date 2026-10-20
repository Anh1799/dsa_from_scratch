
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

    def test_bfs(self):
        self.assertEqual(
            self.graph.bfs("A"),
            ["A", "B", "C", "D", "E"]
        )

    def test_dfs(self):
        self.assertEqual(
            self.graph.dfs("A"),
            ["A", "B", "D", "E", "C"]
        )

    def test_duplicate_edge(self):
        self.graph.add_edge("A", "B")
        self.assertEqual(
            self.graph.adj["A"].count("B"), 1
        )

    def test_missing_vertex(self):
        with self.assertRaises(KeyError):
            self.graph.bfs("Z")

if __name__ == "__main__":
    unittest.main()
