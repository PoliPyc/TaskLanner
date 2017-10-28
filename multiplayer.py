import socket
#import netifaces

class Multiplayer():
    def __init__(self):
        self.myIp = self.getMyIp()
        self.opponentIp = ""
        self.opponentPort = 0
        self.buffer = 1024

    #need to find a proper way
    def getMyIp(self):
        pass

    def setOpponentIp(self, ip):
        self.opponentIp = ip

    def setOpponentPort(self, port):
        self.opponentPort = port

    def sendPlace(self, x, y):
        coordinates = (x,y)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.opponentIp, self.opponentPort))
        s.send(coordinates)
        data = s.recv(self.buffer)
        s.close()

    def receivePlace(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.opponentIp, self.opponentPort))
        s.listen(1)

        conn, addr = s.accept()
        print('Connection address: {}'.format(addr))
        while True:
            data = conn.recv(self.buffer)
            if not data: break
            print("received data: {}".format(data))

        conn.close()
        s.close()


