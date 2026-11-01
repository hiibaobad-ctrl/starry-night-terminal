# ?? Starry Night in the Terminal

A Python script that renders Vincent van Gogh's *The Starry Night* directly inside your terminal using ANSI true-color codes and half-block characters.

## How it works
The script downloads the original high-resolution painting, resizes it to fit your terminal window dynamically, and renders it using the ¯ (upper half block) character. By setting the foreground color to the top pixel and the background color to the bottom pixel, we achieve a crisp, 2x vertical resolution pixel art effect.

## Installation
1. Clone the repository
2. Install the required library:
   pip install pillow

## Usage
Run the script:
   python starry_terminal.py

*(Note: For the best experience, use a terminal that supports TrueColor (24-bit), like Windows Terminal, iTerm2, or the VS Code integrated terminal. Make sure your terminal window is maximized!)*
