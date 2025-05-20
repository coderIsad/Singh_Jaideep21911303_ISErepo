# user_interface.py
# Module for handling user interactions

import color_analysis as ca

def display_menu():
    """Display the main menu options."""
    print("\nColor Analysis System")
    print("=====================")
    print("1. EM Spectrum Analysis")
    print("2. Color Fun Facts")
    print("3. Exit")
    return input("Enter your choice (1-3): ")

def em_spectrum_menu():
    """Display the EM Spectrum Analysis menu options."""
    print("\nEM Spectrum Analysis")
    print("===================")
    print("1. Get frequency range for a color")
    print("2. Convert frequency to wavelength")
    print("3. Convert wavelength to frequency")
    print("4. Check if frequency is in visible/IR/UV range")
    print("5. Get color from frequency")
    print("6. Compare two frequencies")
    print("7. Back to main menu")
    return input("Enter your choice (1-7): ")

def color_fun_facts_menu():
    """Display the Color Fun Facts menu options."""
    print("\nColor Fun Facts")
    print("==============")
    print("1. Get stone for a color")
    print("2. Get musical note for a color")
    print("3. Get emotion for a color")
    print("4. Back to main menu")
    return input("Enter your choice (1-4): ")

def get_color_input():
    """Get a color name from the user."""
    print("\nValid colors: Red, Orange, Yellow, Green, Blue, Indigo, Violet")
    color = input("Enter a color name: ")
    return color

def get_frequency_input():
    """Get a frequency value from the user."""
    while True:
        try:
            freq = int(input("Enter a frequency (in THz): "))
            if ca.is_valid_frequency(freq):
                return freq
            else:
                print(f"Please enter a valid frequency between {ca.VALID_FREQ_MIN} and {ca.VALID_FREQ_MAX} THz.")
        except ValueError:
            print("Please enter a valid integer.")

def get_wavelength_input():
    """Get a wavelength value from the user."""
    while True:
        try:
            wl = float(input("Enter a wavelength (in nm): "))
            if wl > 0:
                return wl
            else:
                print("Please enter a positive wavelength value.")
        except ValueError:
            print("Please enter a valid number.")

def handle_em_spectrum():
    """Handle the EM Spectrum Analysis menu options."""
    while True:
        choice = em_spectrum_menu()
        
        if choice == '1':
            color = get_color_input()
            freq_range = ca.get_frequency_range(color)
            if freq_range:
                print(f"Frequency range for {color}: {freq_range[0]} - {freq_range[1]} THz")
            else:
                print(f"No frequency range found for {color}.")
        
        elif choice == '2':
            freq = get_frequency_input()
            wavelength = ca.frequency_to_wavelength(freq)
            print(f"Wavelength for {freq} THz: {wavelength:.2f} nm")
        
        elif choice == '3':
            wl = get_wavelength_input()
            freq = ca.wavelength_to_frequency(wl)
            print(f"Frequency for {wl} nm: {freq:.2f} THz")
        
        elif choice == '4':
            freq = get_frequency_input()
            print(f"Is {freq} THz in visible range? {ca.is_visible_light(freq)}")
            print(f"Is {freq} THz in IR range? {ca.is_ir_range(freq)}")
            print(f"Is {freq} THz in UV range? {ca.is_uv_range(freq)}")
        
        elif choice == '5':
            freq = get_frequency_input()
            color = ca.get_color_from_frequency(freq)
            print(f"Color for {freq} THz: {color}")
        
        elif choice == '6':
            print("Enter the first frequency:")
            freq1 = get_frequency_input()
            print("Enter the second frequency:")
            freq2 = get_frequency_input()
            result = ca.compare_frequencies(freq1, freq2)
            print(f"Result: {result}")
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")

def handle_color_fun_facts():
    """Handle the Color Fun Facts menu options."""
    while True:
        choice = color_fun_facts_menu()
        
        if choice == '1':
            color = get_color_input()
            stone = ca.get_stone_for_color(color)
            print(f"Stone for {color}: {stone}")
        
        elif choice == '2':
            color = get_color_input()
            note = ca.get_note_for_color(color)
            print(f"Musical note for {color}: {note}")
        
        elif choice == '3':
            color = get_color_input()
            emotion = ca.get_emotion_for_color(color)
            print(f"Emotion for {color}: {emotion}")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

def run_interface():
    """Run the main user interface."""
    while True:
        choice = display_menu()
        
        if choice == '1':
            handle_em_spectrum()
        
        elif choice == '2':
            handle_color_fun_facts()
        
        elif choice == '3':
            print("Thank you for using the Color Analysis System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_interface()
