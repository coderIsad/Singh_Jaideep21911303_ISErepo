# Constants for EM spectrum (in THz)
VISIBLE_LIGHT_MIN = 400  # THz
VISIBLE_LIGHT_MAX = 790  # THz
IR_MIN = 1  # THz
IR_MAX = 400  # THz
UV_MIN = 790  # THz
UV_MAX = 30000  # THz
VALID_FREQ_MIN = 1  # THz
VALID_FREQ_MAX = 40000  # THz

# Color frequency ranges (in THz)
COLOR_RANGES = {
    "Red": (400, 484),
    "Orange": (484, 508),
    "Yellow": (508, 526),
    "Green": (526, 606),
    "Blue": (606, 668),
    "Indigo": (668, 689),
    "Violet": (689, 790)
}

# Color associations
COLOR_STONES = {
    "Red": "Ruby",
    "Orange": "Amber",
    "Yellow": "Topaz",
    "Green": "Emerald",
    "Blue": "Sapphire",
    "Indigo": "Lapis Lazuli",
    "Violet": "Amethyst"
}

COLOR_NOTES = {
    "Red": "C",
    "Orange": "D",
    "Yellow": "E",
    "Green": "F",
    "Blue": "G",
    "Indigo": "A",
    "Violet": "B"
}

COLOR_EMOTIONS = {
    "Red": "Passion and Energy",
    "Orange": "Enthusiasm and Creativity",
    "Yellow": "Happiness and Optimism",
    "Green": "Growth and Harmony",
    "Blue": "Calm and Trust",
    "Indigo": "Intuition and Perception",
    "Violet": "Imagination and Spirituality"
}

def is_valid_frequency(frequency):
    """
    Check if a frequency is within the valid range.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        bool: True if frequency is valid, False otherwise
    """
    return VALID_FREQ_MIN <= frequency <= VALID_FREQ_MAX

def is_visible_light(frequency):
    """
    Check if a frequency is within the visible light range.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        bool: True if frequency is in visible light range, False otherwise
    """
    return VISIBLE_LIGHT_MIN <= frequency <= VISIBLE_LIGHT_MAX

def is_ir_range(frequency):
    """
    Check if a frequency is within the IR range.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        bool: True if frequency is in IR range, False otherwise
    """
    return IR_MIN <= frequency <= IR_MAX

def is_uv_range(frequency):
    """
    Check if a frequency is within the UV range.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        bool: True if frequency is in UV range, False otherwise
    """
    return UV_MIN <= frequency <= UV_MAX

def get_color_from_frequency(frequency):
    """
    Get the color name from a frequency.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        str: Color name or appropriate message
    """
    if not is_valid_frequency(frequency):
        return "Invalid frequency. Please enter a frequency between 1 and 40000 THz."
    
    if not is_visible_light(frequency):
        if frequency < VISIBLE_LIGHT_MIN:
            return "This frequency is lower than that of red light and not in the visible spectrum."
        else:
            return "This frequency is higher than that of violet light and not in the visible spectrum."
    
    for color, (lower, upper) in COLOR_RANGES.items():
        if lower <= frequency <= upper:
            return color
    
    return "No specific color found for this frequency."

def get_frequency_range(color_name):
    """
    Get the frequency range for a given color name.
    
    Args:
        color_name (str): Name of the color
        
    Returns:
        tuple: (lower_bound, upper_bound) in THz or None if color not found
    """
    color_name = color_name.capitalize()
    return COLOR_RANGES.get(color_name)

def frequency_to_wavelength(frequency):
    """
    Convert frequency to wavelength using c = λν.
    
    Args:
        frequency (int): Frequency in THz
        
    Returns:
        float: Wavelength in nanometers
    """
    if not is_valid_frequency(frequency):
        return None
    
    # Speed of light in nm/s
    c = 299792458 * 1e9
    # Convert THz to Hz
    frequency_hz = frequency * 1e12
    # Calculate wavelength in nm
    wavelength = c / frequency_hz
    
    return wavelength

def wavelength_to_frequency(wavelength):
    """
    Convert wavelength to frequency using ν = c/λ.
    
    Args:
        wavelength (float): Wavelength in nanometers
        
    Returns:
        float: Frequency in THz
    """
    if wavelength <= 0:
        return None
    
    # Speed of light in nm/s
    c = 299792458 * 1e9
    # Calculate frequency in Hz
    frequency_hz = c / wavelength
    # Convert Hz to THz
    frequency = frequency_hz / 1e12
    
    return frequency

