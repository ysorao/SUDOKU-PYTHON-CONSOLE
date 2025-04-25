# MODULO PARA LA VISUALIZACION DEL JUEGO - Asignado a Desarrollador Geraldyne Paola Palacio
class SudokuDisplay:
    def __init__(self, display_type='numerico'):
        self.display_type = display_type
        self.symbols = ['♣', '♦', '♥', '♠']
    
    def convert_to_display(self, num):
        # Convierte número a su representación visual
        pass

    def convert_from_display(self, value):
        # Convierte visualización a número
        pass

    def get_display_options(self):
        # Opciones de visualización disponibles
        return {
            '1': 'numerico',
            '2': 'letras',
            '3': 'simbolos'
        }
    
    def print_display_menu(self):
        # Menú visual para seleccionar tipo de display
        pass
