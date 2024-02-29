import os
import random
import shutil

# Define the source directory where the species folders are located
source_directory = "/users/Navneet/downloads/bee_wing_photos_isolated"

# Define the target directory where the bootstrapped images will be saved
target_directory = "/users/Navneet/downloads/bootstrap_samples"

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Number of bootstrap samples per species
num_samples = 100

# Valid image file extensions
valid_extensions = ('.png', '.jpg', '.jpeg')

# Loop through each species folder
for species_folder in os.listdir(source_directory):
    species_path = os.path.join(source_directory, species_folder)
    
    # Check if the path is indeed a directory
    if os.path.isdir(species_path):
        # Get a list of image files with valid extensions
        image_files = [f for f in os.listdir(species_path) 
                       if os.path.isfile(os.path.join(species_path, f)) and f.lower().endswith(valid_extensions)]
        
        # Create a target species folder
        target_species_folder = os.path.join(target_directory, species_folder)
        os.makedirs(target_species_folder, exist_ok=True)
        
        # Bootstrap sampling
        for i in range(num_samples):
            # Randomly choose an image file
            chosen_file = random.choice(image_files)
            original_file_path = os.path.join(species_path, chosen_file)
            bootstrapped_file_path = os.path.join(target_species_folder, f"{i}_{chosen_file}")
            
            # Copy the chosen image to the target bootstrap directory
            shutil.copyfile(original_file_path, bootstrapped_file_path)
