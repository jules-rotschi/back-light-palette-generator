from config.shades_of_gray import white
from config.shades_of_gray import black

from modules.conversion.hex_to_rgb import hex_to_rgb
from modules.conversion.rgb_to_hex import rgb_to_hex

class Color_shades:
  def __init__(self, base, opacity, blend_brightness):
    self.base = base
    self.opacity = opacity
    self.blend_color = blend_brightness * 2.55

  def getChannel(self, channel):
    return self.opacity * self.base[channel] + (1 - self.opacity) * self.blend_color

  def getRGB(self):
    return self.getChannel(0), self.getChannel(1), self.getChannel(2)

  def getHex(self):
    return rgb_to_hex(self.getRGB())


def get_colors(base_color_hex):

  color_rgb = hex_to_rgb(base_color_hex)

  colors = []

  color_100 = Color_shades(color_rgb, 0.2, white)
  color_200 = Color_shades(color_rgb, 0.4, white)
  color_300 = Color_shades(color_rgb, 0.6, white)
  color_400 = Color_shades(color_rgb, 0.8, white)
  color_500 = Color_shades(color_rgb, 1, black)
  color_600 = Color_shades(color_rgb, 0.8, black)
  color_700 = Color_shades(color_rgb, 0.6, black)
  color_800 = Color_shades(color_rgb, 0.4, black)
  color_900 = Color_shades(color_rgb, 0.2, black)

  shades = (
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

  for shade in shades:
    colors.append(shade.getHex())

  return tuple(colors)

def generate_palette(base_color_hex):

  if base_color_hex[0] == '#':
    base_color_hex = base_color_hex[1::]

  palette = get_colors(base_color_hex)

  return palette