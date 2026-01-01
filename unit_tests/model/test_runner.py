import pytest
import sys
import os

if __name__ == "__main__":
    # Run pytest on the current directory
    sys.exit(pytest.main([os.path.dirname(__file__)]))
