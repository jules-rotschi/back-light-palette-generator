from modules.conversion import hex_to_rgb
from modules.conversion import rgb_to_hsl_hsp

hex_to_rgb = hex_to_rgb.hex_to_rgb
rgb_to_hslp = rgb_to_hsl_hsp.rgb_to_hslp

def get_brightness(base_color_hex) :

  if base_color_hex[0] == '#':
    base_color_hex = base_color_hex[1::]

  color_rgb = hex_to_rgb(base_color_hex)
  color_hslp = rgb_to_hslp(color_rgb)

  return color_hslp[3]