def compare_frequencies(freq1, freq2):
    """
    Compare two frequencies to determine if they represent the same color.
    
    Args:
        freq1 (int): First frequency in THz
        freq2 (int): Second frequency in THz
        
    Returns:
        str: Result of comparison
    """
    if not is_valid_frequency(freq1) or not is_valid_frequency(freq2):
        return "One or both frequencies are invalid."
    
    color1 = get_color_from_frequency(freq1)
    color2 = get_color_from_frequency(freq2)
    
    if not is_visible_light(freq1) and not is_visible_light(freq2):
        return "Both frequencies are outside the visible spectrum."
    elif not is_visible_light(freq1):
        return f"The first frequency is outside the visible spectrum. The second frequency represents {color2}."
    elif not is_visible_light(freq2):
        return f"The second frequency is outside the visible spectrum. The first frequency represents {color1}."
    
    if color1 == color2:
        return f"Both frequencies represent the same color: {color1}."
    else:
        return f"The frequencies represent different colors: {color1} and {color2}."

def get_stone_for_color(color_name):
    """
    Get the stone associated with a color.
    
    Args:
        color_name (str): Name of the color
        
    Returns:
        str: Name of the stone or error message
    """
    color_name = color_name.capitalize()
    if color_name in COLOR_STONES:
        return COLOR_STONES[color_name]
    else:
        return "No stone found for this color."

def get_note_for_color(color_name):
    """
    Get the musical note associated with a color.
    
    Args:
        color_name (str): Name of the color
        
    Returns:
        str: Musical note or error message
    """
    color_name = color_name.capitalize()
    if color_name in COLOR_NOTES:
        return COLOR_NOTES[color_name]
    else:
        return "No musical note found for this color."

def get_emotion_for_color(color_name):
    """
    Get the emotion associated with a color.
    
    Args:
        color_name (str): Name of the color
        
    Returns:
        str: Emotion description or error message
    """
    color_name = color_name.capitalize()
    if color_name in COLOR_EMOTIONS:
        return COLOR_EMOTIONS[color_name]
    else:
        return "No emotion found for this color."

# Main function to demonstrate functionality
def main():
    print("Color Analysis System")
    print("=====================")
    
    # Demo for EM spectrum functions
    print("\nEM Spectrum Functions:")
    print("-----------------------")
    
    # Get frequency range for a color
    color = "Blue"
    freq_range = get_frequency_range(color)
    print(f"Frequency range for {color}: {freq_range} THz")
    
    # Convert frequency to wavelength
    freq = 650
    wavelength = frequency_to_wavelength(freq)
    print(f"Wavelength for {freq} THz: {wavelength:.2f} nm")
    
    # Convert wavelength to frequency
    wl = 500
    freq = wavelength_to_frequency(wl)
    print(f"Frequency for {wl} nm: {freq:.2f} THz")
    
    # Check if frequency is in visible range
    freq = 650
    print(f"Is {freq} THz in visible range? {is_visible_light(freq)}")
    
    # Check if frequency is in IR range
    freq = 300
    print(f"Is {freq} THz in IR range? {is_ir_range(freq)}")
    
    # Check if frequency is in UV range
    freq = 1000
    print(f"Is {freq} THz in UV range? {is_uv_range(freq)}")
    
    # Get color from frequency
    freq = 650
    color = get_color_from_frequency(freq)
    print(f"Color for {freq} THz: {color}")
    
    # Compare two frequencies
    freq1 = 450
    freq2 = 650
    result = compare_frequencies(freq1, freq2)
    print(f"Comparing {freq1} THz and {freq2} THz: {result}")
    
    # Demo for Color Fun Facts functions
    print("\nColor Fun Facts Functions:")
    print("--------------------------")
    
    # Get stone for a color
    color = "Red"
    stone = get_stone_for_color(color)
    print(f"Stone for {color}: {stone}")
    
    # Get musical note for a color
    note = get_note_for_color(color)
    print(f"Musical note for {color}: {note}")
    
    # Get emotion for a color
    emotion = get_emotion_for_color(color)
    print(f"Emotion for {color}: {emotion}")

if __name__ == "__main__":
    main()