from decimal import Decimal, InvalidOperation
from calculator.commands import Command

class MultiplicationCommand(Command):
    def execute(self, num1=None, num2=None, raise_exception=False):
        try:
            if num1 is None:
                num1 = input("Enter the first number: ").strip()
            if num2 is None:
                num2 = input("Enter the second number: ").strip()

            if raise_exception:
                raise Exception("Forced exception for testing")

            num1_decimal, num2_decimal = map(Decimal, [num1, num2])

            result = num1_decimal * num2_decimal

            print(f"The result of multiplying {num1_decimal} and {num2_decimal} is: {result}")

        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number. You are in the main menu.")
        
        except Exception as e:
            print(f"An error occurred: {e}")