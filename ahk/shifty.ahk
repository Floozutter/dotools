#SingleInstance Force
#MaxThreadsPerHotkey 2
delay := 25
shifting := false
F6::
    shifting := !shifting
    while (shifting) {
        Send, {Shift Down}
        Sleep, delay
        Send, {Shift Up}
        Sleep, delay
    }
    Send, {Shift Up}
return
