# -*- coding: utf-8 -*-
import urllib.request
from PIL import Image
import os
import time

# 1. Download the image if it doesn't exist
img_path = "starry_night_source.jpg"
if not os.path.exists(img_path):
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
    print("Downloading masterpiece...")
    urllib.request.urlretrieve(url, img_path)

# 2. Get terminal size dynamically
try:
    terminal_size = os.get_terminal_size()
    term_width = terminal_size.columns
    term_height = terminal_size.lines
except:
    term_width = 120
    term_height = 40

img_width = term_width - 2 
img_height = (term_height - 4) * 2 

# 3. Open and resize the image
img = Image.open(img_path)
img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)

# 4. Clear screen and hide cursor
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[?25l", end="")

print("\n  \033[1;33mThe Starry Night - Vincent van Gogh\033[0m\n")

# 5. Render using the '▀' character
for y in range(0, img_height, 2):
    line = "  " 
    for x in range(img_width):
        r1, g1, b1 = img.getpixel((x, y))[:3]
        if y + 1 < img_height:
            r2, g2, b2 = img.getpixel((x, y + 1))[:3]
        else:
            r2, g2, b2 = (0, 0, 0)
        
        # Foreground = Top pixel, Background = Bottom pixel
        line += f"\033[38;2;{r1};{g1};{b1}m\033[48;2;{r2};{g2};{b2}m\u2580"
    
    line += "\033[0m"
    print(line)
    time.sleep(0.02)

print("\033[?25h", end="")
print("\n  \033[1;36mPress Enter to exit...\033[0m")
input()