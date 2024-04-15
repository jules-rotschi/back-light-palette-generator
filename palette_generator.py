from config.shades_of_gray import shades_of_gray

from modules.generate_palette import generate_palette

from modules.set_brightness import set_brightness

from modules.get_opacities import get_opacities

base_color_hex = input('Base color (hex): ')
use_base_color_input = input('Use base color in palette ? (y/enter)')

use_base_color: bool = use_base_color_input == 'y'

palette = generate_palette(base_color_hex, use_base_color)

shades = [
  50,
  100,
  200,
  300,
  400,
  500,
  600,
  700,
  800,
  900,
  950,
]

print('\n--- COLORS ---')

for color in palette:
  print(str(shades[palette.index(color)]) + ': ' + '#' + color, end='\n')

opacities = get_opacities(base_color_hex)

print('\n--- OPACITIES ---')

for opacity in opacities:
  print(str((opacities.index(opacity) + 1) * 20) + '% : ' + '#' + opacity, end='\n')