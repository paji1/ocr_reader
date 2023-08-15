import os
import cv2
import easyocr

reader = easyocr.Reader(['en'])

current_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = 'card.jpg'
image_path = os.path.join(current_dir, image_filename)

img = cv2.imread(image_path)

if img is None:
    print('Wrong path:', image_path)
else:
    # img_resized = cv2.resize(img, dsize=(1000, 700))
    results = reader.readtext(img)
    extracted_text = [result[1] for result in results]
    for text in extracted_text:
        print(text)
