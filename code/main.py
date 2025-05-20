# code/main.py
import sys
import os

# 1) Project root ko path mein add karo
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

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
    print("\nRunning Black-box Tests")
    from testing import blackbox_testing
    suite_bb = unittest.TestLoader().loadTestsFromModule(blackbox_testing)
    unittest.TextTestRunner(verbosity=2).run(suite_bb)

    # White-box tests
    print("\nRunning White-box Tests")
    from testing import whitebox_testing
    suite_wb = unittest.TestLoader().loadTestsFromModule(whitebox_testing)
    unittest.TextTestRunner(verbosity=2).run(suite_wb)

    # Summary & demo
    print("\nRunning Combined Test Summary and Demo")
    import testing.run_tests
    # importing run_tests triggers its execution (it prints summary + demo)

def main():
    if len(sys.argv) > 1:
        opt = sys.argv[1].lower()
        if opt == "--help":
            print_usage()
        elif opt == "--console":
            ui.run_interface()
        elif opt == "--file":
            fi.run_file_interface()
        elif opt == "--demo":
            ca.main()
        elif opt == "--test":
            run_all_tests()
        else:
            print(f"Unknown option: {opt}")
            print_usage()
    else:
        ui.run_interface()

if __name__ == "__main__":
    main()
