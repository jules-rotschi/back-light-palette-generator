def hsp_to_hsl(inputs):

  hue_input = inputs[0]
  saturation_input = inputs[1]
  perceptual_brightness_input = inputs[2]

  hue = int(hue_input) / 60
  saturation = int(saturation_input) / 100
  perceptual_brightness = int(perceptual_brightness_input) / 100
    
  def get_red():
    if hue <= 1:
      return 1
    elif hue <= 2:
      return (-1 / 1) * (hue - 1) + 1
    elif hue <= 4:
      return 0
    elif hue <= 5:
      return (1 / 1) * (hue - 4)
    else:
      return 1

  def get_green():
    if hue <= 1:
      return (1 / 1) * hue
    elif hue <= 3:
      return 1
    elif hue <= 4:
      return (-1 / 1) * (hue - 3) + 1
    else:
      return 0
    
  def get_blue():
    if hue <= 2:
      return 0
    elif hue <= 3:
      return (1 / 1) * (hue - 2)
    elif hue <= 5:
      return 1
    else:
      return (-1 / 1) * (hue - 5) + 1

  hue_perceptual_brightness = 0.299 * get_red() + 0.587 * get_green() + 0.114 * get_blue()

  color_perceptual_brightness = (hue_perceptual_brightness - 0.5) * saturation + 0.5

  def get_lightness():
    if perceptual_brightness <= color_perceptual_brightness:
      return (0.5 / color_perceptual_brightness) * perceptual_brightness
    else:
      x = (perceptual_brightness - color_perceptual_brightness) / (1 - color_perceptual_brightness)
      b = 0.5
      return x + b - b * x
  
  hue = hue * 60
  saturation = saturation * 100
  lightness = get_lightness() * 100

  return hue, saturation, lightness