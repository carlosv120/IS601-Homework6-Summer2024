"""Testing the Calculator App"""

import pytest
from calculator import Calculator

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calculator = Calculator()
    with pytest.raises(SystemExit) as e:
        calculator.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator = Calculator()
    with pytest.raises(SystemExit):
        calculator.start()
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_get_environment_variable():
    """Testing getting the environment variables"""
    calculator = Calculator()
    #Retrieve the current environment setting
    current_env = calculator.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"
    