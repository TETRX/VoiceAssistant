import abc
import string
from abc import ABC

import paho.mqtt.client as mqtt

from src.config.network_config import QUERY_CHANNEL, ANSWER_CHANNEL


class VAModule(ABC):
    def __init__(self, broadcast_channel=ANSWER_CHANNEL, listen_channel=QUERY_CHANNEL, broker="127.0.0.1",
                 client=mqtt.Client()):
        self.broadcast_channel = broadcast_channel
        self.listen_channel = listen_channel
        self.broker = broker
        self.client = client
        self.init_client()

    def init_client(self):
        self.client.on_message = self.on_message

        def on_connect(client, userdata, flags, rc):
            client.subscribe(self.listen_channel)

        self.client.on_connect = on_connect

        self.client.connect(self.broker)

        self.client.loop_start()

    def on_message(self, client, userdata, message):
        query = str(message.payload.decode("utf-8"))
        print("Received:", query)
        answer = self.process_query(query)
        print("Answering", query, "with:", answer)
        self.client.publish(self.broadcast_channel, answer)

    @abc.abstractmethod
    def process_query(self, query: string) -> string:
        pass

    @classmethod
    def main(cls):
        module = cls()
        import time
        time.sleep(10000)  # TODO: better solution
