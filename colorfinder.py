#! /usr/bin/python3
# /***************************************************************************
#  *   colorfinder.py                                                        *
#  *                                                                         *
#  *   Copyright (C) 2023-2024 by Jan Dolstra                                *
#  *   dev@jandnet.nl                                                        *
#  *                                                                         *
#  *   This program is free software; you can redistribute it and/or modify  *
#  *   it under the terms of the GNU General Public License as published by  *
#  *   the Free Software Foundation; either version 3 of the License, or     *
#  *   (at your option) any later version.                                   *
#  *                                                                         *
#  *   This program is distributed in the hope that it will be useful,       *
#  *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#  *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          *
#  *   GNU General Public License for more details.                          *
#  *                                                                         *
#  *   You should have received a copy of the GNU General Public License     *
#  *   along with this program; if not, write to the                         *
#  *   Free Software Foundation, Inc.,                                       *
#  *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
#  ***************************************************************************/
import math
import re

def find_nearest_colors(hex_color, color_list, top_n=3):
    """Finds the top N nearest colors in the given list to the specified hex color.

    Args:
        hex_color: The hex color to find the nearest matches for.
        color_list: A list of hex colors to search through.
        top_n: The number of nearest colors to return (default is 3).

    Returns:
        A list of tuples containing the nearest hex colors and their distances.
    """
    # Convert the hex color to RGB values
    r, g, b = hex_to_rgb(hex_color)

    # Create a list to store colors and their distances
    distances = []

    # Calculate the distance for each color in the list
    for color in color_list:
        cr, cg, cb = hex_to_rgb(color)
        distance = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        distances.append((color, distance))

    # Sort by distance and return the top N results
    distances.sort(key=lambda x: x[1])
    return distances[:top_n]

