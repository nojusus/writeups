Download the provided file "Minions1.jpeg" and run the command
```bash
strings Minions1.jpeg | head -n 4 | tail -n 1
```
to get a password. Run the command
```bash
steghide extract -sf Minions1.jpeg
```
and enter the found password. A new file is extracted with an encoded string. Decode it with the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
