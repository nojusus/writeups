Download the provided file "bobbytoesipad.png" and go to https://hexed.it. Search for the bytes FF E0. Skip 2 bytes and change the byte 63 to 10. Select 39 bytes after the changed byte, right click and "Delete selected bytes". Export the trailer bytes from FF D8 to FF D9 as a "JPG" file. The new image contains a string. Run the command
```bash
java -jar Stegsolve.jar
```
Open the file "bobbytoesipad.png" and look for another hidden string. Go to https://gchq.github.io/CyberChef and paste the string from the file "bobbytoesipad.png" into "Input". Add the operation "Vigenère Decode" and paste the string from the fixed "JPG" file into "Key" to get the flag.
