from config.shades_of_gray import shades_of_gray

from modules.set_brightness import set_brightness
from modules.get_brightness import get_brightness

def get_deltas(base_color_brightness):

  deltas = []

  for shade in shades_of_gray:
    delta = abs(shade - base_color_brightness)
    deltas.append(delta)

  return tuple(deltas)


def get_nearest_gray_index(base_color_brightness):
    
  light_grays_deltas = (get_deltas(base_color_brightness)[::-1])[4::]
  dark_grays_deltas = get_deltas(base_color_brightness)[4::]

  nearest_gray_delta = min(min(light_grays_deltas), min(dark_grays_deltas))

  if (nearest_gray_delta in light_grays_deltas) and (nearest_gray_delta in dark_grays_deltas):
    return 4
  
  if (nearest_gray_delta in light_grays_deltas):
    index = light_grays_deltas.index((min(light_grays_deltas)))
    return -index + 4

  if (nearest_gray_delta in dark_grays_deltas):
    index = dark_grays_deltas.index((min(dark_grays_deltas)))
    return index + 4
    

def get_colors(base_color_hex):

  base_color_brightness = get_brightness(base_color_hex)

  colors = []
  
  for shade in shades_of_gray:
    if shades_of_gray.index(shade) == get_nearest_gray_index(base_color_brightness):
      colors.append(base_color_hex)
    else:
      new_color_hex = set_brightness(base_color_hex, shade)
      colors.append(new_color_hex)

  return tuple(colors)


def generate_palette_strict(base_color_hex) :

  if base_color_hex[0] == '#':
    base_color_hex = base_color_hex[1::]

  palette = get_colors(base_color_hex)

  return palette