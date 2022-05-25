#pragma once

void CALLBACK TimerProc(HWND, UINT, UINT_PTR id, DWORD current_time) {
    KillTimer(nullptr, id);

    LASTINPUTINFO lii;
    GetLastInputInfo(&lii);

    auto const time_since_last_input {current_time - lii.dwTime};

    if (time_since_last_input < IDLE_TIME) {
        auto const remaining_time {IDLE_TIME - time_since_last_input};
        SetTimer(nullptr, 0, remaining_time, &TimerProc);
    }
    else {
        SendLog(log, GetCurrentDate());
        SetTimer(nullptr, 0, IDLE_TIME, &TimerProc);
    }
}

DWORD WINAPI Waiter(LPVOID lParam) {
    SetTimer(nullptr, 0, 0, &TimerProc);

    MSG msg = {0};
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
