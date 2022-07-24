    #!/usr/bin/env python
    # Python Network Programming Cookbook,Second Edition -- Chapter - 1
    
    
import re
import socket
import sys
from urllib import response
import random
    
host = 'localhost'
data_payload = 2048
backlog = 5
port = 9900


# List of responses to be used in the chatbot
# list of places to travel
travel_destinations = ['Bali', 'Thailand', 'Shanghai', 'Nigra Falls' , 'Dallas']

# create a list of greeting words
greeting_words = ['hello', 'hi', 'greetings', 'sup', 'what\'s up', 'hey', 'hola']
# create a list of goodbye words
goodbye_words = ['bye', 'goodbye', 'see you later', 'cya', 'later', 'adios']

# looking for places to travel 
suggestion_words = ['where', 'where to', 'where to go', 'where to go to', 'where to go to']

#covid queries
covid_queries = ['covid', 'covidd 19', 'covid-19', 'coronavirus', 'coronavirus disease 19', 'coronavirus disease 19']

#thanking
thankyou_words = ['thank you', 'thanks', 'thank you very much', 'thank you so much', 'thank you so much for your help']


# function to select the response to be sent to the user according to the input matched with the list of words
def reply_selector (response_words):
    # check if any of the words in the response_words list is in the greeting_words list
    for word in response_words:
        if word in greeting_words:
            reply = b'Hello Human! I am a chatbot. I am here to help you find the best place to travel.'
        elif word in goodbye_words:
            reply = b'Goodbye Human!'
        elif word in suggestion_words:
            reply = b'You would love to go to ' + random.choice(travel_destinations)
        elif word in covid_queries:
            reply = b'I don\'t know what to say about COVID-19 but be sure to be vaccinated before traveling to any countries.'
        elif word in thankyou_words:
            reply = b'You are welcome! Is there anything else I can do for you?'
        else:
            reply = b'Sorry I don\'t understand what you said.'
    return reply
    
    
def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, 
                          socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, 
                      socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = ('localhost', 9900)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    while True: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(data_payload)
        # convert data to string
        data = data.decode('utf-8')
        print("Message Received form Human User: " + data)
        if data:
            data = data.lower()
            # print ("Data to Send to Client:" + data)
            # break the sentence into array of words
            response_words = data.split()
            response = reply_selector(response_words)
            print ("Sending to System: %s" %str(response))
            client.send(response)
        client.close() 
    
            # end connection
if __name__ == '__main__':
    #given_args = parser.parse_args() 
    port =9900
    echo_server(9900)
  

