from PIL import Image, ImageFilter
import numpy as np
import os

# Base directory containing the bee wing photos
base_directory_path = '/users/Navneet/downloads/bootstrap_samples'

# Function to process images in a directory
def process_images_in_directory(directory_path):
    # New folder for processed photos within the given directory
    processed_photos_path = os.path.join(directory_path, 'processed_photos')
    if not os.path.exists(processed_photos_path):
        os.makedirs(processed_photos_path)

    # Get all files in the directory
    files = os.listdir(directory_path)

    # Process each image
    processed_images_paths = []
    for file in files:
        # Only process files that are photos
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, file)
            
            # Load the image
            original_image = Image.open(image_path)
            
            # Calculate the Gaussian Blur radius
            radius = np.mean([original_image.width/600, original_image.height/400]) / 2
            
            # Apply Gaussian Blur
            blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=radius))
            
            # Resize the image to 600x400
            resized_image = blurred_image.resize((600, 400))
            
            # Export the processed images
            processed_image_name = f'processed_{file}'
            processed_image_path = os.path.join(processed_photos_path, processed_image_name)
            resized_image.save(processed_image_path)
            
            # Add the processed image path to the list
            processed_images_paths.append(processed_image_path)
    
    return processed_images_paths

# Process images for each bee species directory
all_processed_images = {}
for species_folder in os.listdir(base_directory_path):
    species_folder_path = os.path.join(base_directory_path, species_folder)
    if os.path.isdir(species_folder_path):
        processed_images = process_images_in_directory(species_folder_path)
        all_processed_images[species_folder] = processed_images

# Print out all processed images paths for each species
for species, images in all_processed_images.items():
    print(f"{species}: {images}")
