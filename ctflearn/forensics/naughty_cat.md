Download the provided file "cut3_c4t.png" and run the command
```bash
binwalk -e cut3_c4t.png
```
to extract hidden files. Run the command
```bash
audacity purrr_2.mp3
```
Turn on the Spectrogram mode to find a hidden string. Fix the broken file's "y0u_4r3.cl0s3.rar" header by going to https://hexed.it and changing the first 4 bytes to 52 61 72 21. Export the fixed file, extract it using the found hidden string as the password to get an encoded string. Decode it with the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
