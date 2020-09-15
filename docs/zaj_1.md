NWD(a,b)
	dopóki b != 0
		r = a mod b
		a = b
		b = r
	zwróć a
	
NWW = a*b/NWD(a,b)
