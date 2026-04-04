Download the provided file "CTFLearn.zip" and extract it to get 2 files. Use this python program:
```python
import sys

file1 = bytearray(open(sys.argv[1], 'rb').read())
file2 = bytearray(open(sys.argv[2], 'rb').read())

size = len(file1) if len(file1) < len(file2) else len(file2)
xord = bytearray(size)

for i in range(size):
	xord[i] = file1[i] ^ file2[i]
	
open(sys.argv[3], 'wb').write(xord)
```
and run the command
```bash
python3 xor.py CTFLearn.pdf CTFLearn.txt output.pdf
```
to get the flag.
