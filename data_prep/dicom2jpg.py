import os
import glob
import pydicom
from PIL import Image
import numpy as np

def dicom_to_jpg(dicom_path, output_path):
    dicom_data = pydicom.dcmread(dicom_path)
    pixel_array = dicom_data.pixel_array

    # Normalize the pixel array to the range 0-255
    pixel_array = (pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array)) * 255
    pixel_array = pixel_array.astype(np.uint8)

    # Create an image from the pixel array
    image = Image.fromarray(pixel_array)
    image.save(output_path, format='JPEG')

# Define the root directory and output directory
root_dir = os.path.expanduser('~/data/vindr_mammo/vm1.0.0/images/')
output_dir = os.path.expanduser('~/finetune_llava_vindr/dataset/jpg_images/')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Find all .dicom files in the root directory and its subdirectories
dicom_files = glob.glob(os.path.join(root_dir, '**/*.dicom'), recursive=True)

for dicom_file in dicom_files:
    # Get the base name and replace the extension with .jpg
    base_name = os.path.basename(dicom_file)
    output_file = os.path.join(output_dir, base_name.replace('.dicom', '.jpg'))

    # Convert the DICOM file to JPEG
    #dicom_to_jpg(dicom_file, output_file)

    # Only convert if the JPEG file does not already exist
    if not os.path.exists(output_file):
        dicom_to_jpg(dicom_file, output_file)

print(f'Converted {len(dicom_files)} DICOM files to JPEG format.')

