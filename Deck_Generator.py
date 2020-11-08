# ABOUT
# Written by Sam L
# 7 November 2020

# This code is intended to generate concatenated image files for uploading custom card decks to Tabletop Simulator (TTS).
# In TTS, users must specify a series of dimensions and then provide one file with all cards placed in adjacent spaces.
# This script takes all card images from a given folder and concatenates them into a single image suitable for upload.

# INPUTS
# a folder with all card faces. The default pathway assumes that this file is run in a directory also containing a folder of images titled "to_concat"
# card face images. These must be .png or .jpg. IMPORTANT: the last character in the filename needs to be an integer specifying the number of instances of that card in the deck
# dimensions [optional]. If unspecified, the script uses default TTS max dimensions and derives the total deck count from files and associated filenames (see line above)

# OUTPUTS
# a single image file, RGB, called "newdeck.jpg". This is ready for TTS upload

# Import packages
from PIL import Image, ImageFilter
import glob
import numpy as np
import math

# Import all images from a specified folder. Default is a relative pathname to folder "to_concat"
images = []
for filename in glob.iglob("to_concat/*"):
    # Open a new image
    im = Image.open(filename)
    # Add the image as many times as instances of the card occur in the deck
    # MAKE SURE the last character in the filename (not including .png or .jpg) is the integer count of the card
    count = int(filename[-5])
    for i in range(count):
        # Add the image to a list
        images.append(im)

# PARAMETERS, with explanations and default values
# num_col (width): count of cards along horizontal axis. Default 10, max 10
num_col = 10
# num_row (height): count of cards along vertical axis. Default 7, max 7
num_row = 7
# num_cards: total count of cards in the deck. Default 53, max 70. Using len(images) will count the cards for you, based on card count and instances from the filename
num_cards = len(images)
# Checks
if num_col > 10:
    print('Your specified width exceeds the maximum value of 10.')
if num_row > 7:
    print('Your specified height exceeds the maximum value of 7.')
if num_cards > 70:
    print('Your specified card count exceeds the maximum value of 70.')
if num_cards > num_col*num_row:
    print('Your specified dimensions cannot support the listed card count.')

# NOTE: This code assumes all cards are the exact same dimensions. Ensure that this is true before proceeding.

# Obtain card dimensions
card_w = images[0].width
card_h = images[0].height
# Create base image for complete card deck
des = Image.new(mode = 'RGB', size = (card_w*num_col, card_h*num_row))
# Calculate actual number of rows
row_actual = math.ceil(num_cards/num_col);


# Deck Sythesizer

# First, create each row of the final deck image
row_images = []
idx = 0
for i in range(row_actual):
    row_des = Image.new(mode = 'RGB', size = (card_w*num_col, card_h*1))
    for j in range(num_col):
        if idx < num_cards:
            im = images[idx]
            row_des.paste(im, (j*card_w, 0))
        idx += 1
    row_images.append(row_des)

# Second, append the rows to one another to create the final image
for i in range(row_actual):
    im = row_images[i]
    des.paste(im, (0, i*card_h))

des.save('newdeck.jpg')