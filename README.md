### Running the System

You can run the system using the main script with different options:

\`\`\`
python main.py [option]
\`\`\`

Options:
- `--help`: Display help message
- `--console`: Run the console-based interface (default)
- `--file`: Run the file-based interface
- `--demo`: Run a demonstration of the system
- `--test`: Run the test suite

### Console Interface

The console interface provides an interactive menu to access all functionality:

\`\`\`
python main.py --console
\`\`\`

### File Interface

The file interface allows processing frequencies from a file:

python main.py --file

This will:
1. Create a sample input file with frequencies
2. Process the file and generate an output file with analysis results
3. Display the contents of the output file

### Demo Mode

To see a quick demonstration of the system's capabilities:

\`\`\`
python main.py --demo
\`\`\`

## Examples

### EM Spectrum Analysis

```python
import color_analysis as ca

# Get frequency range for a color
freq_range = ca.get_frequency_range("Blue")
print(f"Frequency range for Blue: {freq_range} THz")  # (606, 668)

# Convert frequency to wavelength
wavelength = ca.frequency_to_wavelength(650)
print(f"Wavelength for 650 THz: {wavelength:.2f} nm")  # 461.22 nm

# Get color from frequency
color = ca.get_color_from_frequency(550)
print(f"Color for 550 THz: {color}")  # Green

# Compare two frequencies
result = ca.compare_frequencies(450, 650)
print(result)  # "The frequencies represent different colors: Red and Blue."
