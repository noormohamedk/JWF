from PIL import Image
import os

# Define paths
base_path = r"D:\Download"
logo_path = os.path.join(base_path, "jwf logo.jpeg")
shalik_path = os.path.join(base_path, "shalik.jpeg")
asha_path = os.path.join(base_path, "asha .jpeg")

# Load logo as background
logo = Image.open(logo_path)
print(f"Logo size: {logo.size}")

# Load person images
shalik = Image.open(shalik_path)
asha = Image.open(asha_path)
print(f"Shalik size: {shalik.size}")
print(f"Asha size: {asha.size}")

# Create composite images - person on logo background
target_size = (200, 200)

def create_composite(person_img, output_name, person_name):
    # Resize person image to fit
    person_resized = person_img.resize(target_size, Image.Resampling.LANCZOS)
    
    # Create logo background  
    logo_bg = logo.resize(target_size, Image.Resampling.LANCZOS)
    
    # Blend person image over logo (60% person, 40% logo)
    composite = Image.blend(logo_bg, person_resized, 0.65)
    
    # Save
    output_path = os.path.join(base_path, output_name)
    composite.save(output_path, quality=95)
    print(f"Created: {output_path}")

create_composite(shalik, "shalik_composite.jpeg", "Shalik")
create_composite(asha, "asha_composite.jpeg", "Asha")

print("\nComposite images created successfully!")
