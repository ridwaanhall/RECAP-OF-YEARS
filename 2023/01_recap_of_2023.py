# %%
import os
import time
from PIL import Image

# %%
def type_with_total_time(text, total_time=5.3):
    delay = total_time / len(text)

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def display_image_with_delay(image_path, delay=0.3):
    image = Image.open(image_path)
    image.show()
    time.sleep(delay)

text_to_type = "and with that the 2023 season"
total_typing_time = 3.5

type_with_total_time(text_to_type, total_typing_time)

image_folder = "2023/images"
image_path1 = os.path.join(image_folder, "image1.jpeg")
display_image_with_delay(image_path1)

image_path2 = os.path.join(image_folder, "image2.jpeg")
display_image_with_delay(image_path2)
