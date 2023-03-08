#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:57:08 2023

@author: dakidarts
"""


import random
import os
from PIL import Image, ImageFilter

def generate_gradient(num_gradients, width, height):
    # Define the starting and ending colors of the gradient
    start_color = (random.randint(50, 255), random.randint(40, 255), random.randint(30, 255), random.randint(50, 255))
    end_color = (random.randint(30, 255), random.randint(60, 255), random.randint(50, 255), random.randint(30, 255))
    
    # Calculate the increment for each color channel
    r_inc = (end_color[0] - start_color[0]) / num_gradients
    g_inc = (end_color[1] - start_color[1]) / num_gradients
    b_inc = (end_color[2] - start_color[2]) / num_gradients
    
    # Generate the gradient
    gradient = []
    for i in range(num_gradients):
        r = int(start_color[0] + (r_inc * i))
        g = int(start_color[1] + (g_inc * i))
        b = int(start_color[2] + (b_inc * i))
        gradient.append((r, g, b))
    
    # Create a new image with the gradient
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            pixel_color = gradient[int(x / width * num_gradients)]
            pixels[x, y] = pixel_color
            
            
        
    # Apply effects to the gradient image
    image = image.filter(ImageFilter.GaussianBlur(radius=num_blur))
    
    return image

# Create the gradients directory if it does not exist
if not os.path.exists("gradients"):
    os.makedirs("gradients")

# Define image sizes
hd_size = (1280, 720)
two_k_size = (1920, 1080)
four_k_size = (3840, 2160)
eight_k_size = (7680, 4320)

# Define options for number of gradients and image size
num_gradients_options = range(1, 101)
image_size_options = {"hd": hd_size, "2k": two_k_size, "4k": four_k_size, "8k": eight_k_size}
num_blur_options = range(100, 501)

# Ask the user to choose the number of gradients and image size
while True:
    num_gradients = input(f"How many gradients do you want to generate ({num_gradients_options[0]}-{num_gradients_options[-1]})? ")
    try:
        num_gradients = int(num_gradients)
        if num_gradients not in num_gradients_options:
            print(f"Please enter a number between {num_gradients_options[0]} and {num_gradients_options[-1]}")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    image_size = input(f"What image resolution do you want (HD, 2K, 4K, 8K)? ")
    try:
        image_size = image_size.lower()
        if image_size not in image_size_options.keys():
            print("Please enter a valid image size option")
            continue
        break
    except ValueError:
        print("Please enter a valid option")


while True:
    num_blur = input(f"What amount of Blur Radius do you want ({num_blur_options[0]}-{num_blur_options[-1]})? ")
    try:
        num_blur = int(num_blur)
        if num_blur not in num_blur_options:
            print(f"Please enter a number between {num_blur_options[0]} and {num_blur_options[-1]}")
            continue
        break
    except ValueError:
        print("Please enter a valid number")
        
        
        
# Generate gradient images
width, height = image_size_options[image_size]
for i in range(1, num_gradients + 1):
    gradient = generate_gradient(num_gradients, width, height)
    filename = f"gradients/soup_{i}.png"
    gradient.save(filename)

print("Tada.. your soup is ready! enjoy :)")
