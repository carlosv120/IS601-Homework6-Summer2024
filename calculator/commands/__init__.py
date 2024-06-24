from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """IF for Look before you leap (LBYL) when are error is more likely to happen most of the times"""
        """Try-Catch for Easier to ask for forgiveness than permission (EAFP) for when the error will not be common"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
            