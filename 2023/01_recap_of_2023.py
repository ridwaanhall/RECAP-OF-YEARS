# %%
import os
import time
import matplotlib.pyplot as plt

# %%
def text_2023(text, total_time=5.3):
    delay = total_time / len(text)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

text_to_type = "and with that the 2023 season comes to an end,\ngood night<3"
total_typing_time = 5.3

text_2023(text_to_type, total_typing_time)

# Get the absolute path to the image folder
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, "images")

# List of image filenames in the folder
image_filenames = ["image1.jpeg", "image2.jpeg", "image3.jpeg", "image4.jpeg", "image5.jpeg", "image6.jpeg", "image7.jpeg"]  # Add more filenames as needed

# Load and display each image with a delay
for image_filename in image_filenames:
    image_path = os.path.join(image_folder, image_filename)
    img = plt.imread(image_path)
    plt.imshow(img)
    plt.axis('off')  # Optional: Hide axis labels and ticks
    plt.show(block=False)  # Set block=False to allow plt.pause to work

    # Add a delay of 0.3 seconds between images
    plt.pause(0.3)

    # Clear the current figure to remove the displayed image
    plt.clf()

# Close the figure to ensure it's not left open
plt.close()
# %%
