import socket
import pickle
# import netifaces

class Multiplayer():
    def __init__(self):
        self.myID = ""
        self.myIp = self.getMyIp()
        self.opponentIp = ""
        self.opponentPort = 0
        self.buffer = 1024
        self.socket = ""
        self.connection = ""

    def setMyID(self, id):
        self.myID = id

    # need to find a proper way
    def getMyIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = (s.getsockname()[0])
        s.close()
        return ip

    def setOpponentIp(self, ip):
        self.opponentIp = ip

    def setOpponentPort(self, port=6006):
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
        print("joined server")

    def setConnection(self):
        self.connection, addr = self.socket.accept()
        print("connected")

    def sendData(self, data):
        data = pickle.dumps(data)
        self.connection.send(data)

    def receiveData(self):
        while True:
            data = self.connection.recv(self.buffer)
            if not data: break
            return pickle.loads(data)
