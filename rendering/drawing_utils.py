import random
import tkinter as tk

def clear_screen(canvas, width, height, pixel_size, gap_size, color, t):
    # Determine the effective step size, including the gap
    step_size = pixel_size + gap_size

    # Calculate the number of pixels that can be drawn, considering the step size
    num_pixels_x = (width + gap_size) // step_size
    num_pixels_y = (height + gap_size) // step_size

    # Generate positions for all pixels that cover the canvas
    pixel_positions = [(x * step_size, y * step_size) for x in range(num_pixels_x) for y in range(num_pixels_y)]

    # Shuffle to randomize the order
    random.shuffle(pixel_positions)

    # Schedule coloring each pixel
    for i, (x0, y0) in enumerate(pixel_positions):
        schedule_pixel_color(canvas, x0, y0, pixel_size, color, i * t)

def schedule_pixel_color(canvas, x0, y0, pixel_size, color, delay):
    # Define the drawing operation with correct dimensions and color
    canvas.after(delay, lambda: canvas.create_rectangle(x0, y0, x0 + pixel_size, y0 + pixel_size, fill=color, outline=""))
