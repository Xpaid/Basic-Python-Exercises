from pathlib import Path
from PIL import Image, ImageTk
import pyglet

# Color Variables
PRIMARY = "#007bff"
SECONDARY = "#6c757d"
SUCCESS = "#28a745"
DANGER = "#dc3545"
WARNING = "#ffc107"
INFO = "#17a2b8"
LIGHT = "#f8f9fa"
DARK = "#000000"

pyglet.options['win32_gdi_font'] = True

fontpath = Path(__file__).parent.parent / 'assets' / 'Bloxat.ttf'
pyglet.font.add_file(str(fontpath))

Bloxat = "Bloxat"

def load_image(image_name):
    img_path = Path(__file__).parent.parent / 'assets' / image_name  # Update to your image path
    img = Image.open(img_path)  # Open the image using Pillow

    target_width = 300
    target_height = int(target_width * 4 / 3)  
    img = img.resize((target_width, target_height)) 

    return ImageTk.PhotoImage(img)

