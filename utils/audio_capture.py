import pyaudio
import numpy as np
import sounddevice as sd
import config

class AudioStream:
    def __init__(self, source='speakers'):
        self.source = source
        self.rate = config.SAMPLE_RATE
        self.chunk = config.CHUNK_SIZE
        self.format = pyaudio.paInt16
        self.channels = 1
        
        if self.source == 'speakers':
            self.stream = sd.InputStream(
                samplerate=self.rate,
                blocksize=self.chunk,
                channels=self.channels,
                dtype=np.int16
            )
        else:
            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk
            )
    
    def listen(self):
        while True:
            if self.source == 'speakers':
                audio_chunk, _ = self.stream.read(self.chunk)
            else:
                audio_chunk = self.stream.read(self.chunk, exception_on_overflow=False)
            yield np.frombuffer(audio_chunk, dtype=np.int16)
    
    def close(self):
        if self.source == 'speakers':
            self.stream.stop()
        else:
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

if __name__ == "__main__":
    audio_stream = AudioStream(source=config.AUDIO_SOURCE)
    try:
        for chunk in audio_stream.listen():
            print(f"Получен аудиофрагмент размером {len(chunk)}")
    except KeyboardInterrupt:
        print("Завершение работы...")
        audio_stream.close()