import re
result = "    pushfd\n"
a_original = []
a_path = []
f_original = open('eax_dx_original.txt')
for line in f_original.readlines():
    a_original.append(line)
f_path = open('eax_dx_path.txt')
for line in f_path.readlines():
    a_path.append(line)
for i in range(0,len(a_original)-1):
    if a_original[i]!=a_path[i]:
        original_crc = re.sub("^\s+|\n|\r|\s+$", '', a_original[i])[:re.sub("^\s+|\n|\r|\s+$", '', a_original[i]).index(";")]
        addr = re.sub("^\s+|\n|\r|\s+$", '', a_original[i])[re.sub("^\s+|\n|\r|\s+$", '', a_original[i]).index(";")+1:]
        path_crc = re.sub("^\s+|\n|\r|\s+$", '', a_path[i])[:re.sub("^\s+|\n|\r|\s+$", '', a_path[i]).index(";")]
        result += "    cmp eax, "+path_crc + "\n"
        result += "    jne short @next" + str(i) + "\n"
        result += "    cmp dx, "+addr + "\n"
        result += "    jne short @next" + str(i) + "\n"
        result += "    mov eax, " + original_crc + "\n"
        result += "    jmp @Exit" + "\n"
        result += "@next" + str(i) + ":" + "\n"
result += "@Exit:" + "\n"
result += "    ;Damaged instructions" + "\n"
result += "    popfd" + "\n"
result += "    jmp ret_addr" + "\n"
f = open("path_crc.asm","w")
f.write(result)
f.close
