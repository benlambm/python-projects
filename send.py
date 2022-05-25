import os
import sys
import time
import pika

def main():
    counter = 1
    while True:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body='My name is Ben Lamb and I love Python! #' + str(counter))
        print(f" [x] message #{counter} sent...")
        connection.close()
        time.sleep(1.0)
        counter += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)