
# Function to hide text within an image
def hide_text_in_image(input_image_path, output_image_path, secret_text):
    from stegano import lsb
    secret = lsb.hide(input_image_path, secret_text)
    secret.save(output_image_path)

    # hide_text_in_image(input_image, output_image, secret_message)
    extracted_message = extract_text_from_image(output_image)

    print("Message hidden securely.")

    return output_image_path
