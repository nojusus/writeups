```python
with open("file.txt", "r") as f:
    read = f.read()

# Extract specific line to get the "flag"
flagLine = ""
for line in read.splitlines():
    if "flag" in line:
        flagLine = line.strip()
        print(flagLine)
        break

# Count occurences of the letter "A"
count = 0
for letter in read:
    if letter.upper() == "A":
        count += 1
print(f"\nThere are {count} A letters.")

# Reformat the found line into uppercase
print(f"\n{flagLine.upper()}")
```
