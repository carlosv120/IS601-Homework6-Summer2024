import sys
import os

# Fixing while debugging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()
