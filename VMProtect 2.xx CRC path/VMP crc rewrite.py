from x64dbgpy.pluginsdk import *
import sys

f = open('eax_dx_original.txt')
for line in f.readlines():
	register.SetEAX(int(line[:line.index(";")], 0))
	debug.Run()
	