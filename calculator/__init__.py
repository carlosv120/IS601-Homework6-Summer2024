import pkgutil
import importlib
from calculator.commands import CommandHandler, Command
from calculator.plugins.Menu import MenuCommand

class Calculator:
    def __init__(self): 
        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'calculator.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name.lower(), item())
                            self.plugins.append(plugin_name)  # Add the plugin name to the list
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Load plugins
        self.load_plugins()
        
        # Add the Menu plugin to the list and register the menu command
        self.plugins.append("Menu")  
        self.command_handler.register_command("menu", MenuCommand(self.plugins))

        # Print available plugins
        self.command_handler.execute_command("menu")

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().lower()
            self.command_handler.execute_command(user_input)