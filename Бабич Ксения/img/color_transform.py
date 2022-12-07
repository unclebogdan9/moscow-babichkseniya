def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"
