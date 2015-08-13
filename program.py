
from sender import Sender
from receiver import Receiver

def main():
    sender = Sender()
    sender.connect('localhost')
    sender.create_queue('inbox')
    sender.send_message('inbox', 'Hello')
    sender.disconnect()

    receiver = Receiver()
    receiver.connect('localhost')
    receiver.receive('inbox')
    receiver.disconnect()


if __name__ == '__main__':
    main()
