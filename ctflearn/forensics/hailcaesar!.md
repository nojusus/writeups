Download the provided file "HailCaesar.jpg" and run the command
```bash
file HailCaesar.jpg
```
The last comment is encrypted with a Caesar cipher. Decrypt it using this program:
```python
def decrypt(cipher_text, shift):
  result = ""
  for char in cipher_text:
    ascii_value = ord(char)
    if 32 <= ascii_value <= 126:
      normalized = ascii_value - 32
      shifted = (normalized - shift) % 95
      result += chr(shifted + 32)
    else:
      result += char
  return result

def brute_force(cipher_text):
  for shift in range(95):
    decrypted = decrypt(cipher_text, shift)
    print(f"Shift {shift:2}: {decrypted}")

cipher = input("Enter cipher text: ")
brute_force(cipher)
```
Paste the copied comment and go to Shift 18 to get the flag.
