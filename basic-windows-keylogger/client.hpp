#pragma once

SOCKET sock = INVALID_SOCKET;

bool initWinsock() {
    WSAData data;

    if (WSAStartup(MAKEWORD(2, 2), &data) != 0) {
        cerr << "Can't start Winsock." << endl;
        return false;
    }

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        cerr << "Can't create socket." << endl;
        WSACleanup();
        return false;
    }

    sockaddr_in hint;

    hint.sin_family = AF_INET;
    hint.sin_port = htons(PORT);
    hint.sin_addr.s_addr = inet_addr(SERVER_ADDR.c_str());

    if (connect(sock, (sockaddr*)&hint, sizeof(hint)) == -1) {
        cerr << "Connection gone wrong." << endl;
        closesocket(sock);
        WSACleanup();

        return false;
    }

    cout << "Connection was successful." << endl;

    return true;
}

void SendLog(string &msg, string timestamp_end) {
    if (msg.empty())
        return;

    if (!initWinsock())
        return;

    msg += "\r\n[" + timestamp_end + "]";

    if (send(sock, msg.c_str(), msg.length(), 0) == -1) cerr << "Can't send the log." << endl;
    else cout << "Just sent the log." << endl;

    msg.clear();

    closesocket(sock);
    WSACleanup();
}
