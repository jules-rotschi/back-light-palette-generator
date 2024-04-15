from modules.set_brightness import set_brightness
from config.shades_of_gray import shades_of_gray

base_color_hex = input('Base color (hex): ')
shade_input = input('Shade: ')
shade = int(shade_input)

def get_target_brightness(shade):
  if shade == 50:
    return shades_of_gray[0]
  if shade == 100:
    return shades_of_gray[1]
  if shade == 200:
    return shades_of_gray[2]
  if shade == 300:
    return shades_of_gray[3]
  if shade == 400:
    return shades_of_gray[4]
  if shade == 500:
    return shades_of_gray[5]
  if shade == 600:
    return shades_of_gray[6]
  if shade == 700:
    return shades_of_gray[7]
  if shade == 800:
    return shades_of_gray[8]
  if shade == 900:
    return shades_of_gray[9]
  if shade == 950:
    return shades_of_gray[10]
  
new_color = set_brightness(base_color_hex, get_target_brightness(shade))

print('Corrected color: ' + '#' + new_color)