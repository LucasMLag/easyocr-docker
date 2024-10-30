import os
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['pt', 'en'])

# Define the input and output directories
base_dir = '/app'
input_dir = os.path.join(base_dir, 'input')
output_dir = os.path.join(base_dir, 'output')

# Creates output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the 'input' directory
for filename in os.listdir(input_dir):

    # Construct the full file path
    file_path = os.path.join(input_dir, filename)

     # Check if it is a file (and not a directory)
    if os.path.isfile(file_path):

        # Perform OCR on the image
        result = reader.readtext(file_path, detail=0, paragraph=True)

        # Save results to a text file with the same name as the image
        output_path = os.path.join(output_dir, f"{filename}.txt")
        with open(output_path, "w") as f:
            for text in result:
                f.write(text + "\n")
        print(f"Results for {filename} saved to {output_path}")