import colorgram

NUM_OF_COLORS = 50

# Extract `NUM_OF_COLORS` colors from an image.
colors = colorgram.extract("image.jpg", NUM_OF_COLORS)

def rgb_color(color_obj):
  r = color_obj.rgb[0]
  g = color_obj.rgb[1]
  b = color_obj.rgb[2]
  return (r, g, b)

list_rbg_colors = [rgb_color(color) for color in colors]