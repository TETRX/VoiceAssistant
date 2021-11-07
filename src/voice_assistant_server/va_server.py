import paho.mqtt.client as mqtt
from ..config.network_config import QUERY_CHANNEL, ANSWER_CHANNEL, DEFAULT_BROKER
from .tts import TTS


class VAServer:
    def __init__(self, broadcast_channel=QUERY_CHANNEL, listen_channel=ANSWER_CHANNEL, broker=DEFAULT_BROKER,
                 client=mqtt.Client(), tts_client=TTS()):
        self.broadcast_channel = broadcast_channel
        self.listen_channel = listen_channel
        self.broker = broker
        self.tts_client = tts_client
        self.client = client
        self.init_client()

    def init_client(self):
        self.client.on_message = self.on_message
        connect_res = self.client.connect(self.broker)
        print(connect_res)

        self.client.subscribe(self.listen_channel)
        self.client.loop_start()

    def pub(self, msg):
        print("Publishing:", msg)
        self.client.publish(self.broadcast_channel, msg)

    def on_message(self, _, __, message):
        message = str(message.payload.decode("utf-8"))
        print("Got answer:", message)
        self.tts_client.say(message)
