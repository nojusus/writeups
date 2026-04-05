Download the provided file "ShahOfGimli.jpg" and run the command
```bash
binwalk -e ShahOfGimli.jpg
```
Extract the file "20517" and run the command
```bash
sha256sum Gimli04Base.jpg
```
Run the command
```bash
openssl enc -d -aes-256-cbc -iv 00000000000000000000000000000000 -K YourFoundString -in flag.enc -out flag.txt
```
to get the flag.
