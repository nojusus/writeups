Download the provided file "TheVault.zip" and extract it. Go to https://hexed.it and open the file "Vault.jpg". Export the trailer after the FF D9 marker as a new image. Brute force the ROT cipher using this program:
```python
data = open('trailer.jpg', 'rb').read()

printable = [b for b in data if 32 <= b <= 126]

for shift in range(95):
  decoded = ""
  for b in printable:
    new = 32 + ((b - 32 - shift) % 95)
    decoded += chr(new)

  start = 0
  while True:
    idx = decoded.find("CTFlearn{", start)
    if idx == -1:
      break
    end_idx = decoded.find("}", idx)
    if end_idx != -1:
      flag = decoded[idx:end_idx+1]
      print(f"Shift {shift}: {flag}")
    start = idx + 1
```
to get the flag on Shift 17.
