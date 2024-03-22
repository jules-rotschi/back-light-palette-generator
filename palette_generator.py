from conversion_modules import hex_to_rgb
from conversion_modules import rgb_to_hsl_hsp
from conversion_modules import hsp_to_hsl
from conversion_modules import hsl_to_rgb
from conversion_modules import rgb_to_hex

gray_100_input = input('Gray-100 value: ')
gray_200_input = input('Gray-200 value: ')
gray_300_input = input('Gray-300 value: ')
gray_400_input = input('Gray-400 value: ')
gray_500_input = input('Gray-500 value: ')
gray_600_input = input('Gray-600 value: ')
gray_700_input = input('Gray-700 value: ')
gray_800_input = input('Gray-800 value: ')
gray_900_input = input('Gray-900 value: ')

base_color_hex = input('Base color (hex): ')

if base_color_hex[0] == '#':
  base_color_hex = base_color_hex[1::]

color_name = input('Color name: ')

use_base_color_input = input('Insert base color in palette ? (enter/n)')

if use_base_color_input == 'n':
  use_base_color = False
else:
  use_base_color = True

shades_of_gray = (
  int(gray_100_input),
  int(gray_200_input),
  int(gray_300_input),
  int(gray_400_input),
  int(gray_500_input),
  int(gray_600_input),
  int(gray_700_input),
  int(gray_800_input),
  int(gray_900_input)
)

color_rgb = hex_to_rgb.hex_to_rgb(base_color_hex)
color_hslp = rgb_to_hsl_hsp.rgb_to_hslp(color_rgb)
color_hsp = color_hslp[0], color_hslp[1], color_hslp[3]

def get_deltas():

  deltas = []

  for shade in shades_of_gray:
    delta = abs(shade - color_hsp[2])
    deltas.append(delta)

  return tuple(deltas)

def get_nearest_gray_index():
  
  light_grays_deltas = (get_deltas()[::-1])[4::]
  dark_grays_deltas = get_deltas()[4::]

  nearest_gray_delta = min(min(light_grays_deltas), min(dark_grays_deltas))

  if (nearest_gray_delta in light_grays_deltas) and (nearest_gray_delta in dark_grays_deltas):
    return 4
  
  if (nearest_gray_delta in light_grays_deltas):
    index = light_grays_deltas.index((min(light_grays_deltas)))
    return -index + 4

  if (nearest_gray_delta in dark_grays_deltas):
    index = dark_grays_deltas.index((min(dark_grays_deltas)))
    return index + 4

def get_colors():

  colors = []
  
  if use_base_color:
    for shade in shades_of_gray:
      if shades_of_gray.index(shade) == get_nearest_gray_index():
        colors.append(base_color_hex)
      else:
        new_color_hsp = color_hsp[0], color_hsp[1], shade
        new_color_hsl = hsp_to_hsl.hsp_to_hsl(new_color_hsp)
        new_color_rgb = hsl_to_rgb.hsl_to_rgb(new_color_hsl)
        new_color_hex = rgb_to_hex.rgb_to_hex(new_color_rgb)
        colors.append(new_color_hex)

  else:
    for shade in shades_of_gray:
      new_color_hsp = color_hsp[0], color_hsp[1], shade
      new_color_hsl = hsp_to_hsl.hsp_to_hsl(new_color_hsp)
      new_color_rgb = hsl_to_rgb.hsl_to_rgb(new_color_hsl)
      new_color_hex = rgb_to_hex.rgb_to_hex(new_color_rgb)
      colors.append(new_color_hex)

  return tuple(colors)

color_100 = get_colors()[0]
color_200 = get_colors()[1]
color_300 = get_colors()[2]
color_400 = get_colors()[3]
color_500 = get_colors()[4]
color_600 = get_colors()[5]
color_700 = get_colors()[6]
color_800 = get_colors()[7]
color_900 = get_colors()[8]

palette = (
  color_100,
  color_200,
  color_300,
  color_400,
  color_500,
  color_600,
  color_700,
  color_800,
  color_900
)

for color in palette:
  print('bl-prim-color-' + color_name + '-' + str((palette.index(color) + 1) * 100) + ' = ' + '#' + color, end='\n')