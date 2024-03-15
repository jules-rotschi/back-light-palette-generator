import hex_to_rgb
import rgb_to_hsl_hsp
import hsp_to_hsl
import hsl_to_rgb
import rgb_to_hex

base_color_hex = input('Base color (hex): ')

if base_color_hex[0] == '#':
  base_color_hex = base_color_hex[1::]

target_perceptual_brightness = input('Target perceptual brightness: ')

color_rgb = hex_to_rgb.hex_to_rgb(base_color_hex)
color_hslp = rgb_to_hsl_hsp.rgb_to_hslp(color_rgb)
color_hsp = color_hslp[0], color_hslp[1], color_hslp[3]

perceptual_brightness = int(target_perceptual_brightness)

new_color_hsp = color_hsp[0], color_hsp[1], perceptual_brightness
new_color_hsl = hsp_to_hsl.hsp_to_hsl(new_color_hsp)
new_color_rgb = hsl_to_rgb.hsl_to_rgb(new_color_hsl)
new_color_hex = rgb_to_hex.rgb_to_hex(new_color_rgb)

print('Corrected color: ' + '#' + new_color_hex)