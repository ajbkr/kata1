import unittest

from main import price


class CheckOutTestCase(unittest.TestCase):
    def test_totals(self):
        self.assertEqual(0, price([]))
        self.assertEqual(50, price(["A"]))
        self.assertEqual(80, price(["A", "B"]))
        self.assertEqual(115, price(["C", "D", "B", "A"]))
        self.assertEqual(100, price(["A", "A"]))
        self.assertEqual(130, price(["A", "A", "A"]))
        self.assertEqual(180, price(["A", "A", "A", "A"]))
        self.assertEqual(230, price(["A", "A", "A", "A", "A"]))
        self.assertEqual(260, price(["A", "A", "A", "A", "A", "A"]))
        self.assertEqual(160, price(["A", "A", "A", "B"]))
        self.assertEqual(175, price(["A", "A", "A", "B", "B"]))
        self.assertEqual(190, price(["A", "A", "A", "B", "B", "D"]))
        self.assertEqual(190, price(["D", "A", "B", "A", "B", "A"]))


if __name__ == '__main__':
    unittest.main()
