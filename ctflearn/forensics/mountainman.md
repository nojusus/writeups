Download the provided file "MountainMan.jpg" and run the command
```bash
xxd MountainMan.jpg
```
Copy the bytes after the first FF D9 marker and go to https://gchq.github.io/CyberChef/. Paste the bytes into "Input". Add the operations "From Hex" and "XOR", and type in "cb" inside "Key" to get the flag.
