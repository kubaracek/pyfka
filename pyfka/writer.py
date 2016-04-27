import kafka
import logging
from pyfka.utils import json_encode, str_encode

logger = logging.getLogger('pyfka')

class PyfkaWriter(object):
    def __init__(self, url):
        self.url = url

    def connect(self, topic = None, **kafka_args):
        kafka_args['bootstrap_servers'] = self.url

        if not 'value_serializer' in kafka_args:
            kafka_args['value_serializer'] = json_encode

        if not 'key_serializer' in kafka_args:
            kafka_args['key_serializer'] = str_encode

        self.topic = topic
        self.kafka_args = kafka_args

        try:
            print(kafka_args)
            self.producer = kafka.KafkaProducer(**kafka_args)
            logger.info('--> kafka connected')

        except kafka.common.NodeNotReadyError:
            logger.info('--> kafka reconnect')
            self.connect(topic=self.topic, **self.kafka_args)

        return self


    def close(self):
        self.producer.close()

    def reconnect(self):
        logger.info('--> kafka reconnect')
        self.connect(self.topic, self.kafka_args)

    def send(self, message, key = None, topic = None):
        t = topic or self.topic

        return self.producer.send(t, value=message, key=key)

    def flush(self):
        self.producer.flush()
