import random
import tkinter as tk

class imageRenderer:
    def __init__(self, canvas, image_data, config_data):
        self.canvas = canvas
        self.image_data = image_data
        self.config_data = config_data

    def draw_pixel(self, x0, y0, delay):
        # This method schedules drawing a single pixel with a delay
        self.canvas.after(delay, lambda: self.canvas.create_rectangle(x0, y0, x0 + self.config_data["pixel_size"], y0 + self.config_data["pixel_size"], fill="white", outline=""))

    def draw_image(self, start_x, start_y):
        draw_commands = []
        bytes_per_row = (self.image_data["width_pixels"] + 7) // 8

        for row in range(self.image_data["height"]):
            for byte_index in range(bytes_per_row):
                byte_value = self.image_data["bytes"][row * bytes_per_row + byte_index]
                for bit in range(8):
                    if byte_index * 8 + bit >= self.image_data["width_pixels"]:
                        break
                    pixel_on = (byte_value >> (7 - bit)) & 1
                    if pixel_on:
                        x0 = start_x + (byte_index * 8 + bit) * (self.config_data["pixel_size"] + self.config_data["gap_size"])
                        y0 = start_y + row * (self.config_data["pixel_size"] + self.config_data["gap_size"])
                        draw_commands.append((x0, y0))

        # Shuffle the list of draw commands to randomize the order
        random.shuffle(draw_commands)
        # Schedule each draw command with an increasing delay to visualize the effect
        delay = 0
        delay_increment = 3  # Milliseconds between each pixel draw, adjust as needed
        for x0, y0 in draw_commands:
            self.draw_pixel(x0, y0, delay)
            delay += delay_increment
    