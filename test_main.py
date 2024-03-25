import unittest
import random
# import sys
# sys.path.insert(0,'C:\\Users\\kamad\\Desktop\\Python\\DEV013-guess-the-number')
from main import number_evaluation, reset_game, turn, main
from unittest import TestCase, mock
from unittest.mock import patch
from random import randint

# Variables globales 
secret_number = 50
participant_name = "Ana"
low_range = 1
high_range = 100

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=[participant_name, 50, 'N'])
    @patch('builtins.print')
    def test_main_function(self, mock_print, mock_input):
        # Llamar a la función principal
        main()

        # Verificar que se llamen a las funciones y métodos necesarios
        mock_input.assert_called_with("¿Quieres jugar de nuevo? S/N ")
        mock_print.assert_called_with("¡Gracias por participar!")

class TestNumberEvaluation(unittest.TestCase):
    @mock.patch('builtins.input', side_effect = [participant_name, secret_number])
    @mock.patch('random.randint', return_value = secret_number)
    def test_correct_guess(self, input_mock, randint_mock):
        
        #input_mock.return_value = participant_name
        # Probar la funcion
        reset_game()
        print("Number_evaluation player =", participant_name, "y guess =", secret_number)
        actual_result = number_evaluation(participant_name, secret_number)
        print("Resultado de number_evaluation:", actual_result)
        print("Secret number:", secret_number)
        #print("Guess ", guess)

        # Verificar el resultado
        expected_result = True
        print("Assertion:", actual_result, "==", expected_result)
        print("Actual Result:", actual_result)
        print("Expected Result:", expected_result)
        self.assertEqual(expected_result, actual_result)

class TestComputerTurn(unittest.TestCase):
    @patch('builtins.input', side_effect=['Computadora'])
    @patch('main.low_range', 1)  # Establecer el bajo rango
    @patch('main.high_range', 40)  # Establecer el alto rango
    @patch('main.secret_number', 50)  # Establecer el número secreto
    def test_turn(self, input_mock):
      player, guess = turn('Computadora')
      # Verificar el resultado
      expected_player = 'Computadora'
      expected_guess = 20  # El número específico de la computadora
      self.assertEqual(player, expected_player)
      self.assertEqual(guess, expected_guess)

if __name__ == '__main__':
  print("Linea 66")
  unittest.main()




