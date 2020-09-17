X1 := 0
Y1 := 0
X2 := 0
Y2 := 0
X3 := 0
Y3 := 0
X4 := 0
Y4 := 0
X5 := 0
Y5 := 0

^1::
	MouseGetPos X1, Y1
return
^2::
	MouseGetPos X2, Y2
return
^3::
	MouseGetPos X3, Y3
return
^4::
	MouseGetPos X4, Y4
return
^5::
	MouseGetPos X5, Y5
return

1::
	MouseMove %X1%, %Y1%
	Click
return
2::
	MouseMove %X2%, %Y2%
	Click
return
3::
	MouseMove %X3%, %Y3%
	Click
return
4::
	MouseMove %X4%, %Y4%
	Click
return
5::
	MouseMove %X5%, %Y5%
	Click
return
