import kafka
import logging
from pyfka.utils import json_decode, str_decode

logger = logging.getLogger('pyfka')

class PyfkaReader(object):
    def __init__(self, url):
        self.url = url

    def connect(self, topic = None, **kafka_args):
        kafka_args['bootstrap_servers'] = self.url

        if not 'value_deserializer' in kafka_args:
            kafka_args['value_deserializer'] = json_decode

        if not 'key_deserializer' in kafka_args:
            kafka_args['key_deserializer'] = str_decode

        try:
            logger.info('--> ' + str(kafka_args))
            print(kafka_args)
            self.consumer = kafka.KafkaConsumer(topic, **kafka_args)
            logger.info('--> kafka connected')

        except kafka.common.NodeNotReadyError:
            logger.info('--> kafka reconnect')
            self.connect(topic)

        return self

    def close(self):
        self.consumer.close()

    def subscribe(self, topic):
        self.consumer.subscribe(topic)

        return self

    def receive(self, fn, key=None):
        for msg in self.consumer:
            try:
                if key is None or msg.key == key:
                    fn(msg.value, key=msg.key)
            except ValueError:
                logger.error('value error: ' + msg)
