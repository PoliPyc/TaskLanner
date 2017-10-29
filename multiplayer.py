import socket
#import netifaces

class Multiplayer():
    def __init__(self):
        self.myIp = self.getMyIp()
        self.opponentIp = ""
        self.opponentPort = 0
        self.buffer = 1024
        self.socket = ""
        self.connection = ""

    #need to find a proper way
    def getMyIp(self):
        return socket.gethostname()

    def setOpponentIp(self, ip):
        self.opponentIp = ip

    def setOpponentPort(self, port = 6006):
        self.opponentPort = port

    def setNetGame(self):
        print("type opponent ip: ", end="")
        self.setOpponentIp(input())
        print("type opponent port [default = 6006]: ", end="")
        self.setOpponentPort(int(input() or 6006))

    def createServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.myIp, 6006))
        self.socket.listen(1)

    def joinServer(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.opponentIp, self.opponentPort))

    def setConnection(self):
        self.connection, addr = self.socket.accept()


    def sendPlace(self, x, y):
        coordinates = (x,y)
        self.connection.send(coordinates)

    def receivePlace(self):
        while True:
            coordinates = self.connection.recv(self.buffer)
            if not coordinates: break
            return coordinates


