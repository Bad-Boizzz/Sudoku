text_colors = {
    "black":   30,
    "red":     31,
    "green":   32,
    "yellow":  33,
    "blue":    34,
    "magenta": 35,
    "cyan":    36,
    "white":   37,
    "reset":   0
}

bg_colors = {
        "black":   40,
        "red":     41,
        "green":   42,
        "yellow":  43,
        "blue":    44,
        "magenta": 45,
        "cyan":    46,
        "white":   47,
        "reset":   0
    }

def print_flavoured_text(text, color="reset", background="reset", end = "\n", sep = " ", flush = True):
    """
    Print text with a specified color and background color. After printing, the color and background are reset to default.
    """
    if color not in text_colors:
        raise ValueError(f"Invalid color: {color}. Available colors are: {', '.join(text_colors.keys())}")
    if background not in bg_colors:
        raise ValueError(f"Invalid background color: {background}. Available colors are: {', '.join(bg_colors.keys())}")
    print(f"\033[{bg_colors[background]}m{text}\033[0m", end=end, sep=sep, flush=flush)

def print_colored_background(text, background="black", end = "\n", sep = " ", flush = True):
    """
    Print text with a specified background color. After printing, the background color is reset to default.
    """ 
    if background not in bg_colors:
        raise ValueError(f"Invalid background color: {background}. Available colors are: {', '.join(bg_colors.keys())}")
    print(f"\033[{bg_colors[background]}m{text}\033[0m", end=end, sep=sep, flush=flush)


def print_colored_text(text, color="reset", end = "\n", sep = " ", flush = True):
    """
    Print text in a specified color. After printing, the color is reset to default.
    """ 
    if color not in text_colors:
        raise ValueError(f"Invalid color: {color}. Available colors are: {', '.join(text_colors.keys())}")
    print(f"\033[{text_colors[color]}m{text}\033[0m", end=end, sep=sep, flush=flush)


def change_text_color(color="reset"):
    """
    Change the text color. All text printed after this will be in the specified color.
    To reset the color, use "reset".
    """
    if color not in text_colors:
        raise ValueError(f"Invalid color: {color}. Available colors are: {', '.join(text_colors.keys())}")
    print(f"\033[{text_colors[color]}m", end='')

def change_background_color(background="reset"):
    """
    Change the background color. All text printed after this will be in the specified background color.
    To reset the background color, use "reset".
    """
    if background not in bg_colors:
        raise ValueError(f"Invalid background color: {background}. Available colors are: {', '.join(bg_colors.keys())}")
    print(f"\033[{bg_colors[background]}m", end='')

if __name__ == "__main__":
    # Example usage
    # print_colored_text("Hello, World!", "red")
    # print_colored_text("Hello, World!", "green")
    # print_colored_text("Hello, World!", "blue")
    # print_colored_text("Hello, World!", "yellow")
    # print_colored_text("Hello, World!", "magenta")
    # print_colored_text("Hello, World!", "cyan")
    # print_colored_text("Hello, World!", "white")
    # print_colored_text("Hello, World!", "black")
    # print("elo")
   

    # print("elo")
    # change_text_color("red")
    # print("elo")
    # print_colored_background("Hello, World!", "red")
    # print_colored_background("Hello, World!", "green")
    # print_colored_background("Hello, World!", "blue")
    # print_colored_background("Hello, World!", "reset")

    print_flavoured_text("Hello, World!", "red", "green", end = "asd", flush = True)