from x64dbgpy.pluginsdk import *
import sys

f_path = open("eax_dx_path.txt","w")
f_path.write("")
f_path.close
f_original = open('eax_dx_original.txt')
for line in f_original.readlines():
	f_path = open("eax_dx_path.txt","a")
	f_path.write(str("0x"+format(register.GetEAX(), "x")) + ";" + str("0x"+format(register.GetDX(), "x")) + "\n")
	f_path.close
	register.SetEAX(int(line[:line.index(";")], 0))
	debug.Run()
