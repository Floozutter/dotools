#MaxThreadsPerHotkey 2

jumping := false
F1::
    jumping := !jumping
    while (jumping) {
        Send, {Space}
        Sleep, 1500
    }
return
