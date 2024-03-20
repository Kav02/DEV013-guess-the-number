# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

from main import turn
def test_turn_invalid_input(self):
    participant_name = "Ana"
    guess = 150   
    turn(participant_name) 
    self.assertFalse(guess,150)
    
def test_number_evaluation():
    secret_number = 92
    