def get_opacities(base_color_hex):

  opacities = []

  hex_opacity_values = (
    hex(int(20 * 2.55)),
    hex(int(40 * 2.55)),
    hex(int(60 * 2.55)),
    hex(int(80 * 2.55))
  )

  for value in hex_opacity_values:
    opacities.append(base_color_hex + value[2::])

  return tuple(opacities)