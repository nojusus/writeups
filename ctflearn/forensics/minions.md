Download the provided "Hey_You.png" file and run the command
```bash
binwalk Hey_You.png | grep https
```
to get a download link for another image. Run the command
```bash
binwalk -e Only_Few_Steps.jpg
```
to extract a third image. Run the command
```bash
strings YouWon(Almost).jpg | grep CTF
```
to get an encoded string. Keep decoding the string using the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
