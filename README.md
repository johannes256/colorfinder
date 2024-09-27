# Nearest Hex Color Finder

This Python script helps you find the nearest color from a predefined list of hex color codes. It uses the Euclidean distance in the RGB color space to calculate which color from the list is the closest to the given hex color.

## Features

- **Hex to RGB Conversion**: Converts a hex color code to its corresponding RGB values.
- **Euclidean Distance Calculation**: Finds the nearest color by computing the Euclidean distance between the RGB values of the input color and each color in the list.
- **Predefined Color List**: Includes an extensive list of common hex color codes.

## How It Works

1. The script converts the input hex color code into its RGB values.
2. It iterates over a list of predefined hex color codes, converting each to RGB.
3. The script then computes the Euclidean distance between the input color's RGB values and each color in the list.
4. Finally, the color with the smallest distance is returned as the nearest match.

## Usage

1. Clone the repository and navigate to the project directory.
2. The main function to use is `find_nearest_color(hex_color, color_list)`.
   
      Example:
      
         ```python
            hex_color = "#f2e3bc"  # Input hex color
               nearest_color = find_nearest_color(hex_color, color_list)
                  print(f"The nearest color to {hex_color} is {nearest_color}")
                     ```
                     
                     3. A list of hex color codes is provided within the script, but you can modify it if needed.
                     
                     ## Example Output
                     
                     For an input color of `#f2e3bc`, the script returns the nearest color from the list as `#f5deb3`.
                     
                     ## Dependencies
                     
                     This script requires Python 3.x and the `math` module (which is part of the Python standard library).
                     
                     ---
                     
                     This text gives users an overview of what the script does, how it works, and how to use it. You can adjust it further based on your needs or additional features.
