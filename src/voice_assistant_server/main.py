from src.voice_assistant_server.stt import STT
from src.voice_assistant_server.tts import TTS
from src.voice_assistant_server.va_server import VAServer


def main():
    stt = STT()
    tts = TTS()
    va_server = VAServer(tts_client=tts)
    while True:
        va_server.pub(stt.recognize())



if __name__ == "__main__":
    main()
