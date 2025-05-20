# file_interface.py
# Module for handling file-based inputs and outputs

import color_analysis as ca
import os

def read_frequencies_from_file(filename):
    """
    Read frequencies from a file.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        list: List of frequencies read from the file
    """
    frequencies = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    freq = int(line.strip())
                    frequencies.append(freq)
                except ValueError:
                    print(f"Warning: Ignoring invalid frequency value: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return frequencies

def write_analysis_to_file(frequencies, filename):
    """
    Write color analysis results to a file.
    
    Args:
        frequencies (list): List of frequencies to analyze
        filename (str): Path to the output file
    """
    try:
        with open(filename, 'w') as file:
            file.write("Color Analysis Results\n")
            file.write("=====================\n\n")
            
            for freq in frequencies:
                file.write(f"Frequency: {freq} THz\n")
                
                if ca.is_valid_frequency(freq):
                    file.write(f"Wavelength: {ca.frequency_to_wavelength(freq):.2f} nm\n")
                    file.write(f"In visible range: {ca.is_visible_light(freq)}\n")
                    file.write(f"In IR range: {ca.is_ir_range(freq)}\n")
                    file.write(f"In UV range: {ca.is_uv_range(freq)}\n")
                    
                    color = ca.get_color_from_frequency(freq)
                    file.write(f"Color: {color}\n")
                    
                    if ca.is_visible_light(freq):
                        for color_name, (lower, upper) in ca.COLOR_RANGES.items():
                            if lower <= freq <= upper:
                                file.write(f"Stone: {ca.get_stone_for_color(color_name)}\n")
                                file.write(f"Musical note: {ca.get_note_for_color(color_name)}\n")
                                file.write(f"Emotion: {ca.get_emotion_for_color(color_name)}\n")
                                break
                else:
                    file.write("Invalid frequency.\n")
                
                file.write("\n")
            
            print(f"Analysis results written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def process_batch_file(input_filename, output_filename):
    """
    Process a batch of frequencies from an input file and write results to an output file.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path to the output file
    """
    frequencies = read_frequencies_from_file(input_filename)
    
    if frequencies:
        write_analysis_to_file(frequencies, output_filename)
    else:
        print("No valid frequencies found in the input file.")

def create_sample_input_file(filename, frequencies):
    """
    Create a sample input file with the given frequencies.
    
    Args:
        filename (str): Path to the file to create
        frequencies (list): List of frequencies to write to the file
    """
    try:
        with open(filename, 'w') as file:
            for freq in frequencies:
                file.write(f"{freq}\n")
        print(f"Sample input file created: {filename}")
    except Exception as e:
        print(f"Error creating sample file: {e}")

def run_file_interface():
    """Run the file-based interface."""
    print("\nColor Analysis System - File Interface")
    print("=====================================")
    
    # Create a sample input file
    sample_frequencies = [450, 550, 650, 750, 350, 850]
    input_filename = "input_frequencies.txt"
    create_sample_input_file(input_filename, sample_frequencies)
    
    # Process the input file
    output_filename = "color_analysis_results.txt"
    process_batch_file(input_filename, output_filename)
    
    # Display the contents of the output file
    try:
        print("\nContents of the output file:")
        print("===========================")
        with open(output_filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Output file {output_filename} not found.")
    except Exception as e:
        print(f"Error reading output file: {e}")

if __name__ == "__main__":
    run_file_interface()


def run_file_interface():
    """Run the file-based interface."""
    print("\nColor Analysis System - File Interface")
    print("=====================================")
    
    # Create a sample input file
    sample_frequencies = [450, 550, 650, 750, 350, 850]
    input_filename = "input_frequencies.txt"
    create_sample_input_file(input_filename, sample_frequencies)
    
    # Process the input file
    output_filename = "color_analysis_results.txt"
    process_batch_file(input_filename, output_filename)
    
    # Display the contents of the output file
    try:
        print("\nContents of the output file:")
        print("===========================")
        with open(output_filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Output file {output_filename} not found.")
    except Exception as e:
        print(f"Error reading output file: {e}")
    # Create a sample input file
    sample_frequencies = [450, 550, 650, 750, 350, 850]
    input_filename = "input_frequencies.txt"
    create_sample_input_file(input_filename, sample_frequencies)
    # Process the input file
    output_filename = "color_analysis_results.txt"
    process_batch_file(input_filename, output_filename)
    # Display the contents of the output file
    try:
        print("\nContents of the output file:")
        print("===========================")
        with open(output_filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Output file {output_filename} not found.")
    except Exception as e:
        print(f"Error reading output file: {e}")    


def run_file_interface():
    """Run the file-based interface."""
    print("\nColor Analysis System - File Interface")
    print("=====================================")
    
    # Create a sample input file
    sample_frequencies = [450, 550, 650, 750, 350, 850]
    input_filename = "input_frequencies.txt"
    create_sample_input_file(input_filename, sample_frequencies)
    
    # Process the input file
    output_filename = "color_analysis_results.txt"
    process_batch_file(input_filename, output_filename)
    
    # Display the contents of the output file
    try:
        print("\nContents of the output file:")
        print("===========================")
        with open(output_filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Output file {output_filename} not found.")
    except Exception as e:
        print(f"Error reading output file: {e}")




