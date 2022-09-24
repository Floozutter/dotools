SetBatchLines, -1
SetKeyDelay, 25

F1::
    while (GetKeyState("F1", "P")) {
        Send, {e down}
        Send, {e up}
    }
return

F2::
    while (GetKeyState("F2", "P")) {
        Send, {e down}
        Send, {e up}
        Send, {Right down}
        Send, {Right up}
    }
return
