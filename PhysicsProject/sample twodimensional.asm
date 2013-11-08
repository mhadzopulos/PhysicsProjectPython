

INCLUDE Irvine32.inc
Fib PROTO, num1:dword
.data
array1 byte 10,20,30,40,50
	   byte 60,70,80,90,75
	   byte 63,55,89,15,10
space byte " ",0
RowNumber DWORD 0
ColumnNumber DWORD 0
NumCols DWORD 5
.code
main PROC
mov eax,0
mov edx,0
mov ebx,0
mov ecx,0
mov ecx,3
mov esi,OFFSET array1
L1:
push ecx
mov ecx,NumCols
L2:
	mov eax,NumCols
	mul RowNumber
	mov ebx,eax
	mov esi,ColumnNumber
	mov al,array1[ebx+esi]
	call WriteInt
	mov edx,OFFSET space
	call WriteString
	inc ColumnNumber
loop L2
mov ColumnNumber,0
pop ecx
call CRLF
inc RowNumber
loop L1


exit
main ENDP


END main