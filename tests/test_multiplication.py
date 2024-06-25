'''Testing Multiplication'''
from calculator.plugins.Multiplication import MultiplicationCommand

def test_multiply_success(capfd):
    """Test the multiplication command with valid inputs."""
    command = MultiplicationCommand()
    command.execute('2', '3')
    out = capfd.readouterr().out
    assert out.strip() == "The result of multiplying 2 and 3 is: 6"

def test_multiply_invalid_number(capfd):
    """Test the multiplication command with one valid and one invalid input."""
    command = MultiplicationCommand()
    command.execute('1.2', 'abc')
    out = capfd.readouterr().out
    assert out.strip() == "Invalid number input: 1.2 and/or abc is not a valid number. You are in the main menu."

def test_multiply_user_input_prompts(monkeypatch, capfd):
    """Test the multiplication command prompts for user input when num1 and num2 are None."""
    inputs = iter(['4', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplicationCommand()
    command.execute()
    out = capfd.readouterr().out
    assert out.strip() == "The result of multiplying 4 and 2 is: 8"

def test_multiply_generic_exception(capfd):
    """Test the multiplication command with a forced generic exception."""
    command = MultiplicationCommand()
    command.execute('2', '3', raise_exception=True)
    out = capfd.readouterr().out
    assert "An error occurred: Forced exception for testing" in out.strip()
    