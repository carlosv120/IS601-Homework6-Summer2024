import os
import pkgutil
import importlib
import sys
from calculator.commands import CommandHandler, Command
from calculator.plugins.Menu import MenuCommand
from dotenv import load_dotenv
import logging
import logging.config


class Calculator:
    def __init__(self): 
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)



    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'calculator.plugins'
        plugins_path = plugins_package.replace('.', '/')

        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except TypeError as te:
                    logging.error(f"Error importing plugin {plugin_name}:{te}")


    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name.lower(), item())
                self.plugins.append(plugin_name)
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")


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