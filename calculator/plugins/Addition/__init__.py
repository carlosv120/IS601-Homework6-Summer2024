from decimal import Decimal, InvalidOperation
from calculator.commands import Command
import logging

class AdditionCommand(Command):
    def execute(self, num1=None, num2=None, raise_exception=False):
        try:
            if num1 is None:
                num1 = input("Enter the first number: ").strip()
                logging.info("First number entered: %s", num1)
            if num2 is None:
                num2 = input("Enter the second number: ").strip()
                logging.info("Second number entered: %s", num2)

            if raise_exception:
                raise Exception("Forced exception for testing")

            num1_decimal, num2_decimal = map(Decimal, [num1, num2])
            logging.info("Converted input to Decimal: num1_decimal=%s, num2_decimal=%s", num1_decimal, num2_decimal)

            result = num1_decimal + num2_decimal
            logging.info("Addition result: %s", result)

            print(f"The result of adding {num1_decimal} and {num2_decimal} is: {result}")

        except InvalidOperation:
            logging.error("Invalid number input: %s or %s is not a valid number", num1, num2)
            print(f"Invalid number input: {num1} and/or {num2} is not a valid number. You are in the main menu.")
        
        except Exception as e:
            logging.exception("An error occurred: %s", e)
            print(f"An error occurred: {e}")
