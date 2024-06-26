import base64

def convert_audio_to_base64(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
    return encoded_string

# Replace 'path_to_your_audio_file.wav' with the path to your audio file
encoded_audio = convert_audio_to_base64(r'C:\Users\om\Desktop\FS\voi.wav')
print(encoded_audio)
