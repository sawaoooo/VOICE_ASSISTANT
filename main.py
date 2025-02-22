import threading
from utils.audio_capture import AudioStream
from utils.speech_to_text import SpeechToText
from utils.text_analyzer import TextAnalyzer
from utils.gui import run_gui, MainWindow
import config

def process_audio(window):
    audio_stream = AudioStream(source=config.AUDIO_SOURCE)
    speech_to_text = SpeechToText()
    text_analyzer = TextAnalyzer()
    
    for audio_chunk in audio_stream.listen():
        text = speech_to_text.transcribe(audio_chunk)
        if text:
            response = text_analyzer.analyze_and_respond(text)
            window.update_text(f"\nРаспознанный текст: {text}")
            window.update_text(f"Ответ бота: {response}")

def main():
    def start_processing(window):
        audio_thread = threading.Thread(target=process_audio, args=(window,))
        audio_thread.start()

    run_gui(start_processing)

if __name__ == "__main__":
    main()
