Download the provided file "Jakarta.jpg" and split the trailer into parts using this program:
```python
with open('Jakarta.jpg', 'rb') as f:
  jpg = f.read()

trailer = jpg[0xC41E1:]
parts = trailer.split(b'\xff\xd9')
parts = parts[:-1]

for i, part in enumerate(parts):
  filename = f'part{i}.bin'
  with open(filename, 'wb') as f:
    f.write(part)
```
Apply XOR using this program:
```python
with open('Jakarta.jpg', 'rb') as f:
  jpg = f.read()

with open('part0.bin', 'rb') as f:
  encrypted_key = f.read()

rsa_prefix = b'-----BEGIN RSA PRIVATE KEY-----'

xor_bytes = []
for i in range(len(rsa_prefix)):
  xor_bytes.append(rsa_prefix[i] ^ encrypted_key[i])

offset = jpg.find(bytes(xor_bytes))

rsa_key = bytearray()
for i in range(len(encrypted_key)):
  rsa_key.append(encrypted_key[i] ^ jpg[offset + i])

with open('jakarta_rsa.key', 'wb') as f:
  f.write(rsa_key)
```
Run the command
```bash
openssl rsautl -decrypt -inkey jakarta_rsa.key -in part3.bin -pkcs
```
to get the flag.
