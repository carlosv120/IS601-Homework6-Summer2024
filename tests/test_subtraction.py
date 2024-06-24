'''Testing Subtraction'''
from calculator.plugins.Subtraction import SubtractionCommand

def test_subtract_success(capfd):
    """Test the subtraction command with valid inputs."""
    command = SubtractionCommand()
    command.execute('5', '3')
    out = capfd.readouterr().out
    assert out.strip() == "The result of subtracting 3 from 5 is: 2"

def test_subtract_invalid_number(capfd):
    """Test the subtraction command with one valid and one invalid input."""
    command = SubtractionCommand()
    command.execute('1.1', 'abc')
    out = capfd.readouterr().out
    assert out.strip() == "Invalid number input: 1.1 or abc is not a valid number. You are in the main menu."

def test_subtract_user_input_prompts(monkeypatch, capfd):
    """Test the subtraction command prompts for user input when num1 and num2 are None."""
    inputs = iter(['4', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractionCommand()
    command.execute()
    out = capfd.readouterr().out
    assert out.strip() == "The result of subtracting 2 from 4 is: 2"

def test_subtract_generic_exception(capfd):
    """Test the subtraction command with a forced generic exception."""
    command = SubtractionCommand()
    command.execute('2', '3', raise_exception=True)
    out = capfd.readouterr().out
    assert "An error occurred: Forced exception for testing" in out.strip()
    