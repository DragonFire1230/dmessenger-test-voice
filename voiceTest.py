#!/usr/bin/python3

recieveBytes = 2048

import socket
import threading

class Server:
    def __init__(self):
            self.ip = socket.gethostbyname(socket.gethostname())
            while 1:
                try:
                    self.port = 7002

                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.bind((self.ip, self.port))

                    break
                except:
                    print("[Error] Couldn't bind to that port")

            self.connections = []
            self.accept_connections()

    def accept_connections(self):
        self.s.listen(100)

        print('[Info] Running on IP: '+self.ip)
        print('[Info] Running on port: '+str(self.port))
        
        while True:
            c, addr = self.s.accept()

            print(Back.GREEN + f'[Connect] Connected: {addr}')

            self.connections.append(c)

            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
        
    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.s and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self,c,addr):
        while 1:
            try:
                data = c.recv(recieveBytes)
                self.broadcast(c, data)
            
            except socket.error:
                c.close()

server = Server()