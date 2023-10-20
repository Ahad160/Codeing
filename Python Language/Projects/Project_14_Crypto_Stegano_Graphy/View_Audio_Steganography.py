from pydub import AudioSegment
import numpy as np

# Function to extract the hidden message
def extract_message(audio_file):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert the audio to a numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Extract the message from the audio
    message_binary = ""
    for sample in audio_array:
        message_bit = sample & 1  # Extract the least significant bit
        message_binary += str(message_bit)

    # Convert the binary message to text
    message = ""
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i+8]
        message += chr(int(byte, 2))

    return message

if __name__ == "__main__":
    audio_file = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Music_With_Hidden_Message.wav"  # The modified audio file

    extracted_message = extract_message(audio_file)
    print("Extracted Message:", extracted_message)
