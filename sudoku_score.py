# MODULO PARA LA PUNTUACION DEL JUEGO - Asignado a Desarrollador Yovany Sora Olaya
import json
from datetime import datetime

class SudokuScore:
    def __init__(self):
        self.scores_file = 'highscores.json'
        self.highscores = []
        self.current_score = 0
        self.consecutive_wins = 0
    
    def load_highscores(self):
        # Cargar puntajes desde archivo JSON
        pass

    def save_highscores(self):
        # Guardar puntajes en archivo JSON
        pass

    def add_score(self, name, score):
        # Agregar un nuevo puntaje
        pass

    def calculate_score(self):
        # Calcular la puntuación con bonus
        pass

    def show_highscores(self):
        # Mostrar los mejores puntajes
        pass

    def reset_consecutive_wins(self):
        # Reiniciar el contador de victorias
        pass

    def increment_consecutive_wins(self):
        # Aumentar victorias consecutivas
        pass

    def get_current_score(self):
        # Obtener puntuación actual
        pass

    def add_to_current_score(self, points):
        # Sumar puntos al score actual
        pass
