
def ascii1(): 
	led = """\
	|
	|
	|	
	|
	"""
	print (led)
def ascii2():
	led = """\
    --
      |
    --
   |
    --	
	"""
	print (led)
def ascii3():
	led = """\
    --
      |
    --
      |
    --	
	"""
	print (led)
def ascii4():
	led = """\
   |  |
    --
      |
      |	
	"""
	print (led)
def ascii5():
	led = """\
	 __
	|
	 --
	   |
	 --
	"""	
	print (led)
def ascii6():
	led = """\
	 __
	|
	|--
	|  |
	 --
	"""
	print (led)
def ascii7():
	led = """\
	 __
	   |
	 
	   |
	   |
	"""
	print (led)

def ascii8():
	led = """\
	 --
	|  |
	 --
	|  |
	 --
	"""
	print (led)
def ascii9():
	led = """\
	 --
	|  |
	 --
	   |
	 --
	"""
	print (led)
def ascii0():
	led = """\
	 --
	|  |
	|  |
	|  |
	 --
	"""
	print (led)

led = input("give a number (seperate by space)")
list(led)

if "1" in led:
	ascii1()
if "2" in led:
	ascii2()
if "3" in led:
	ascii3()
if "4" in led:
	ascii4()
if "5" in led:
	ascii5()
if "6" in led:
	ascii6()
if "7" in led:
	ascii7()
if "8" in led:
	ascii8()
if "9" in led:
	ascii9()
if "0" in led:
	ascii0()
