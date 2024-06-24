import sys
from calculator.commands import Command

class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")