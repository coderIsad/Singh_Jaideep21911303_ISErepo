# test_blackbox.py
# Black-box test cases for the color analysis system

import unittest
import color_analysis as ca
import os
import io
from contextlib import redirect_stdout

class TestBlackBox(unittest.TestCase):

    # Equivalence Partitioning

    def test_is_valid_frequency_ep(self):
        self.assertTrue(ca.is_valid_frequency(1))
        self.assertTrue(ca.is_valid_frequency(20000))
        self.assertTrue(ca.is_valid_frequency(40000))
        self.assertFalse(ca.is_valid_frequency(0))
        self.assertFalse(ca.is_valid_frequency(-10))
        self.assertFalse(ca.is_valid_frequency(40001))

    def test_is_visible_light_ep(self):
        self.assertTrue(ca.is_visible_light(400))
        self.assertTrue(ca.is_visible_light(600))
        self.assertTrue(ca.is_visible_light(790))
        self.assertFalse(ca.is_visible_light(399))
        self.assertFalse(ca.is_visible_light(791))

    def test_get_color_from_frequency_ep(self):
        self.assertEqual(ca.get_color_from_frequency(450), "Red")
        self.assertEqual(ca.get_color_from_frequency(550), "Green")
        self.assertEqual(ca.get_color_from_frequency(750), "Violet")
        self.assertEqual(ca.get_color_from_frequency(350),
                         "This frequency is lower than that of red light and not in the visible spectrum.")
        self.assertEqual(ca.get_color_from_frequency(800),
                         "This frequency is higher than that of violet light and not in the visible spectrum.")
        self.assertEqual(ca.get_color_from_frequency(50000),
                         "Invalid frequency. Please enter a frequency between 1 and 40000 THz.")

    def test_get_frequency_range_ep(self):
        self.assertEqual(ca.get_frequency_range("Red"), (400, 484))
        self.assertEqual(ca.get_frequency_range("Green"), (526, 606))
        self.assertEqual(ca.get_frequency_range("Violet"), (689, 790))
        self.assertEqual(ca.get_frequency_range("red"), (400, 484))
        self.assertEqual(ca.get_frequency_range("GREEN"), (526, 606))
        self.assertIsNone(ca.get_frequency_range("Pink"))
        self.assertIsNone(ca.get_frequency_range(""))

    # Boundary Value Analysis

    def test_is_valid_frequency_bva(self):
        self.assertFalse(ca.is_valid_frequency(0))
        self.assertTrue(ca.is_valid_frequency(1))
        self.assertTrue(ca.is_valid_frequency(2))
        self.assertTrue(ca.is_valid_frequency(39999))
        self.assertTrue(ca.is_valid_frequency(40000))
        self.assertFalse(ca.is_valid_frequency(40001))

    def test_is_visible_light_bva(self):
        self.assertFalse(ca.is_visible_light(399))
        self.assertTrue(ca.is_visible_light(400))
        self.assertTrue(ca.is_visible_light(401))
        self.assertTrue(ca.is_visible_light(789))
        self.assertTrue(ca.is_visible_light(790))
        self.assertFalse(ca.is_visible_light(791))

    def test_frequency_to_wavelength_bva(self):
        self.assertIsNotNone(ca.frequency_to_wavelength(1))
        self.assertIsNotNone(ca.frequency_to_wavelength(40000))
        self.assertIsNone(ca.frequency_to_wavelength(0))
        self.assertIsNone(ca.frequency_to_wavelength(40001))

    # Required by assignment: student ID & name

    def test_student_id_values(self):
        freq = 123
        self.assertTrue(ca.is_valid_frequency(freq))
        self.assertTrue(ca.is_ir_range(freq))
        self.assertFalse(ca.is_visible_light(freq))
        self.assertEqual(
            ca.get_color_from_frequency(freq),
            "This frequency is lower than that of red light and not in the visible spectrum."
        )

    def test_student_name(self):
        color_name = "Green"
        self.assertEqual(ca.get_stone_for_color(color_name), "Emerald")
        self.assertEqual(ca.get_note_for_color(color_name), "F")
        self.assertEqual(ca.get_emotion_for_color(color_name), "Growth and Harmony")

    def test_main_function_output(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            ca.main()
        output = captured_output.getvalue()
        self.assertIn("Color Analysis System", output)
        self.assertIn("EM Spectrum Functions", output)
        self.assertIn("Color Fun Facts Functions", output)
        self.assertIn("Frequency range for Blue", output)
        self.assertIn("Wavelength for 650 THz", output)

if __name__ == "__main__":
    unittest.main()