def hex_to_rgb(hex_color):
    """Converts a hex color to RGB values.

    Args:
        hex_color: The hex color to convert.

    Returns:
        A tuple of RGB values.
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = hex_color * 2
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def is_valid_hex_color(hex_color):
    """Checks if the input is a valid hex color code."""
    return bool(re.match(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$', hex_color))

# Dictionary of hex color codes and corresponding names
color_dict = {
    "aliceblue": "#F0F8FF",
    "ansi_black": "#000000",
    "ansi_blue": "#000080",
    "ansi_bright_black": "#808080",
    "ansi_bright_blue": "#0000FF",
    "ansi_bright_cyan": "#00FFFF",
    "ansi_bright_green": "#00FF00",
    "ansi_bright_magenta": "#FF00FF",
    "ansi_bright_red": "#FF0000",
    "ansi_bright_white": "#FFFFFF",
    "ansi_bright_yellow": "#FFFF00",
    "ansi_cyan": "#008080",
    "ansi_green": "#008000",
    "ansi_magenta": "#800080",
    "ansi_red": "#800000",
    "ansi_white": "#C0C0C0",
    "ansi_yellow": "#808000",
    "antiquewhite": "#FAEBD7",
    "aqua": "#00FFFF",
    "aquamarine": "#7FFFD4",
    "azure": "#F0FFFF",
    "beige": "#F5F5DC",
    "bisque": "#FFE4C4",
    "black": "#000000",
    "blanchedalmond": "#FFEBCD",
    "blue": "#0000FF",
    "blueviolet": "#8A2BE2",
    "brown": "#A52A2A",
    "burlywood": "#DEB887",
    "cadetblue": "#5F9EA0",
    "chartreuse": "#7FFF00",
    "chocolate": "#D2691E",
    "coral": "#FF7F50",
    "cornflowerblue": "#6495ED",
    "cornsilk": "#FFF8DC",
    "crimson": "#DC143C",
    "cyan": "#00FFFF",
    "darkblue": "#00008B",
    "darkcyan": "#008B8B",
    "darkgoldenrod": "#B8860B",
    "darkgray": "#A9A9A9",
    "darkgreen": "#006400",
    "darkgrey": "#A9A9A9",
    "darkkhaki": "#BDB76B",
    "darkmagenta": "#8B008B",
    "darkolivegreen": "#556B2F",
    "darkorange": "#FF8C00",
    "darkorchid": "#9932CC",
    "darkred": "#8B0000",
    "darksalmon": "#E9967A",
    "darkseagreen": "#8FBC8F",
    "darkslateblue": "#483D8B",
    "darkslategray": "#2F4F4F",
    "darkturquoise": "#00CED1",
    "darkviolet": "#9400D3",
    "deeppink": "#FF1493",
    "deepskyblue": "#00BFFF",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1E90FF",
    "firebrick": "#B22222",
    "floralwhite": "#FFFAF0",
    "forestgreen": "#228B22",
    "fuchsia": "#FF00FF",
    "gainsboro": "#DCDCDC",
    "ghostwhite": "#F8F8FF",
    "gold": "#FFD700",
    "goldenrod": "#DAA520",
    "gray": "#808080",
    "green": "#008000",
    "greenyellow": "#ADFF2F",
    "grey": "#808080",
    "honeydew": "#F0FFF0",
    "hotpink": "#FF69B4",
    "indianred": "#CD5C5C",
    "indigo": "#4B0082",
    "ivory": "#FFFFF0",
    "khaki": "#F0E68C",
    "lavender": "#E6E6FA",
    "lavenderblush": "#FFF0F5",
    "lawngreen": "#7CFC00",
    "lemonchiffon": "#FFFACD",
    "lightblue": "#ADD8E6",
    "lightcoral": "#F08080",
    "lightcyan": "#E0FFFF",
    "lightgoldenrodyellow": "#FAFAD2",
    "lightgray": "#D3D3D3",
    "lightgreen": "#90EE90",
    "lightpink": "#FFB6C1",
    "lightsalmon": "#FFA07A",
    "lightseagreen": "#20B2AA",
    "lightskyblue": "#87CEFA",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#B0C4DE",
    "lightyellow": "#FFFFE0",
    "lime": "#00FF00",
    "limegreen": "#32CD32",
    "linen": "#FAF0E6",
    "magenta": "#FF00FF",
    "mediumaquamarine": "#66CDAA",
    "mediumblue": "#0000CD",
    "mediumorchid": "#BA55D3",
    "mediumpurple": "#9370DB",
    "mediumseagreen": "#3CB371",
    "mediumslateblue": "#7B68EE",
    "mediumspringgreen": "#00FA9A",
    "mediumturquoise": "#48D1CC",
    "mediumvioletred": "#C71585",
    "midnightblue": "#191970",
    "mintcream": "#F5FFFA",
    "mistyrose": "#FFE4E1",
    "moccasin": "#FFE4B5",
    "navajowhite": "#FFDEAD",
    "navy": "#000080",
    "oldlace": "#FDF5E6",
    "olive": "#808000",
    "olivedrab": "#6B8E23",
    "orange": "#FFA500",
    "orangered": "#FF4500",
    "orchid": "#DA70D6",
    "palegoldenrod": "#EEE8AA",
    "palegreen": "#98FB98",
    "paleturquoise": "#AFEEEE",
    "palevioletred": "#DB7093",
    "papayawhip": "#FFEFD5",
    "peachpuff": "#FFDAB9",
    "peru": "#CD853F",
    "pink": "#FFC0CB",
    "plum": "#DDA0DD",
    "powderblue": "#B0E0E6",
    "purple": "#800080",
    "rebeccapurple": "#663399",
    "red": "#FF0000",
    "rosybrown": "#BC8F8F",
    "royalblue": "#4169E1",
    "saddlebrown": "#8B4513",
    "salmon": "#FA8072",
    "sandybrown": "#F4A460",
    "seagreen": "#2E8B57",
    "seashell": "#FFF5EE",
    "sienna": "#A0522D",
    "silver": "#C0C0C0",
    "skyblue": "#87CEEB",
    "slateblue": "#6A5ACD",
    "slategray": "#708090",
    "snow": "#FFFAFA",
    "springgreen": "#00FF7F",
    "steelblue": "#4682B4",
    "tan": "#D2B48C",
    "teal": "#008080",
    "thistle": "#D8BFD8",
    "tomato": "#FF6347",
    "turquoise": "#40E0D0",
    "violet": "#EE82EE",
    "wheat": "#F5DEB3",
    "white": "#FFFFFF",
    "whitesmoke": "#F5F5F5",
    "yellow": "#FFFF00",
    "yellowgreen": "#9ACD32"
}

# User input for hex color
while True:
    user_input = input("Enter a hex color code (e.g., #FFFFFF) or 'q' to quit: ")

    # Check if the input is a valid hex color code
    if is_valid_hex_color(user_input):
        # Find the top 3 nearest colors
        nearest_colors = find_nearest_colors(user_input, color_dict.values(), top_n=3)

        # Display the results
        print(f"The nearest colors to {user_input} are:")
        for i, (nearest_color_hex, distance) in enumerate(nearest_colors):
            nearest_color_name = [name for name, hex_code in color_dict.items() if hex_code.lower() == nearest_color_hex.lower()]
            nearest_color_name = nearest_color_name[0] if nearest_color_name else "Unknown"
            print(f"{i + 1}. {nearest_color_hex} ({nearest_color_name}), Distance: {distance:.2f}")
        break
    else:
        if user_input.lower() == "q":
            break
        else:
            print("Invalid hex color code. Please enter a valid hex color (e.g., #FFFFFF).")
            print()
