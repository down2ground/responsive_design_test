import sys

def recalc_component(base, value):
    return base - base * value // 256


bg = sys.argv[1].strip()
in_color = sys.argv[2].strip()

bg_r = bg[0:2]
bg_g = bg[2:4]
bg_b = bg[5:7]

in_color_r = in_color[0:2]
in_color_g = in_color[2:4]
in_color_b = in_color[5:7]

print(hex(recalc_component(int(bg_r, 16), int(in_color_r, 16)))[2:].rjust(2, "0") +
      hex(recalc_component(int(bg_g, 16), int(in_color_g, 16)))[2:].rjust(2, "0") +
      hex(recalc_component(int(bg_b, 16), int(in_color_b, 16)))[2:].rjust(2, "0"))

