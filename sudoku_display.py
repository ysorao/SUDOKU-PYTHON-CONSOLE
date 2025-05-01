# MODULO PARA LA VISUALIZACION DEL JUEGO
class SudokuDisplay:
    def __init__(self, display_type='numerico'):
        self.display_type = display_type
        self.symbols = ['♣', '♦', '♥', '♠']

    # CONVERTIENDO EL NUMERO A LA VISUALIZACION SELECCIONADA
    def convert_to_display(self, num):
        if num == 0:
            return " "
        if self.display_type == 'numerico':
            return str(num)
        elif self.display_type == 'letras':
            return chr(64 + num)  # A=65, B=66, etc.
        else:  # simbolos
            return self.symbols[num-1]

    # CONVERTIENDO LA VISUALIZACION SELECCIONADA A UN NUMERO
    def convert_from_display(self, value):
        if self.display_type == 'numerico':
            return int(value)
        elif self.display_type == 'letras':
            return ord(value.upper()) - 64  # A=1, B=2, etc.
        else:  # simbolos
            return self.symbols.index(value) + 1

    # OBTENER LAS OPCIONES DE VISUALIZACION
    def get_display_options(self):
        return {
            '1': 'numerico',
            '2': 'letras',
            '3': 'simbolos'
        }

    # IMPRIMIR EL MENU DE VISUALIZACION
    def print_display_menu(self):
        print("\nSelecciona el tipo de visualización:")
        print("1. Numérico (1-4)")
        print("2. Letras (A-D)")
        print("3. Símbolos (♣ ♦ ♥ ♠)")
