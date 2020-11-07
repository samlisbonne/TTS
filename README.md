# TTS
Used to host scripts which may be of interest for Tabletop Simulator Users

ABOUT: Deck Generator

This code is intended to generate concatenated image files for uploading custom card decks to Tabletop Simulator (TTS). In TTS, users must specify a series of dimensions and then provide one file with all cards placed in adjacent spaces. This script takes all card images from a given folder and concatenates them into a single image suitable for upload.

INPUTS
1) a folder with all card faces. The default pathway assumes that this file is run in a directory also containing a folder of images titled "to_concat"
2) card face images. These must be .png or .jpg.
3) dimensions [optional]. If unspecified, the script uses default TTS max dimensions and derives the total deck count from files and associated filenames (see line above)

REQUIREMENTS:
1) all card faces must be the same size.
2) IMPORTANT: the last character in the filename needs to be an integer specifying the number of instances of that card in the deck

OUTPUTS
1) a single image file, RGB, called "newdeck.jpg". This is ready for TTS upload
