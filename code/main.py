# main.py
# Main script to run the color analysis system

import sys
import user_interface as ui


def print_usage():
    """Print usage information."""
    print("Usage: python main.py [option]")
    print("Options:")
    print("  --help      : Display this help message")
    print("  --console   : Run the console-based interface")
    print("  --file      : Run the file-based interface")
    print("  --demo      : Run a demonstration of the system")
    print("  --test      : Run the test suite")
    print("If no option is provided, the console interface will be launched.")


def main():
    """Main function to run the color analysis system."""
    # Parse command line arguments
    ui.run_interface()

if __name__ == "__main__":
    main()
