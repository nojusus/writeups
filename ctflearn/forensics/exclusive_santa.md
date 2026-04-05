Download the provided file "Exclusive_Santa.rar" and run the command
```bash
binwalk -e Exclusive_Santa.rar
```
to extract hidden files. Run the command
```bash
foremost -i 3.png
```
to extract a hidden file "00000102.png". Run the command
```bash
java -jar Stegsolve.jar
```
Open the file "1.png", go to "Analyse" > "Image Combiner" and select the file "00000102.png". Save the new image and run the command
```bash
convert solved.bmp -flop output.png
```
to get the flag.
