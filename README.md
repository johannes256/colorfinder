# Nearest color finder for Textual

This Python script allows users to input a hex color code and find the top 3 nearest colors from the list of named colors for [textual](https://textual.textualize.io/api/color/#textual.color--named-colors). The nearest colors are calculated using the Euclidean distance in the RGB color space.

## Features

- **Hex Color Validation**: Ensures that user inputs are valid hex color codes.
- **Nearest Color Matching**: Finds and displays the top 3 closest color matches from a predefined dictionary of colors.
- **Predefined Color Dictionary**: Includes a dictionary of named hex colors based on common color names.
- **Distance Calculation**: Uses Euclidean distance to measure the difference between RGB values.

## How It Works

1. The user is prompted to input a valid hex color code (e.g., `#FF6347`).
2. The script calculates the Euclidean distance between the input color and each color in the predefined dictionary.
3. It returns the top 3 closest matching colors along with their names (if available) and the calculated distances.

## Usage

1. Clone or download the script.
2. Ensure that you have Python 3 installed.
3. Run the script in a terminal or command prompt.

   ```bash
   python nearest_color_finder.py
   ```

4. Enter a hex color code when prompted (e.g., `#FFFFFF` for white).
5. The script will display the top 3 closest colors to the input.

## Example Input and Output

```bash
Enter a hex color code (e.g., #FFFFFF) or 'q' to quit: #FF6347
The nearest colors to #FF6347 are:
1. #FF6347 (tomato), Distance: 0.00
2. #FF4500 (orangered), Distance: 29.00
3. #FFA07A (lightsalmon), Distance: 86.87
```

## Exiting

- To exit the script, simply enter q.

## Requirements

- Python 3.x nd the `math` module (which is part of the Python standard library).

## Functions

- `find_nearest_colors(hex_color, color_list, top_n=3)`: Finds the top N nearest colors to the input hex color.
- `hex_to_rgb(hex_color)`: Converts a hex color to RGB values.
- `is_valid_hex_color(hex_color)`: Validates whether the input is a valid hex color code.

## Functions

This project is open-source and available under GNU General Public License version 3.
