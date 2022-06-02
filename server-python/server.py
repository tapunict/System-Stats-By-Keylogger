import socket
import time
import csv


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def binding(self, n):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(n)

    def receive(self):
        (victim, address) = self.sock.accept()
        data = victim.recv(10240)
        return data.decode('utf8')

    def close(self):
        self.sock.close()


class CSV:
    def __init__(self):
        pass

    def __write__(self, path, row):
        with open(path, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def writeMetadata(self, uuid, window, timestampBegin, timestampEnd):
        self.__write__('csv/metadata.csv', [uuid, window, timestampBegin, timestampEnd])

    def writeLog(self, uuid, log):
        self.__write__('csv/logs.csv', [uuid, log])


class ExtractFeatures:
    def __init__(self, log):
        self.log = log.split("\r\n")

    def getUUID(self):
        uuid = self.log[0].split("] :: [")[0]
        return uuid[1:]

    def getWindow(self):
        firstPart = self.log[0].split("] :: [")[1]
        wnd = firstPart.split("] :: [")[0]
        return wnd

    def getTimestampBegin(self):
        tmp = self.log[0].split("] :: [")[2]
        return tmp[:-1]

    def getLogText(self):
        return self.log[1]

    def getTimestampEnd(self):
        return self.log[2][1:-1]
    

output = CSV()  
server = Server("0.0.0.0", 8800)

while True:
    try:
        server.binding(1)

    except Exception as e:
        print("Error on connecting:", e)
        time.sleep(45)
        continue

    break

while True:
    try:
        new_log = server.receive()
        fts = ExtractFeatures(new_log)
        
        output.writeMetadata(fts.getUUID(), fts.getWindow(), fts.getTimestampBegin(), fts.getTimestampEnd())
        output.writeLog(fts.getUUID(), fts.getLogText())

        print('\n')
        print(new_log, end='', flush=True)

        del fts

    except Exception as e:
        print("Error while receiving:", e)
        server.close()

        break

del server
del output
