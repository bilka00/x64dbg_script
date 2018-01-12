from x64dbgpy.pluginsdk import *
import sys

f = open("eax_dx_original.txt","w")
f.write("")
f.close
for i in range(1,100):
	f = open("eax_dx_original.txt","a")
	f.write(str("0x"+format(register.GetEAX(), "x")) + ";" + str("0x"+format(register.GetDX(), "x")) + "\n")
	f.close
	debug.Run()
