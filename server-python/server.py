import socket
import time
import csv

from threading import Thread


class CSV:
    def __init__(self):
        pass

    def __write__(self, path, row):
        with open(path, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def writeMetadata(self, uuid, window, timestampBegin, timestampEnd):
        self.__write__('metadata.csv', [uuid, window, timestampBegin, timestampEnd])

    def writeLog(self, uuid, log):
        self.__write__('logs.csv', [uuid, log])


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
    

class ClientThread:
    def __init__(self, victim):
        self.__conn = victim

    def __receive(self):
        data = self.__conn.recv(10240)
        return data.decode('utf8')

    def __consolePrint(self, new_log):
        print('\n')
        print(new_log, end='', flush=True)
        
    def __csvPrint(self, fts):
        output = CSV()
        output.writeMetadata(fts.getUUID(), fts.getWindow(), fts.getTimestampBegin(), fts.getTimestampEnd())
        output.writeLog(fts.getUUID(), fts.getLogText())
        del output

    def __processing(self, new_log):
        features = ExtractFeatures(new_log)
        self.__csvPrint(features)
        self.__consolePrint(new_log)
        del features
    
    def run(self):
        try:
            self.__processing(self.__receive())
            
        except Exception as e:
            print("Error while receiving:", e)
            self.__victim.close()


class Server:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def __createClientThread(self, conn):
        victim = ClientThread(conn)
        victim.run()

    def binding(self, n):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.__host, self.__port))
        self.sock.listen(n)

    def receive(self):
        while True:
            (victim, address) = self.sock.accept()
            Thread(target=self.__createClientThread, args=(victim,)).start()

    def close(self):
        self.sock.close()


server = Server("0.0.0.0", 8800)

while True:
    try:
        server.binding(16)

    except Exception as e:
        print("Error on connecting:", e)
        time.sleep(45)
        continue

    break

server.receive()
server.close()
