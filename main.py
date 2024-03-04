import tkinter as tk
from rendering.logo_renderer import LogoRenderer
from utils.data_loader import load_json_data

# Load configurations and logo data
config_data = load_json_data('config.json')
logo_data = load_json_data('assets/logo.json')

# Initialize Tkinter root and canvas
root = tk.Tk()
root.title("Logo Rendering")
canvas = tk.Canvas(root, width=config_data["window_width"], height=config_data["window_height"], bg="black")
canvas.pack()

# Create LogoRenderer instance and draw the logo
logo_renderer = LogoRenderer(canvas, logo_data, config_data)
rendered_logo_width = logo_data["width_pixels"] * (config_data["pixel_size"] + config_data["gap_size"]) - config_data["gap_size"]
rendered_logo_height = logo_data["height"] * (config_data["pixel_size"] + config_data["gap_size"]) - config_data["gap_size"]
start_x = (config_data["window_width"] - rendered_logo_width) // 2
start_y = (config_data["window_height"] - rendered_logo_height) // 2

logo_renderer.draw_logo(start_x, start_y)

# Start the Tkinter event loop
root.mainloop()
