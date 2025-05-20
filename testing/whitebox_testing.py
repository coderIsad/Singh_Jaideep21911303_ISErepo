# test_whitebox.py
# White-box test cases for the color analysis system

import unittest
import color_analysis as ca

class TestWhiteBox(unittest.TestCase):

    def test_compare_frequencies_paths(self):
        self.assertEqual(
            ca.compare_frequencies(0, 50000),
            "One or both frequencies are invalid."
        )
        self.assertEqual(
            ca.compare_frequencies(300, 900),
            "Both frequencies are outside the visible spectrum."
        )
        self.assertEqual(
            ca.compare_frequencies(300, 600),
            "The first frequency is outside the visible spectrum. The second frequency represents Blue."
        )
        self.assertEqual(
            ca.compare_frequencies(600, 900),
            "The second frequency is outside the visible spectrum. The first frequency represents Blue."
        )
        self.assertEqual(
            ca.compare_frequencies(550, 560),
            "Both frequencies represent the same color: Green."
        )
        self.assertEqual(
            ca.compare_frequencies(450, 650),
            "The frequencies represent different colors: Red and Blue."
        )

    def test_get_color_from_frequency_paths(self):
        self.assertEqual(
            ca.get_color_from_frequency(50000),
            "Invalid frequency. Please enter a frequency between 1 and 40000 THz."
        )
        self.assertEqual(
            ca.get_color_from_frequency(300),
            "This frequency is lower than that of red light and not in the visible spectrum."
        )
        self.assertEqual(
            ca.get_color_from_frequency(800),
            "This frequency is higher than that of violet light and not in the visible spectrum."
        )
        self.assertEqual(ca.get_color_from_frequency(450), "Red")
        self.assertEqual(ca.get_color_from_frequency(650), "Blue")

if __name__ == "__main__":
    unittest.main()
