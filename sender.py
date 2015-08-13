
import pika

class Sender(object):

    """Docstring for Sender. """

    def __init__(self):
        """TODO: to be defined1. """
        self.connection = None
        self.channel = None

    def connect(self, host):
        """TODO: Docstring for connection.

        :host: TODO
        :returns: TODO

        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()

    def create_queue(self, queue_name):
        """TODO: Docstring for create_queue.

        :queue_name: TODO
        :returns: TODO

        """
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print "message sent successfully"

    def disconnect(self):
        self.connection.close()


