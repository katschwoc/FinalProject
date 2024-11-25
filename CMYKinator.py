from PIL import Image, ImageEnhance, ImageFilter
import os

def main():
    """
    Main function that runs the program.
    """
    # input filename and path
    input_file = "input_image.jpg"
    watermark_path = "watermark_image.png"
    output_folder = "CMYK_Images"

    # create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the input file
    with Image.open(input_file) as image:
        # Resize image
        resized_image = resize_img(image, height=800)

        # Add watermark before converting to CMYK
        watermarked_image = watermark(resized_image, watermark_path, transparency=128, position=(100, 100))

        # Convert image to CMYK
        cmyk_image = rgba_to_cmyk(watermarked_image)

        # Adjust CMYK channels (choose values from 0-255)
        cmyk_image = adjust_cyan(cmyk_image, adjustment_value=0)   # Adjust cyan
        cmyk_image = adjust_magenta(cmyk_image, adjustment_value=0)  # Adjust magenta
        cmyk_image = adjust_yellow(cmyk_image, adjustment_value=0)  # Adjust yellow
        cmyk_image = adjust_black(cmyk_image, adjustment_value=0)    # Adjust black

        # Apply contrast adjustments (if needed)
        adjusted_image = adjust_contrast(cmyk_image, factor=0)  # Example factor

        # Save the adjusted image
        output_file = os.path.join(output_folder, "{input_file}_CMYK_Adjusted.jpg")
        adjusted_image.save(output_file)
        print(f"Image saved as {output_file}")

def watermark(image, watermark_path, transparency=128, position=(0, 0)):
    """
    Adds a watermark to the image with transparency and position options.
    Alpha channel for transparency adjustments.
    Pasts the watermark onto the original image.
    """
    # Open the watermark image
    with Image.open(watermark_path) as watermark:
        # Resize watermark if needed (optional, resizing to 25% of the original image size)
        width = image.width // 4
        height = image.height // 4
        watermark_resized = watermark.resize((width, height))

        # Get the position (defaults to bottom-left)
        padding = 50
        x = position[0] if position[0] else padding
        y = position[1] if position[1] else image.height - watermark_resized.height - padding

        # If watermark is not in RGBA mode, convert it to RGBA to support transparency
        if watermark_resized.mode != 'RGBA':
            watermark_resized = watermark_resized.convert("RGBA")

        # Modify the transparency (alpha channel) of the watermark
        watermark_data = watermark_resized.getdata()
        new_watermark_data = []
        for item in watermark_data:
            r, g, b, a = item
            a = int(a * (transparency / 255))  # Adjust transparency (0-255)
            new_watermark_data.append((r, g, b, a))
        watermark_resized.putdata(new_watermark_data)

        # Paste the watermark onto the image using the alpha channel as a mask
        image.paste(watermark_resized, (x, y), mask=watermark_resized.getchannel('A'))

        return image

def rgba_to_cmyk(image):
    """
    Converts the image from RGBA to CMYK.
    """
    # Ensure the image is in RGB mode first
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert RGB to CMYK
    cmyk_image = image.convert('CMYK')

    return cmyk_image

def adjust_cyan(cmyk_image, adjustment_value):
    """
    Adjust the Cyan channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    c = c.point(lambda i: i + adjustment_value)  # Adjust cyan
    c = c.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))

def adjust_magenta(cmyk_image, adjustment_value):
    """
    Adjust the Magenta channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    m = m.point(lambda i: i + adjustment_value)  # Adjust magenta
    m = m.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))

def adjust_yellow(cmyk_image, adjustment_value):
    """
    Adjust the Yellow channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    y = y.point(lambda i: i + adjustment_value)  # Adjust yellow
    y = y.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))

def adjust_black(cmyk_image, adjustment_value):
    """
    Adjust the Black channel in the CMYK image.
    Adjustment_value is a value between 0 and 255.
    """
    c, m, y, k = cmyk_image.split()
    k = k.point(lambda i: i + adjustment_value)  # Adjust black
    k = k.point(lambda i: max(min(i, 255), 0))  # Range is between 0 and 255

    return Image.merge("CMYK", (c, m, y, k))

def resize_img(img, height):
    """
    Resize the image while maintaining aspect ratio.
    """
    aspect_ratio = img.width / img.height
    resize_width = int(height * aspect_ratio)
    resized_img = img.resize((resize_width, height))

    return resized_img

def adjust_contrast(cmyk_image, factor):
    """
    Adjust the contrast of the image.
    """
    enhancer = ImageEnhance.Contrast(cmyk_image)
    return enhancer.enhance(factor)

# def batch_render():
# optional function not needed if just one image is being manipulated
# if more than one image, use function. if not only one image, save file 
# after rgb_to_cmyk converts image and after image manipulations are completed
# function batch renders images with similar file names such as "artworkRGB.jpg and drawingRGB.jpg"
# function saves rendered images to new folder called "CMYK Images"




if __name__ == "__main__":
    main()