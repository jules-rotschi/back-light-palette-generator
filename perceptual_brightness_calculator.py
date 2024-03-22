from conversion_modules import hex_to_rgb
from conversion_modules import rgb_to_hsl_hsp

base_color_hex = input('Color (hex): ')

if base_color_hex[0] == '#':
  base_color_hex = base_color_hex[1::]

color_rgb = hex_to_rgb.hex_to_rgb(base_color_hex)
color_hslp = rgb_to_hsl_hsp.rgb_to_hslp(color_rgb)

print('Perceptual brightness: ' + str(round(color_hslp[3], 0)))