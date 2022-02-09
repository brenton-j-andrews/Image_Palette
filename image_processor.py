import numpy as np
from PIL import Image


def processor():
    image = np.array(Image.open("static/ginger.jpg"))
    flattened_image = image.reshape(-1, image.shape[2])
    pixel_values, indices, counts = np.unique(flattened_image, return_index=True, return_counts=True)

    indices = indices[0:10]

    extracted_colors = []

    for i in range(indices.size):
        extracted_colors.append(flattened_image[indices[i]])

    return extracted_colors
