The downloaded gif file cannot be opened. Analyzing the file with HexEd, it becomes apparent the header is missing. Select the first byte of the file > right click > Insert Bytes Here... > Insert 4 new bytes. Type in 47 49 46 38, so the header becomes GIF89a. Save the fixed gif file and open it. The file contains a base64 encoded string that can be decoded with the command
```bash
echo "ZmxhZ3tnMWZfb3JfajFmfQ==" | base64 -d
```
to reveal the flag.
