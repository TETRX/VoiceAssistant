from src.voice_assistant_server.stt import STT
from src.voice_assistant_server.tts import TTS
from src.voice_assistant_server.va_server import VAServer
from src.config.network_config import DEFAULT_BROKER


def main(broker):
    stt = STT()
    tts = TTS()
    va_server = VAServer(tts_client=tts, broker=broker)
    while True:
        va_server.pub(stt.recognize())


if __name__ == "__main__":
    import sys
    broker = DEFAULT_BROKER
    if len(sys.argv) >= 2:
        broker = sys.argv[1]
    main(broker)
