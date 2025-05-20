# Run the test suite for the color analysis system
import unittest
import test_color_analysis

# Create a test suite
suite = unittest.TestLoader().loadTestsFromModule(test_color_analysis)

# Run the tests
result = unittest.TextTestRunner(verbosity=2).run(suite)

print(f"\nTest Summary:")
print(f"Ran {result.testsRun} tests")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")
print(f"Skipped: {len(result.skipped)}")

# Print test results
if result.wasSuccessful():
    print("\nAll tests passed successfully!")
else:
    print("\nSome tests failed. See details above.")

# Run a demo of the system
print("\n\nRunning a demo of the Color Analysis System:")
print("===========================================")

import color_analysis as ca
ca.main()