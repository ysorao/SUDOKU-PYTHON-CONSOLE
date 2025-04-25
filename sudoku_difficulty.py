# MODULO PARA LA DIFICULTAD DEL JUEGO - Asignado a Desarrollador Flor Alba Tovar
class SudokuDifficulty:
    def __init__(self, difficulty='facil'):
        self.difficulty = difficulty

    def get_difficulty_options(self):
        return {
            '1': 'facil',
            '2': 'dificil'
        }
    
    def print_difficulty_menu(self):
        # Muestra el menú de dificultad
        pass

    def get_border(self):
        # Devuelve el tipo de borde del tablero
        pass
