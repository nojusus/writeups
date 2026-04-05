Download the provided file "inception.png". Scan the QR codes inside the image with this program:
```python
import cv2
import numpy as np
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode

img = "inception.png"
img_cv = cv2.imread(img)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
pil_img = Image.open(img)

small = cv2.resize(img_cv, None, fx=0.25, fy=0.25)
detector = cv2.QRCodeDetector()
outer_text, bbox, _ = detector.detectAndDecode(small)

pts = (bbox[0] * 4).astype(int)
x_start, y_start = pts[0][0], pts[0][1]
x_end,   y_end   = pts[2][0], pts[2][1]

modules = 21
mod_size = (x_end - x_start) / modules

chunks = []

for r in range(modules):
    for c in range(modules):
        x0 = x_start + int(c * mod_size)
        y0 = y_start + int(r * mod_size)
        x1 = x_start + int((c + 1) * mod_size)
        y1 = y_start + int((r + 1) * mod_size)

        cell = pil_img.crop((x0, y0, x1, y1))
        text = None

        for invert in [True, False]:
            for size in [400, 600, 800]:
                attempt = cell.convert("RGB")
                if invert:
                    attempt = ImageOps.invert(attempt)
                attempt = attempt.resize((size, size), Image.NEAREST)
                decoded = decode(attempt)
                if decoded:
                    text = decoded[0].data.decode('utf-8')
                    break
            if text:
                break

        if text:
            chunks.append((r, c, text))

message = ''.join(t for _, _, t in chunks)
print(message)
```
The program prints an encoded string. Go to https://base64.guru/converter/decode/image/png and convert the string into a "PNG" file. Scan the QR code to get the flag.
