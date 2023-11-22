# %%
import matplotlib.pyplot as plt
import os

# %%
# Get the absolute path to the image file
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, "images")
image_path = os.path.join(image_folder, "image1.jpeg")

# Load and display the image
img = plt.imread(image_path)
plt.imshow(img)
plt.axis('off')  # Optional: Hide axis labels and ticks
plt.show()

# %%
