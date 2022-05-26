#pragma once

void SaveNewUUID() {
    HKEY hkey;
    Uuid = GenerateUUID();

    RegCreateKeyEx(HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\TAP", 0L, nullptr, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS, nullptr, &hkey, nullptr);
    LONG res = RegOpenKeyEx(HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\TAP", 0, KEY_ALL_ACCESS, &hkey);

    if (res == ERROR_SUCCESS) RegSetValueEx(hkey, "UUID", 0, REG_SZ, (BYTE *)Uuid.c_str(), Uuid.length());
    RegCloseKey(hkey);
}

void ReadUUID() {
    HKEY hkey;
    LONG openRes = RegOpenKeyEx(HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\TAP", 0, KEY_ALL_ACCESS, &hkey);

    if (openRes != ERROR_SUCCESS) {
        SaveNewUUID();
        return;
    }

    TCHAR value[37];
    DWORD value_length = sizeof(value);
    LONG updateRes = RegQueryValueEx(hkey, "UUID", nullptr, nullptr, (LPBYTE)value, &value_length);

    RegCloseKey(hkey);

    if (updateRes == ERROR_SUCCESS) Uuid = value;
    else SaveNewUUID();
}

DWORD WINAPI SignIn(LPVOID lParam) {
    ReadUUID();
    cout << "Computer UUID: " << Uuid << endl;

    return 0;
}
