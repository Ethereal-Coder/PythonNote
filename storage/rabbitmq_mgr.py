# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

import pika


class RabbitMQProduce(object):
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port, blocked_connection_timeout=300, socket_timeout=60))
        self.channel = self.connection.channel()
        # self.channel.exchange_declare(exchange='', exchange_type='')
        self.channel.queue_declare(queue=self.topic, durable=True)

    def message_sender(self, msg):
        self.channel.basic_publish(exchange='', routing_key=self.topic, body=msg, properties=pika.BasicProperties(delivery_mode=2))

    def close(self):
        self.connection.close()


download_producer = None


def mq_download_producer():
    global download_producer
    if download_producer is None:
        download_producer = RabbitMQProduce('localhost', 6783, 'download_mq_online')
