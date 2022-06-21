import socket
import time
import csv

from threading import Thread


class CSV:
    def __init__(self):
        pass

    def __write(self, path, row):
        with open(path, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def writeMetadata(self, uuid, window, timestampBegin, timestampEnd, ipAddress):
        self.__write('/usr/app/server/csv/metadata.csv', [uuid, window, timestampBegin, timestampEnd, ipAddress])

    def writeLog(self, uuid, log):
        self.__write('/usr/app/server/csv/logs.csv', [uuid, log])


class ExtractFeatures:
    def __init__(self, log):
        self.__log = log.split("\r\n")

    def getUUID(self):
        uuid = self.__log[0].split("] :: [")[0]
        return uuid[1:]

    def getWindow(self):
        return self.__log[0].split("] :: [")[1]

    def getTimestampBegin(self):
        tmp = self.__log[0].split("] :: [")[2]
        return tmp[:-1]

    def getLogText(self):
        return self.__log[1]

    def getTimestampEnd(self):
        tmp = self.__log[2].split("] :: [")[0]
        return tmp[1:]
    
    def getIpAddress(self):
        ip = self.__log[2].split("] :: [")[1]
        return ip[:-1]
    

class ClientThread:
    def __init__(self, victim):
        self.__conn = victim
        self.__run()

    def __receive(self):
        try:
            data = self.__conn.recv(10240)
            self.__conn.close()
            return data.decode('utf8')

        except Exception as e:
            print("Error in receiving:", e)
            self.__conn.close()
            return None
            
    def __csvPrint(self, fts):
        output = CSV()
        output.writeMetadata(fts.getUUID(), fts.getWindow(), fts.getTimestampBegin(), fts.getTimestampEnd(), fts.getIpAddress())
        output.writeLog(fts.getUUID(), fts.getLogText())
        del output

    def __consolePrint(self, log):
        print('\n')
        print(log, flush=True)

    def __processing(self, new_log):
        features = ExtractFeatures(new_log)
        self.__consolePrint(new_log)
        self.__csvPrint(features)
        del features
    
    def __run(self):
        log = self.__receive()
        if log is not None: self.__processing(log)


class Server:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def binding(self, n):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind((self.__host, self.__port))
        self.__sock.listen(n)

    def listenAll(self):
        while True:
            (victim, address) = self.__sock.accept()
            Thread(target=ClientThread, args=(victim,)).start()

    def close(self):
        self.__sock.close()


NUM_OF_CLIENTS = 128
PORT = 8800

server = Server("0.0.0.0", PORT)

while True:
    try:
        server.binding(NUM_OF_CLIENTS)

    except Exception as e:
        print("Error on connecting:", e)
        time.sleep(45)
        continue

    break

server.listenAll()
server.close()