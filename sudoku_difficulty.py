# MODULO PARA LA DIFICULTAD DEL JUEGO - Asignado a Desarrollador Flor Alba Tovar
class SudokuDifficulty:
    def __init__(self, difficulty='facil'):
        self.difficulty = difficulty

    def get_difficulty_options(self):
        return {
            '1': 'facil',
            '2': 'dificil'
        }