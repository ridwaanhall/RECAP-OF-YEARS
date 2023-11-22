# %%
import matplotlib.pyplot as plt
import os, time

# %%
# Get the absolute path to the image file
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, "images")
image_path1 = os.path.join(image_folder, "image1.jpeg")
image_path2 = os.path.join(image_folder, "image2.jpeg")

# Load and display the first image
img1 = plt.imread(image_path1)
plt.imshow(img1)
plt.axis('off')  # Optional: Hide axis labels and ticks
plt.show()

# Add a delay of 0.3 seconds
time.sleep(0.3)

# Load and display the second image
img2 = plt.imread(image_path2)
plt.imshow(img2)
plt.axis('off')  # Optional: Hide axis labels and ticks
plt.show()

# %%
