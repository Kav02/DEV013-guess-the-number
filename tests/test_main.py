import pytest
import unittest
import sys
sys.path.insert(0,'C:\\Users\\kamad\\Desktop\\Python\\DEV013-guess-the-number')
from main import number_evaluation


# Variables globales para simular el estado del juego 
secret_number = 50
participant_name = "Ana"

class TestNumberEvaluation(unittest.TestCase):

  def test_correct_guess(self):
    player = participant_name
    guess = secret_number
    expected_result = True

    actual_result = number_evaluation(player, guess)

    self.assertEqual(expected_result, actual_result)

  def test_high_guess(self):
    player = participant_name
    guess = secret_number + 10
    expected_result = False

    actual_result = number_evaluation(player, guess)

    self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
  unittest.number_evaluation()




# import unittest
# from unittest import mock
# # import sys
# # sys.path.insert(0,'C:\\Users\\kamad\\Desktop\\Python\\DEV013-guess-the-number')
# #from main import turn, number_evaluation
# import main

# secret_number = 50
# attempts = 2
# participant_guess = [40, 55]
# participant_name = "Ana"
# low_range = 1
# high_range = 100


# def test_turn_with_valid_input():
#   # Simular la entrada del usuario
#      with mock.patch('builtins.input', side_effect=["50"]):
#         actual_player, actual_guess = main.turn(participant_name)

#   # Verificar el resultado
#         expected_player = "Ana"
#         expected_guess = 50
#         assert actual_guess == expected_guess
#         assert actual_player == expected_player

# def test_correct_guess():
#     expected_result = True
#     actual_result = main.number_evaluation(participant_name, secret_number)
#     assert expected_result == actual_result
    
# if __name__ == '__main__':
#     test_correct_guess()
#     test_turn_with_valid_input()  