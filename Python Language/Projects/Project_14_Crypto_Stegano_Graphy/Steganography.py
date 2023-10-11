from PIL import Image

def hide_text_in_image(image_path, text, output_path):
    img = Image.open(image_path)
    encoded_img = img.copy()

    # Convert the text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Check if the text can fit in the image
    if len(binary_text) > img.width * img.height:
        raise ValueError("Text too large for the image")

    data_index = 0

    for x in range(img.width):
        for y in range(img.height):
            pixel = list(img.getpixel((x, y)))

            for color_channel in range(3):  # RGB channels
                if data_index < len(binary_text):
                    pixel[color_channel] = pixel[color_channel] & 254 | int(binary_text[data_index])
                    data_index += 1

            encoded_img.putpixel((x, y), tuple(pixel))

    encoded_img.save(output_path)

def reveal_text_from_image(image_path):
    img = Image.open(image_path)
    binary_text = ''

    for x in range(img.width):
        for y in range(img.height):
            pixel = list(img.getpixel((x, y)))

            for color_channel in range(3):  # RGB channels
                binary_text += str(pixel[color_channel] & 1)

    text = ''.join([chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8)])
    return text

# Example usage
image_path = r'E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\WIN_20230613_15_30_35_Pro.jpg'  # Replace with your image file
text_to_hide = 'I am Raiden The cyber Assassin'
output_image_path = r'E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\output_image.png'

# Hide text in the image
hide_text_in_image(image_path, text_to_hide, output_image_path)

# Retrieve the hidden text from the image
hidden_text = reveal_text_from_image(output_image_path)
print("Hidden Text:", hidden_text)
