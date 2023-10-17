# Function to embed a message securely
def Embed_message(audio_file, message, output_file):
    from pydub import AudioSegment
    import numpy as np
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert the message to binary
    message_binary = ''.join(format(ord(char), '08b') for char in message)

    # Ensure the audio file is long enough to hide the message
    required_length = len(message_binary)
    if required_length > len(audio):
        raise ValueError("The message is too long to hide in this audio file.")

    # Convert the audio to a numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Embed the message securely
    for i, bit in enumerate(message_binary):
        audio_array[i] = (audio_array[i] & ~1) | int(bit)

    # Create a new audio segment from the modified array
    result_audio = AudioSegment(audio_array.tobytes(), frame_rate=audio.frame_rate, sample_width=audio.sample_width, channels=audio.channels)

    # Export the result as a new audio file
    result_audio.export(output_file, format="wav")
    
    print("Message hidden securely.")
    
    return output_file
