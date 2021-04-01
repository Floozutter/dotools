#SingleInstance Force
; https://superuser.com/a/429845
#=::
    WinGet, window, ID, A
    InputBox, width, winsize, width:, , 200, 150
    InputBox, height, winsize, height:, , 200, 150
    WinMove, ahk_id %window%, , , , width, height
return
