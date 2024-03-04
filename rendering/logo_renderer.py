import tkinter as tk
from utils.data_loader import load_json_data

class LogoRenderer:
    def __init__(self, canvas, logo_data, config_data):
        self.canvas = canvas
        self.logo_data = logo_data
        self.config_data = config_data  # Store configuration data as an instance variable
    
    def draw_logo(self, start_x, start_y):
        bytes_per_row = (self.logo_data["width_pixels"] + 7) // 8
        for row in range(self.logo_data["height"]):
            for byte_index in range(bytes_per_row):
                byte_value = self.logo_data["bytes"][row * bytes_per_row + byte_index]
                for bit in range(8):
                    if byte_index * 8 + bit >= self.logo_data["width_pixels"]:
                        break
                    pixel_on = (byte_value >> (7 - bit)) & 1
                    if pixel_on:
                        x0 = start_x + (byte_index * 8 + bit) * (self.config_data["pixel_size"] + self.config_data["gap_size"])
                        y0 = start_y + row * (self.config_data["pixel_size"] + self.config_data["gap_size"])
                        self.canvas.create_rectangle(x0, y0, x0 + self.config_data["pixel_size"], y0 + self.config_data["pixel_size"], fill="white", outline="")
