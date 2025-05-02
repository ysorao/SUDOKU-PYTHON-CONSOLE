# MODULO PARA LA LOGICA DEL JUEGO SUDOKU - Asignado a Desarrollador Yovany Sora Olaya
import random
from sudoku_display import SudokuDisplay
from sudoku_difficulty import SudokuDifficulty

# MODULO PARA EL JUEGO DE SUDOKU
class SudokuGame:
    def __init__(self, display_type='numerico', difficulty='facil'):
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        self.solution = [[0 for _ in range(4)] for _ in range(4)]
        self.display = SudokuDisplay(display_type)
        self.difficulty = SudokuDifficulty(difficulty)
        self.generate_puzzle()

    def is_valid(self, row, col, num):
        # VERIFICAR SI EL NUMERO ES VALIDO EN LA FILA
        if num in self.board[row]:
            return False
        
        # VERIFICAR SI EL NUMERO ES VALIDO EN LA COLUMNA
        for i in range(4):
            if self.board[i][col] == num:
                return False
        
        # VERIFICAR SI EL NUMERO ES VALIDO EN EL CUADRO 2X2
        box_row = (row // 2) * 2
        box_col = (col // 2) * 2
        for i in range(2):
            for j in range(2):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        
        return True

    def solve(self):
        # RESOLVER EL TABLERO
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    for num in range(1, 5):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def generate_puzzle(self):
        # GENERAR UN TABLERO RESUELTO
        self.solve()
        self.solution = [row[:] for row in self.board]
        
        # REMOVER NUMEROS BASADO EN LA DIFICULTAD
        positions = [(i, j) for i in range(4) for j in range(4)]
        random.shuffle(positions)
        
        for i, j in positions[:self.difficulty.get_cells_to_remove()]:
            self.board[i][j] = 0

    def print_board(self):
        # IMPRIMIR EL TABLERO
        border = self.difficulty.get_border()
        print(f"\n  1 2 3 4")
        print(f" {border*9}")
        for i in range(4):
            print(f"{i+1}{border}", end="")
            for j in range(4):
                print(f"{self.display.convert_to_display(self.board[i][j])}", end=" ")
            print(f"{border}")
        print(f" {border*9}")

    def is_complete(self):
        # VERIFICAR SI EL TABLERO ESTA COMPLETO
        return all(0 not in row for row in self.board)

    def check_solution(self):
        # VERIFICAR SI LA SOLUCION ES CORRECTA
        return self.board == self.solution

    def make_move(self, row, col, value):
        # HACER UN MOVIMIENTO   
        try:
            num = self.display.convert_from_display(value)
            if not (1 <= num <= 4):
                return False, "¡Valor inválido!"
            
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                return True, "Movimiento válido"
            else:
                return False, "¡Movimiento inválido!"
                
        except (ValueError, IndexError):
            return False, "¡Valor inválido!" 
