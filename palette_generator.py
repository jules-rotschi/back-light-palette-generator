from config.shades_of_gray import shades_of_gray

from modules.generate_palette_strict import generate_palette_strict
from modules.generate_palette import generate_palette

from modules.set_brightness import set_brightness

from modules.get_opacities import get_opacities

base_color_hex = input('Base color (hex): ')
use_base_color = input('Enter \'y\' if yo want to activate strict color mode (else, press enter)')

if use_base_color == 'yes':
  strict_mode = True

if use_base_color == '':
  strict_mode = False

if strict_mode:
  palette = generate_palette_strict(base_color_hex)
else:
  base_color_hex = set_brightness(base_color_hex, shades_of_gray[4])
  palette = generate_palette(base_color_hex)

for color in palette:
  print(str((palette.index(color) + 1) * 100) + ': ' + '#' + color, end='\n')

opacities = get_opacities(base_color_hex)

for opacity in opacities:
  print(str((opacities.index(opacity) + 1) * 20) + '% : ' + '#' + opacity, end='\n')