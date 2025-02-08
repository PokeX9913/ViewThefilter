
from PIL import Image
import os

def process_images(input_dir, output_dir, convert_to="PNG"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(input_dir, filename)
            try:
                with Image.open(file_path) as img:
                    print(f"Processing: {filename}")
                    img.show()  # Display the image
                    output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.{convert_to.lower()}")
                    img.save(output_file, convert_to)
                    print(f"Saved converted image to: {output_file}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "c:/Users/mario/Downloads/ABDM/Wallapapers/"  # Replace with your input directory
    output_directory = "c:/Users/mario/Downloads/ABDM/Wallapapers/"  # Replace with your output directory
    process_images(input_directory, output_directory)
    import os

# Specify the directory path
new_directory = "c:/Users/mario/Downloads/ABDM/Wallpapers"

# Create the directory
os.makedirs(new_directory, exist_ok=True)  # 'exist_ok=True' avoids error if the directory already exists

print(f"Directory created: {new_directory}")
import os

directory = "c:/Users/mario/Downloads/ABDM/Wallapapers/"

# List all files and directories in the specified path
files = os.listdir(directory)

# Print the list of files
for file in files:
    print(file)
    from PIL import Image

# Specify the path to the image
image_path = "c:/Users/mario/Downloads/ABDM/Wallapapers/xx.png"

# Open the image
img = Image.open(image_path)

# Display the image
img.show()

# Optionally, print image details
print(f"Image format: {img.format}")
print(f"Image size: {img.size}")
print(f"Image mode: {img.mode}")
from PIL import Image, ImageFilter

# Open an image
image_path = "c:/Users/mario/Downloads/ABDM/Documents/xx.png"
image = Image.open(image_path)

# Example manipulations
# Resize the image
resized_image = image.resize((200, 200))

# Apply a filter (e.g., BLUR)
blurred_image = image.filter(ImageFilter.BLUR)

# Convert to grayscale
grayscale_image = image.convert("L")

# Save the manipulated image
output_path = "c:/Users/mario/Downloads/ABDM/Documents/xx.png"
grayscale_image.save(output_path)

print(f"Image manipulated and saved to {output_path}")