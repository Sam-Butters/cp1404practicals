"""
CP1404 Practical 5 - Hex Colours
Sam Butters
"""

hex_colours = {"black": "#000000", "grey": "#808080", "white": "#ffffff", "red": "#ff0000", "orange": "#ffa500",
               "yellow": "#ffff00",
               "green": "#008000", "blue": "0000ff", "indigo": "#4b0082", "violet": "#ee82ee"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"Colour: {colour_name}  Hex code: {hex_colours[colour_name]}")
    except KeyError:
        print(f"{colour_name} is not on the list")
    colour_name = input("Enter colour name: ").lower()

print("Goodbye")
