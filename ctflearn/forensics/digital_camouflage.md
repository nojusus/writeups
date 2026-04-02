Download the provided "data.pcap" file and run the command
```bash
wireshark data.pcap
```
Search for a filter "http" and find the frame 105. Right click on the frame and go "Follow" > "TCP Stream". Type in "pswrd" inside "Find:" and copy the found string. Replace the string's tail from "%3D%3D" to "==" and decode it with the command
```bash
echo YourStringHere | base64 -d
```
to get the flag.
