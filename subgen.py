import speech_recognition as sr

def generate_subtitles(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        print("Processing audio file...")
        audio_data = recognizer.record(source)

    try:
        print("Transcribing audio...")
        subtitles = recognizer.recognize_google(audio_data)
        print("Subtitles generated successfully:\n")
        print(subtitles)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    audio_path = 'audio.wav'
    
    generate_subtitles(audio_path)