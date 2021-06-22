#SingleInstance, Force

interfaceKeys := [1, 2, 3, 4, 5, 6]
switchDelay := 20
holdDelay := 20
waitDelay := 20

SetKeyDelay, -1
SetMouseDelay, -1

MButton::
    Loop, % interfaceKeys.Length() {
        Send, % interfaceKeys[A_Index]
        Sleep, % switchDelay
        Loop, 3 {
            Click, Down
            Sleep, % holdDelay
            Click, Up
            Sleep, % waitDelay
        }
    }
return
