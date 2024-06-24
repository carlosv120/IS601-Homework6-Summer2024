'''Testing Addition'''
from calculator.plugins.Addition import AdditionCommand

def test_add_success(capfd):
    """Test the addition command with valid inputs."""
    command = AdditionCommand()
    command.execute('2', '3')
    out = capfd.readouterr().out
    assert out.strip() == "The result of adding 2 and 3 is: 5"

def test_add_invalid_number(capfd):
    """Test the addition command with one valid and one invalid input."""
    command = AdditionCommand()
    command.execute('1.1', 'abc')
    out = capfd.readouterr().out
    assert out.strip() == "Invalid number input: 1.1 or abc is not a valid number. You are in the main menu."

def test_add_user_input_prompts(monkeypatch, capfd):
    """Test the addition command prompts for user input when num1 and num2 are None."""
    inputs = iter(['4', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AdditionCommand()
    command.execute()
    out = capfd.readouterr().out
    assert out.strip() == "The result of adding 4 and 5 is: 9"

def test_add_generic_exception(capfd):
    """Test the addition command with a forced generic exception."""
    command = AdditionCommand()
    command.execute('2', '3', raise_exception=True)
    out = capfd.readouterr().out
    assert "An error occurred: Forced exception for testing" in out.strip()
    