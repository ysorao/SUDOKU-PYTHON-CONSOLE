# MODULO PRINCIPAL - Asignado a Desarrollador Katherine Trochez

from sudoku_game import SudokuGame
from sudoku_display import SudokuDisplay
from sudoku_difficulty import SudokuDifficulty
from sudoku_score import SudokuScore
    
def main():

    # INICIALIZAR LAS CLASES

    display = SudokuDisplay()
    difficulty = SudokuDifficulty()
    score_manager = SudokuScore()
    
    while True:
        print("\n=== SUDOKU 4x4 ===")
        print("1. Jugar")
        print("2. Ver mejores puntajes")
        print("3. Salir")
        
        choice = input("\nSelecciona una opción: ")
        
        if choice == '3':
            if score_manager.get_current_score() > 0:
                if not score_manager.highscores or score_manager.get_current_score() > score_manager.highscores[0]['score']:
                    name = input("\n¡Nuevo récord! Ingresa tu nombre: ")
                    score_manager.add_score(name, score_manager.get_current_score())
            print("¡Gracias por jugar!")
            break
        
        elif choice == '2':
            score_manager.show_highscores()
            continue
        
        elif choice == '1':

            # SELECCIONE EL TIPO DE VISUALIZACION

            display.print_display_menu()
            display_choice = input("Opción: ")
            display_types = display.get_display_options()
            
            if display_choice not in display_types:
                print("Opción inválida")
                continue
            
            # SELECCIONE LA DIFICULTAD

            difficulty.print_difficulty_menu()
            diff_choice = input("Opción: ")
            difficulties = difficulty.get_difficulty_options()
            
            if diff_choice not in difficulties:
                print("Opción inválida")
                continue
            
            game = SudokuGame(
                display_type=display_types[display_choice],
                difficulty=difficulties[diff_choice]
            )
            
            print("\n¡Comienza el juego!")
            print("Ingresa las coordenadas y el valor (fila columna valor)")
            print("Ejemplo: 1 2 3 (fila 1, columna 2, valor 3)")
            print("Para salir, escribe 'salir'")
            
            while not game.is_complete():
                game.print_board()
                move = input("\nIngresa tu movimiento: ").strip().lower()
                
                if move == 'salir':
                    score_manager.reset_consecutive_wins()
                    break
                
                try:
                    row, col, value = move.split()
                    row = int(row) - 1
                    col = int(col) - 1
                    
                    if not (0 <= row < 4 and 0 <= col < 4):
                        print("¡Coordenadas inválidas!")
                        continue
                    
                    success, message = game.make_move(row, col, value)
                    if not success:
                        print(message)
                        
                except ValueError:
                    print("Formato inválido. Usa: fila columna valor")

            # VERIFICAR SI EL JUEGO ESTA COMPLETO
            
            if game.is_complete():
                if game.check_solution():
                    score_manager.increment_consecutive_wins()
                    points = score_manager.calculate_score()
                    score_manager.add_to_current_score(points)
                    print(f"\n¡Felicidades! Has ganado {points} puntos.")
                    print(f"Puntuación total: {score_manager.get_current_score()}")
                    print(f"Victorias consecutivas: {score_manager.consecutive_wins}")
                else:
                    print("\nLo siento, la solución no es correcta.")
                    score_manager.reset_consecutive_wins()
            else:
                score_manager.reset_consecutive_wins()
            
            print("\nSolución final:")
            game.print_board()
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main() 


