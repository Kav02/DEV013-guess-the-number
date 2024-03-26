# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103
# pylint: disable=unused-argument
import unittest
# import sys
# sys.path.insert(0,'C:\\Users\\kamad\\Desktop\\Python\\DEV013-guess-the-number')
#from random import randint
from unittest.mock import patch
from io import StringIO
from main import number_evaluation, reset_game, turn, main


# Variables globales
secret_number = 50
participant_name = "Ana"
low_range = 1
high_range = 100

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect = [participant_name, "n"])
    @patch('main.turn', return_value=(participant_name, True))  #Devuelve exito
    @patch('main.number_evaluation', return_value=True)
    def test_main_function_play_again(self, mock_input, mock_turn, mock_number_evaluation):

        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            main()

        # Verifica la salida esperada en la consola
        expected_output = "¡Gracias por participar!\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


class TestNumberEvaluation(unittest.TestCase):
    @patch('builtins.input', side_effect = [participant_name, secret_number])
    @patch('random.randint', return_value = secret_number)
    def test_correct_guess(self, input_mock, randint_mock):
        # Probar la funcion
        reset_game()
        actual_result = number_evaluation(participant_name, secret_number)
        # Verificar el resultado
        expected_result = True
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect = [participant_name, secret_number])
    @patch('random.randint', return_value = secret_number)
    def test_high_guess(self, input_mock, randint_mock):
        # Probar la funcion
        reset_game()
        actual_result = number_evaluation(participant_name, 80)
        # Verificar el resultado
        expected_result = False
        self.assertEqual(expected_result, actual_result)


class TestComputerTurn(unittest.TestCase):
    @patch('builtins.input', side_effect=['Computadora'])
    @patch('main.low_range', 1)  # Establecer el bajo rango
    @patch('main.high_range', 40)  # Establecer el alto rango
    @patch('main.secret_number', 25)  # Establecer el número secreto
    def test_turn(self, input_mock):
        player, guess = turn('Computadora')
        # Verificar el resultado
        expected_player = 'Computadora'
        expected_guess = 20  # El número específico de la computadora
        self.assertEqual(player, expected_player)
        self.assertEqual(guess, expected_guess)

if __name__ == '__main__':
    unittest.main()
