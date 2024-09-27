#!/home/johannes/.local/venv/bin/python
# /***************************************************************************
#  *   colorfinder.py                                                              *
#  *                                                                         *
#  *   Copyright (C) 2023-2024 by Jan Dolstra                                *
#  *   jan@jandnet.nl                                                        *
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

def find_nearest_color(hex_color, color_list):
  """Finds the nearest color in the given list to the specified hex color.

  Args:
    hex_color: The hex color to find the nearest match for.
    color_list: A list of hex colors to search through.

  Returns:
    The nearest hex color in the list to the specified hex color.
  """

  # Convert the hex color to RGB values
  r, g, b = hex_to_rgb(hex_color)

  # Find the nearest color in the list
  nearest_color = None
  nearest_distance = float('inf')
  for color in color_list:
    cr, cg, cb = hex_to_rgb(color)
    distance = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
    if distance < nearest_distance:
      nearest_color = color
      nearest_distance = distance

  return nearest_color

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

# Example usage
color_list = hex_codes = [    
    "#f0f8ff", "#000000", "#000080", "#808080", "#0000ff", "#00ffff", "#00ff00", "#ff00ff", 
    "#ff0000", "#ffffff", "#ffff00", "#008080", "#008000", "#800080", "#800000", "#c0c0c0", 
    "#808000", "#faebd7", "#00ffff", "#7fffd4", "#f0ffff", "#f5f5dc", "#ffe4c4", "#000000", 
    "#ffebcd", "#0000ff", "#8a2be2", "#a52a2a", "#deb887", "#5f9ea0", "#7fff00", "#d2691e", 
    "#ff7f50", "#6495ed", "#fff8dc", "#dc143c", "#00ffff", "#00008b", "#008b8b", "#b8860b", 
    "#a9a9a9", "#006400", "#a9a9a9", "#bdb76b", "#8b008b", "#556b2f", "#ff8c00", "#9932cc", 
    "#8b0000", "#e9967a", "#8fbc8f", "#483d8b", "#2f4f4f", "#2f4f4f", "#00ced1", "#9400d3", 
    "#ff1493", "#00bfff", "#696969", "#696969", "#1e90ff", "#b22222", "#fffaf0", "#228b22", 
    "#ff00ff", "#dcdcdc", "#f8f8ff", "#ffd700", "#daa520", "#808080", "#008000", "#adff2f", 
    "#808080", "#f0fff0", "#ff69b4", "#cd5c5c", "#4b0082", "#fffff0", "#f0e68c", "#e6e6fa", 
    "#fff0f5", "#7cfc00", "#fffacd", "#add8e6", "#f08080", "#e0ffff", "#fafad2", "#d3d3d3", 
    "#90ee90", "#d3d3d3", "#ffb6c1", "#ffa07a", "#20b2aa", "#87cefa", "#778899", "#778899", 
    "#b0c4de", "#ffffe0", "#00ff00", "#32cd32", "#faf0e6", "#ff00ff", "#800000", "#66cdaa", 
    "#0000cd", "#ba55d3", "#9370db", "#3cb371", "#7b68ee", "#00fa9a", "#48d1cc", "#c71585", 
    "#191970", "#f5fffa", "#ffe4e1", "#ffe4b5", "#ffdead", "#000080", "#fdf5e6", "#808000", 
    "#6b8e23", "#ffa500", "#ff4500", "#da70d6", "#eee8aa", "#98fb98", "#afeeee", "#db7093",
    "#ffefd5", "#ffdab9", "#cd853f", "#ffc0cb", "#dda0dd", "#b0e0e6", "#800080", "#663399",
    "#ff0000", "#bc8f8f", "#4169e1", "#8b4513", "#fa8072", "#f4a460", "#2e8b57", "#fff5ee",
    "#a0522d", "#c0c0c0", "#87ceeb", "#6a5acd", "#708090", "#708090", "#fffafa", "#00ff7f",
    "#4682b4", "#d2b48c", "#008080", "#d8bfd8", "#ff6347", "#40e0d0", "#ee82ee", "#f5deb3",
    "#ffffff", "#f5f5f5", "#ffff00", "#9acd32"
]
hex_color = "#8ECAE6"
nearest_color = find_nearest_color(hex_color, color_list)
print(nearest_color)
