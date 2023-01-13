from time import sleep
from json import dumps
from kafka import KafkaProducer


KAFKA_HOSTS = ['localhost:9092']
KAFKA_VERSION = (0, 10)
producer = KafkaProducer(bootstrap_servers=KAFKA_HOSTS, api_version=KAFKA_VERSION,
    value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    print("Sent : " + str(e))
    sleep(5)