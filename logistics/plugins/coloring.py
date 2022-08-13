# dependencies.
from logistics.plugins.types import *
from colorama import (
    Fore,
    Back,
    Style,
    init,
)

# initializes coloring.
init()

# paints the text with a desired color ('fr', 'fg', 'fb', 'fk', 'fc', 'fm', 'fy', 'br', 'bg', 'bb', 'bk', 'bc', 'bm', 'by').
def paint_text(
        text : StringType,
        color : StringType,
        print_trigger : BooleanType = True
        ) -> StringType:
        
        '''
        * coloring of CLI.
        
        - text - desired text to print.
        - color - desired color to print in.
        - print_trigger (True/False) - modify return type.
        '''
        
        # Fore coloring.
        colors = {
            'Fr' : Fore.RED,
            'Fg' : Fore.GREEN,
            'Fb' : Fore.BLUE,
            'Fk' : Fore.BLACK,
            'Fm' : Fore.MAGENTA,
            'Fy' : Fore.YELLOW,
            'Fc' : Fore.CYAN,
            
        # Back coloring.
            'Br' : Back.RED,
            'Bg' : Back.GREEN,
            'Bb' : Back.BLUE,
            'Bk' : Back.BLACK,
            'Bm' : Back.MAGENTA,
            'By' : Back.YELLOW,
            'Bc' : Back.CYAN,
            }
        
        if print_trigger == True:
            return print(colors[color] + str(text) + Style.RESET_ALL)
        
        elif print_trigger == False:
            return colors[color] + str(text) + Style.RESET_ALL