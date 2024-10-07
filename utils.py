def hex_to_rgb(hex_color):
    """Convert a hex color to an RGB tuple."""
    r = (hex_color >> 16) & 0xFF
    g = (hex_color >> 8) & 0xFF
    b = hex_color & 0xFF
    return (r, g, b)

def rgb_to_hex(rgb_color):
    """Convert an RGB tuple to a hex color."""
    return (rgb_color[0] << 16) + (rgb_color[1] << 8) + rgb_color[2]

def lerp_color(hex_color1, hex_color2, t):
    """
    Linearly interpolates between two hex colors.

    Parameters:
    - hex_color1: First hex color
    - hex_color2: Second hex color
    - t: A float between 0 and 1 representing the interpolation factor

    Returns:
    - The interpolated hex color
    """
    # Convert hex colors to RGB
    rgb_color1 = hex_to_rgb(hex_color1)
    rgb_color2 = hex_to_rgb(hex_color2)

    # Perform linear interpolation
    r = int(rgb_color1[0] + (rgb_color2[0] - rgb_color1[0]) * t)
    g = int(rgb_color1[1] + (rgb_color2[1] - rgb_color1[1]) * t)
    b = int(rgb_color1[2] + (rgb_color2[2] - rgb_color1[2]) * t)

    # Convert the interpolated RGB color back to hex
    return (r,g,b)