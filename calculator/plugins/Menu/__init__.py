from calculator.commands import Command

class MenuCommand(Command):
    def __init__(self, plugins):
        self.plugins = plugins

    def execute(self):
        print("Loaded plugins:", "\t\t".join(self.plugins))