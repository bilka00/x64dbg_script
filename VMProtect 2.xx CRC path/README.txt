bp MapViewOfFile + 6 
ctrl+F9 (execute till return)
bpm *ax (eax, rax)
F9 (execute)
VM code patern: 

  INC *DX
  ...
  DEC [*BP]
  ...
  JNZ ... (JXX)
  ...
  MOV [*BP], *AX - CRC Save

  *AX - Hash *CX - Size *DX - Address.

Thank Julia 
