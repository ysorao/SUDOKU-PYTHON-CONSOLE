# MODULO PARA LA PUNTUACION DEL JUEGO - Asignado a Desarrollador Yovany Sora Olaya
import json
import os
from datetime import datetime

class SudokuScore:
    def __init__(self):
        self.scores_file = 'highscores.json'
        self.highscores = self.load_highscores()
        self.current_score = 0
        self.consecutive_wins = 0
    # CARGAR LOS PUNTAJES
    def load_highscores(self):
        try:
            if os.path.exists(self.scores_file):
                with open(self.scores_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al cargar los puntajes. Se creará un nuevo archivo.")
        return []
    # GUARDAR LOS PUNTAJES
    def save_highscores(self):
        try:
            with open(self.scores_file, 'w', encoding='utf-8') as f:
                json.dump(self.highscores, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar los puntajes: {e}")
    # AGREGAR UN PUNTAJE
    def add_score(self, name, score):
        if not name.strip():
            name = "Anónimo"
            
        self.highscores.append({
            'name': name,
            'score': score,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        self.highscores.sort(key=lambda x: x['score'], reverse=True)
        self.highscores = self.highscores[:10]  # Keep only top 10
        self.save_highscores()
    # CALCULAR LA PUNTUACION
    def calculate_score(self):
        base_score = 10
        if self.consecutive_wins > 0:
            bonus = 2 ** (self.consecutive_wins - 1)
            return base_score + bonus
        return base_score
    # MOSTRAR LOS PUNTAJES
    def show_highscores(self):
        print("\n=== MEJORES PUNTAJES ===")
        if not self.highscores:
            print("No hay puntajes registrados")
            return
        # MOSTRAR LOS PUNTAJES  
        for i, score in enumerate(self.highscores, 1):
            print(f"{i}. {score['name']}: {score['score']} puntos ({score['date']})")
    # RESETEAR LAS VECES CONSECUTIVAS
    def reset_consecutive_wins(self):
        self.consecutive_wins = 0
    # INCREMENTAR LAS VECES CONSECUTIVAS
    def increment_consecutive_wins(self):
        self.consecutive_wins += 1
    # OBTENER LA PUNTUACION ACTUAL
    def get_current_score(self):
        return self.current_score
    # AGREGAR PUNTAJE A LA PUNTUACION ACTUAL
    def add_to_current_score(self, points):
        self.current_score += points 
