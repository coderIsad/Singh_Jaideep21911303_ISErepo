# white_box_tests.py
# White box testing for the color analysis system

import unittest
import os
import io
import sys
from contextlib import redirect_stdout
import color_analysis as ca

class ColorAnalysisWhiteBoxTests(unittest.TestCase):
    """White box tests for the color analysis system."""
    
 
    # 1. Control Flow Testing
 
    
    def test_get_color_from_frequency_control_flow(self):
        """Test all control flow paths in get_color_from_frequency."""
        # Path: Invalid frequency
        self.assertEqual(
            ca.get_color_from_frequency(50000),
            "Invalid frequency. Please enter a frequency between 1 and 40000 THz."
        )
        
        # Path: Below visible range
        self.assertEqual(
            ca.get_color_from_frequency(300),
            "This frequency is lower than that of red light and not in the visible spectrum."
        )
        
        # Path: Above visible range
        self.assertEqual(
            ca.get_color_from_frequency(800),
            "This frequency is higher than that of violet light and not in the visible spectrum."
        )
        
        # Path: In Red range (first color in the loop)
        self.assertEqual(ca.get_color_from_frequency(450), "Red")
        
        # Path: In Green range (middle color in the loop)
        self.assertEqual(ca.get_color_from_frequency(550), "Green")
        
        # Path: In Violet range (last color in the loop)
        self.assertEqual(ca.get_color_from_frequency(750), "Violet")
    
    def test_compare_frequencies_control_flow(self):
        """Test all control flow paths in compare_frequencies."""
        # Path: One frequency invalid
        self.assertEqual(
            ca.compare_frequencies(0, 500),
            "One or both frequencies are invalid."
        )
        
        # Path: Both frequencies invalid
        self.assertEqual(
            ca.compare_frequencies(0, 50000),
            "One or both frequencies are invalid."
        )
        
        # Path: Both outside visible spectrum
        self.assertEqual(
            ca.compare_frequencies(300, 900),
            "Both frequencies are outside the visible spectrum."
        )
        
        # Path: First outside visible spectrum
        self.assertEqual(
            ca.compare_frequencies(300, 500),
            "The first frequency is outside the visible spectrum. The second frequency represents Orange."
        )
        
        # Path: Second outside visible spectrum
        self.assertEqual(
            ca.compare_frequencies(500, 900),
            "The second frequency is outside the visible spectrum. The first frequency represents Orange."
        )
        
        # Path: Same color
        self.assertEqual(
            ca.compare_frequencies(450, 460),
            "Both frequencies represent the same color: Red."
        )
        
        # Path: Different colors
        self.assertEqual(
            ca.compare_frequencies(450, 550),
            "The frequencies represent different colors: Red and Green."
        )
    
 
    # 2. Data Flow Testing
 
    
    def test_frequency_to_wavelength_data_flow(self):
        """Test data flow in frequency_to_wavelength."""
        # Valid frequency - test the flow of frequency through the calculation
        wavelength = ca.frequency_to_wavelength(500)
        self.assertAlmostEqual(wavelength, 599.58, places=2)
        
        # Invalid frequency - test early return path
        self.assertIsNone(ca.frequency_to_wavelength(0))
        
        # Very small frequency - test precision with extreme values
        wavelength = ca.frequency_to_wavelength(1)
        self.assertAlmostEqual(wavelength, 299792.46, places=2)
        
        # Very large frequency - test precision with extreme values
        wavelength = ca.frequency_to_wavelength(40000)
        self.assertAlmostEqual(wavelength, 7.49, places=2)
    
    def test_wavelength_to_frequency_data_flow(self):
        """Test data flow in wavelength_to_frequency."""
        # Valid wavelength - test the flow of wavelength through the calculation
        frequency = ca.wavelength_to_frequency(500)
        self.assertAlmostEqual(frequency, 599.58, places=2)
        
        # Zero wavelength - test early return path
        self.assertIsNone(ca.wavelength_to_frequency(0))
        
        # Negative wavelength - test early return path
        self.assertIsNone(ca.wavelength_to_frequency(-100))
        
        # Wavelength that results in 1 THz - test precision
        frequency = ca.wavelength_to_frequency(299792.458)
        self.assertAlmostEqual(frequency, 1.0, places=2)
    
 
    # 3. Branch Coverage Testing
 
    
    def test_get_stone_for_color_branches(self):
        """Test all branches in get_stone_for_color."""
        # Branch: Valid color
        self.assertEqual(ca.get_stone_for_color("Red"), "Ruby")
        
        # Branch: Invalid color
        self.assertEqual(
            ca.get_stone_for_color("Pink"),
            "No stone found for this color."
        )
        
        # Branch: Case insensitive
        self.assertEqual(ca.get_stone_for_color("red"), "Ruby")
    
    def test_get_note_for_color_branches(self):
        """Test all branches in get_note_for_color."""
        # Branch: Valid color
        self.assertEqual(ca.get_note_for_color("Blue"), "G")
        
        # Branch: Invalid color
        self.assertEqual(
            ca.get_note_for_color("Pink"),
            "No musical note found for this color."
        )
        
        # Branch: Case insensitive
        self.assertEqual(ca.get_note_for_color("blue"), "G")
    
    def test_get_emotion_for_color_branches(self):
        """Test all branches in get_emotion_for_color."""
        # Branch: Valid color
        self.assertEqual(ca.get_emotion_for_color("Yellow"), "Happiness and Optimism")
        
        # Branch: Invalid color
        self.assertEqual(
            ca.get_emotion_for_color("Pink"),
            "No emotion found for this color."
        )
        
        # Branch: Case insensitive
        self.assertEqual(ca.get_emotion_for_color("yellow"), "Happiness and Optimism")
    
    def test_is_valid_frequency_branches(self):
        """Test all branches in is_valid_frequency."""
        # Branch: Valid frequency
        self.assertTrue(ca.is_valid_frequency(500))
        
        # Branch: Below minimum
        self.assertFalse(ca.is_valid_frequency(0))
        
        # Branch: Above maximum
        self.assertFalse(ca.is_valid_frequency(50000))
    
    def test_is_visible_light_branches(self):
        """Test all branches in is_visible_light."""
        # Branch: In visible range
        self.assertTrue(ca.is_visible_light(500))
        
        # Branch: Below visible range
        self.assertFalse(ca.is_visible_light(300))
        
        # Branch: Above visible range
        self.assertFalse(ca.is_visible_light(800))
    
    def test_is_ir_range_branches(self):
        """Test all branches in is_ir_range."""
        # Branch: In IR range
        self.assertTrue(ca.is_ir_range(200))
        
        # Branch: Below IR range
        self.assertFalse(ca.is_ir_range(0))
        
        # Branch: Above IR range
        self.assertFalse(ca.is_ir_range(500))
    
    def test_is_uv_range_branches(self):
        """Test all branches in is_uv_range."""
        # Branch: In UV range
        self.assertTrue(ca.is_uv_range(1000))
        
        # Branch: Below UV range
        self.assertFalse(ca.is_uv_range(500))
        
        # Branch: Above UV range
        self.assertFalse(ca.is_uv_range(35000))
    
 
    # 4. Statement Coverage Testing
 
    
    def test_get_frequency_range_statements(self):
        """Test all statements in get_frequency_range."""
        # Valid color name
        self.assertEqual(ca.get_frequency_range("Red"), (400, 484))
        
        # Valid color name with different case
        self.assertEqual(ca.get_frequency_range("red"), (400, 484))
        
        # Invalid color name
        self.assertIsNone(ca.get_frequency_range("Pink"))
    
    def test_main_function_statements(self):
        """Test statements in the main function."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            ca.main()
        
        output = captured_output.getvalue()
        
        # Check if key phrases are in the output
        self.assertIn("Color Analysis System", output)
        self.assertIn("EM Spectrum Functions", output)
        self.assertIn("Color Fun Facts Functions", output)
        self.assertIn("Frequency range for Blue", output)
        self.assertIn("Wavelength for 650 THz", output)
    
 
    # 5. Loop Testing
 
    
    def test_get_color_from_frequency_loop(self):
        """Test the loop in get_color_from_frequency."""
        # First color in range (Red)
        self.assertEqual(ca.get_color_from_frequency(450), "Red")
        
        # Middle color in range (Blue)
        self.assertEqual(ca.get_color_from_frequency(650), "Blue")
        
        # Last color in range (Violet)
        self.assertEqual(ca.get_color_from_frequency(750), "Violet")
    
 
    # 6. Condition Testing
 
    
    def test_is_visible_light_conditions(self):
        """Test all condition combinations in is_visible_light."""
        # Both conditions true
        self.assertTrue(ca.is_visible_light(500))
        
        # First condition false, second true
        self.assertFalse(ca.is_visible_light(300))
        
        # First condition true, second false
        self.assertFalse(ca.is_visible_light(800))
        
        # Both conditions false
        self.assertFalse(ca.is_visible_light(-100))
    
    def test_compare_frequencies_conditions(self):
        """Test condition combinations in compare_frequencies."""
        # Both frequencies valid
        result = ca.compare_frequencies(500, 600)
        self.assertIn("The frequencies represent different colors", result)
        
        # First frequency invalid
        self.assertEqual(
            ca.compare_frequencies(0, 500),
            "One or both frequencies are invalid."
        )
        
        # Second frequency invalid
        self.assertEqual(
            ca.compare_frequencies(500, 50000),
            "One or both frequencies are invalid."
        )
        
        # Both frequencies invalid
        self.assertEqual(
            ca.compare_frequencies(0, 50000),
            "One or both frequencies are invalid."
        )
        
        # Both outside visible spectrum
        self.assertEqual(
            ca.compare_frequencies(300, 900),
            "Both frequencies are outside the visible spectrum."
        )
    
 
    # 7. Path Testing for Complex Functions
 
    
    def test_file_interface_paths(self):
        """Test paths in file interface functions."""
        import file_interface as fi
        
        # Create a temporary input file
        input_filename = "test_input.txt"
        output_filename = "test_output.txt"
        
        # Path 1: Valid frequencies
        test_frequencies = [450, 550, 650]
        fi.create_sample_input_file(input_filename, test_frequencies)
        
        # Process the file
        fi.process_batch_file(input_filename, output_filename)
        
        # Check if the output file exists
        self.assertTrue(os.path.exists(output_filename))
        
        # Path 2: Empty file
        fi.create_sample_input_file("empty.txt", [])
        
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            fi.process_batch_file("empty.txt", "empty_output.txt")
        
        output = captured_output.getvalue()
        self.assertIn("No valid frequencies found", output)
        
        # Path 3: Invalid content
        fi.create_sample_input_file("invalid.txt", ["abc", "def"])
        
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            fi.process_batch_file("invalid.txt", "invalid_output.txt")
        
        output = captured_output.getvalue()
        self.assertIn("No valid frequencies found", output)
        
        # Clean up
        for filename in [input_filename, output_filename, "empty.txt", "invalid.txt"]:
            if os.path.exists(filename):
                os.remove(filename)
    
 
    # 8. Student ID and Name Testing
 
    
    def test_student_id_123(self):
        """Test with the last three digits of a student ID (123)."""
        # Valid frequency path
        self.assertTrue(ca.is_valid_frequency(123))
        
        # Below visible range path
        self.assertFalse(ca.is_visible_light(123))
        
        # In IR range path
        self.assertTrue(ca.is_ir_range(123))
        
        # Below visible range message path
        self.assertEqual(
            ca.get_color_from_frequency(123),
            "This frequency is lower than that of red light and not in the visible spectrum."
        )
    
    def test_student_name_smith(self):
        """Test with the student's last name."""
        # Invalid color name path for get_stone_for_color
        self.assertEqual(
            ca.get_stone_for_color("Smith"),
            "No stone found for this color."
        )
        
        # Invalid color name path for get_note_for_color
        self.assertEqual(
            ca.get_note_for_color("Smith"),
            "No musical note found for this color."
        )
        
        # Invalid color name path for get_emotion_for_color
        self.assertEqual(
            ca.get_emotion_for_color("Smith"),
            "No emotion found for this color."
        )
    

    # 9. Exception Testing
 
    
    def test_file_interface_exceptions(self):
        """Test exception handling in file interface."""
        import file_interface as fi
        
        # FileNotFoundError
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            frequencies = fi.read_frequencies_from_file("nonexistent.txt")
        
        output = captured_output.getvalue()
        self.assertIn("File nonexistent.txt not found", output)
        self.assertEqual(frequencies, [])
        
        # ValueError
        # Create a file with invalid content
        with open("invalid_content.txt", "w") as f:
            f.write("450\nabc\n650\n")
        
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            frequencies = fi.read_frequencies_from_file("invalid_content.txt")
        
        output = captured_output.getvalue()
        self.assertIn("Warning: Ignoring invalid frequency value: abc", output)
        self.assertEqual(frequencies, [450, 650])
        
        # Clean up
        if os.path.exists("invalid_content.txt"):
            os.remove("invalid_content.txt")
    
 
    # 10. Integration Testing
 
    
    def test_color_analysis_file_interface_integration(self):
        """Test integration between color_analysis and file_interface."""
        import file_interface as fi
        
        # Create a temporary input file
        input_filename = "integration_test_input.txt"
        output_filename = "integration_test_output.txt"
        
        # Test with valid frequencies
        test_frequencies = [450, 550, 650]
        fi.create_sample_input_file(input_filename, test_frequencies)
        
        # Process the file
        fi.process_batch_file(input_filename, output_filename)
        
        # Check if the output file exists and contains expected content
        self.assertTrue(os.path.exists(output_filename))
        
        with open(output_filename, "r") as f:
            content = f.read()
            self.assertIn("Frequency: 450 THz", content)
            self.assertIn("Color: Red", content)
            self.assertIn("Frequency: 550 THz", content)
            self.assertIn("Color: Green", content)
            self.assertIn("Frequency: 650 THz", content)
            self.assertIn("Color: Blue", content)
        
        # Test with invalid frequencies
        test_frequencies = [0, 50000]
        fi.create_sample_input_file("invalid_freq.txt", test_frequencies)
        
        # Process the file
        fi.process_batch_file("invalid_freq.txt", "invalid_freq_output.txt")
        
        # Check if the output file exists and contains expected content
        self.assertTrue(os.path.exists("invalid_freq_output.txt"))
        
        with open("invalid_freq_output.txt", "r") as f:
            content = f.read()
            self.assertIn("Frequency: 0 THz", content)
            self.assertIn("Invalid frequency", content)
            self.assertIn("Frequency: 50000 THz", content)
            self.assertIn("Invalid frequency", content)
        
        # Clean up
        for filename in [input_filename, output_filename, "invalid_freq.txt", "invalid_freq_output.txt"]:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    unittest.main(verbosity=2)
