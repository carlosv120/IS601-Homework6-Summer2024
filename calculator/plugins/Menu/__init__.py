import logging
from calculator.commands import Command

class MenuCommand(Command):
    def __init__(self, plugins):
        self.plugins = plugins
        logging.info("MenuCommand initialized with plugins: %s", plugins)

    def execute(self):
        print("Loaded plugins:", "\t\t".join(self.plugins))
        logging.info("MenuCommand executed successfully")