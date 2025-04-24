# MODULO PARA LA PUNTUACION DEL JUEGO - Asignado a Desarrollador Yovany Sora Olaya
import json
from datetime import datetime

class SudokuScore:
    def __init__(self):
        self.scores_file = 'highscores.json'
        self.highscores = []
        self.current_score = 0
        self.consecutive_wins = 0