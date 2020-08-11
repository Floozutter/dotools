^j::
	Click % GetKeyState("LButton") ? "up" : "down"
return

^k::
	Click % "right, " (GetKeyState("RButton") ? "up" : "down")
return
