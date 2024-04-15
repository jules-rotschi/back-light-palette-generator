from modules.conversion import hex_to_rgb
from modules.conversion import rgb_to_hsl_hsp
from modules.conversion import hsp_to_hsl
from modules.conversion import hsl_to_rgb
from modules.conversion import rgb_to_hex

hex_to_rgb = hex_to_rgb.hex_to_rgb
rgb_to_hslp = rgb_to_hsl_hsp.rgb_to_hslp
hsp_to_hsl = hsp_to_hsl.hsp_to_hsl
hsl_to_rgb = hsl_to_rgb.hsl_to_rgb
rgb_to_hex = rgb_to_hex.rgb_to_hex

def set_brightness(base_color_hex, target_brightness) :

  if base_color_hex[0] == '#':
    base_color_hex = base_color_hex[1::]

  color_rgb = hex_to_rgb(base_color_hex)
  color_hslp = rgb_to_hslp(color_rgb)
  color_hsp = color_hslp[0], color_hslp[1], color_hslp[3]

  perceptual_brightness = int(target_brightness)

  new_color_hsp = color_hsp[0], color_hsp[1], perceptual_brightness
  new_color_hsl = hsp_to_hsl(new_color_hsp)
  new_color_rgb = hsl_to_rgb(new_color_hsl)
  new_color_hex = rgb_to_hex(new_color_rgb)

  return new_color_hex