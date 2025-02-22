import whisper
import numpy as np
import tempfile
import soundfile as sf

class SpeechToText:
    def __init__(self, model_size='base'):
        print("[Загрузка модели Whisper]")
        self.model = whisper.load_model(model_size)
    
    def transcribe(self, audio_chunk, rate=16000):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as temp_audio:
            sf.write(temp_audio.name, audio_chunk, rate)
            result = self.model.transcribe(temp_audio.name)
            return result['text'].strip() if result['text'] else ""

if __name__ == "__main__":
    stt = SpeechToText()
    test_audio = np.zeros(16000)  # Заглушка для теста
    print("Тестовое распознавание:", stt.transcribe(test_audio))
