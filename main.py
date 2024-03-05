import tkinter as tk
from rendering.image_renderer import imageRenderer
from utils.data_loader import load_json_data
from rendering.drawing_utils import clear_screen

# Load configurations and image data
config_data = load_json_data('config.json')
image_data = load_json_data('assets/image.json')

# Initialize Tkinter root and canvas
root = tk.Tk()
root.title("image Rendering")
canvas = tk.Canvas(root, width=config_data["window_width"], height=config_data["window_height"], bg="black")
canvas.pack()

# Create imageRenderer instance and draw the image
image_renderer = imageRenderer(canvas, image_data, config_data)
rendered_image_width = image_data["width_pixels"] * (config_data["pixel_size"] + config_data["gap_size"]) - config_data["gap_size"]
rendered_image_height = image_data["height"] * (config_data["pixel_size"] + config_data["gap_size"]) - config_data["gap_size"]
start_x = (config_data["window_width"] - rendered_image_width) // 2
start_y = (config_data["window_height"] - rendered_image_height) // 2

image_renderer.draw_image(start_x, start_y)

# clear_screen(canvas, config_data["window_width"], config_data["window_height"], config_data["pixel_size"], config_data["gap_size"], "red", 1)
# clear
# image_renderer.draw_wave_effect(start_x, start_y)
# hi!!
# Start the Tkinter event loop
root.mainloop()
