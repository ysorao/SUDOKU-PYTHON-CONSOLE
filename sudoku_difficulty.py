# MODULO PARA LA DIFICULTAD DEL JUEGO - Asignado a Desarrollador Flor Alba Tovar

class SudokuDifficulty:
    def __init__(self, difficulty='facil'):
        self.difficulty = difficulty
        self.cells_to_remove = 6 if difficulty == 'facil' else 10

    def get_difficulty_options(self):
        return {
            '1': 'facil',
            '2': 'dificil'
        }

    def print_difficulty_menu(self):
        print("\nSelecciona el nivel de dificultad:")
        print("1. Fácil (6 casillas vacías)")
        print("2. Difícil (10 casillas vacías)")

    def get_border(self):
        return '*' if self.difficulty == 'facil' else '-'

    def get_cells_to_remove(self):
        return self.cells_to_remove 
