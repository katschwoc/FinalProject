# CMYKinator

## Repository
https://github.com/katschwoc/FinalProject.git

## Description
As a digital illustrator, myself and many friends have come across time consuming issues when converting our digital art into CMYK color profiles, and we spend hours manipulating each color into a CMYK adjacent color due to color distortion and desaturation. This program will convert digital images into CMYK with minimal color distortion as well as feature various image manipulation options in much less time than conventional painting programs. 

## Features
- CMYK adjustments
    - Beginning with Pillow, the CMYK channels will be broken apart so the artist can specify what percentage of which color channel should be used to match the print to the digital artwork as closely as possible. Wish for the ability to specify a CMYK profile.
- Contrast adjustments
    - This will allow the artist to increase or decrease contrast 
- Watermark
    - This will allow the artist to place watermarks on their artwork with specified opacity 
- Batch Render
    - This option will allow the artist to convert the color profiles of multiple images in a single execution
- Resizing
    - this option will allow the artist to resize their images for larger or smaller prints

## Challenges
- Pillow's preset CMYK conversion gets the colors close depending on which specific RGB mode the artist used, but there is still some color distortion and contrast loss, especially with the magenta channels and contrast in art created on P3 color profiles. I will research breaking apart color channels so the artist can input what percentage of each channel they need to use to match their digital art
- Batch rendering has not worked well for me in the past, so I will need revisit this lesson to understand where I'm messing up
- I will need to research if Pillow uses a generic CMYK color profile, or if it can be adjusted to meet a printer's specified CMYK profile and paper requirements such as Coated or Uncoated options. Adjusting to a specific printer's CMYK profile is something I would love to add, but I don't know if it is at all possible right now. This is a reaching option, but if I can figure it out, it will happen. 

## Outcomes
Ideal outcomes
- Batch render digital art, converting to high quality prints without wasting time redoing every color pixel as well as image manipulation options relevant to printed artwork

Minimal Outcomes
- Digital art that converts to CMYK and has relevant image manipulation options 

## Milestones
- Week 1
    1. Implement Pillow
    2. Set up image manipulation options
    3. Set up batch rendering
- Week 2
    1. Break apart CMYK color channels 
    2. Determine whether CMYK color profiles can be specified
