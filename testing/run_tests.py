# code/main.py
# code/color_analysis.py
# code/file_interface.py
# Main script to run the color analysis system

import sys
import color_analysis as ca
import user_interface as ui
import file_interface as fi

def print_usage():
    """Print usage information."""
    print("Usage: python main.py [option]")
    print("Options:")
    print("  --help      : Display this help message")
    print("  --console   : Run the console-based interface")
    print("  --file      : Run the file-based interface")
    print("  --demo      : Run a demonstration of the system")
    print("  --test      : Run all test suites (black-box, white-box, summary)")
    print("If no option is provided, the console interface will be launched.")

def run_all_tests():
    """Run black-box, white-box, and summary tests."""
    import unittest

    # Black-box tests
    print("Running Black-box Tests")
    print("==========================")
    try:
        from testing import blackbox_testing
    except ImportError:
        print("Error: could not import blackbox_testing")
    else:
        suite_bb = unittest.TestLoader().loadTestsFromModule(blackbox_testing)
        unittest.TextTestRunner(verbosity=2).run(suite_bb)

    # White-box tests
    print("\nRunning White-box Tests")
    print("===========================")
    try:
        from testing import whitebox_testing
    except ImportError:
        print("Error: could not import whitebox_testiing")
    else:
        suite_wb = unittest.TestLoader().loadTestsFromModule(whitebox_testing)
        unittest.TextTestRunner(verbosity=2).run(suite_wb)

    # Summary & demo
    print("\nTesting ")
    print("========================================")
    try:
        from testing import run_tests
        # run_tests.py will execute its suite and print summary + demo
        # It has its own __main__ guard
        run_tests.main()
    except AttributeError:
        # If run_tests has no main(), just import to execute
        pass
    except ImportError:
        print("Error: could not import run_tests")

def main():
    """Main function to run the color analysis system."""
    if len(sys.argv) > 1:
        option = sys.argv[1].lower()
        
        if option == "--help":
            print_usage()
        elif option == "--console":
            ui.run_interface()
        elif option == "--file":
            fi.run_file_interface()
        elif option == "--demo":
            ca.main()
        elif option == "--test":
            run_all_tests()
        else:
            print(f"Unknown option: {option}")
            print_usage()
    else:
        # Default to console interface
        ui.run_interface()

if __name__ == "__main__":
    main()
