from PIL import Image, ImageDraw
import os

# Define paths
base_path = r"D:\Download"
logo_path = os.path.join(base_path, "jwf logo.jpeg")
shalik_path = os.path.join(base_path, "shalik.jpeg")
asha_path = os.path.join(base_path, "asha .jpeg")

# Load images
logo = Image.open(logo_path)
shalik = Image.open(shalik_path)
asha = Image.open(asha_path)

print(f"Logo size: {logo.size}")
print(f"Shalik size: {shalik.size}")
print(f"Asha size: {asha.size}")

# Target size for team cards
target_size = (250, 280)

def create_better_composite(person_img, output_name, person_name):
    """Create composite with person face prominent on JWF logo background"""
    
    # Create canvas with target size - white background
    canvas = Image.new('RGB', target_size, 'white')
    
    # Resize logo to fill the canvas
    logo_resized = logo.resize(target_size, Image.Resampling.LANCZOS)
    
    # Paste logo as background
    canvas.paste(logo_resized, (0, 0))
    
    # Resize person image to be larger (focus on upper body/face)
    # Make person image bigger to dominate the frame
    person_width = int(target_size[0] * 0.85)  # 85% of canvas width
    person_aspect = person_img.height / person_img.width
    person_height = int(person_width * person_aspect)
    person_resized = person_img.resize((person_width, person_height), Image.Resampling.LANCZOS)
    
    # Calculate position to center the person image horizontally
    # and position them slightly towards top (to show face better)
    x_pos = (target_size[0] - person_width) // 2
    y_pos = int(target_size[1] * 0.05)  # 5% from top
    
    # Create a mask for the person image (slight transparency at edges)
    person_with_alpha = person_resized.convert('RGBA')
    
    # Paste person on canvas
    canvas.paste(person_resized, (x_pos, y_pos))
    
    # Add subtle white frame/border effect
    draw = ImageDraw.Draw(canvas)
    border_width = 3
    border_color = (255, 255, 255)
    
    # Draw border around person area
    person_bbox = [x_pos - border_width, y_pos - border_width, 
                   x_pos + person_width + border_width, y_pos + person_height + border_width]
    draw.rectangle(person_bbox, outline=border_color, width=border_width)
    
    # Save composite
    output_path = os.path.join(base_path, output_name)
    canvas.save(output_path, quality=95)
    print(f"✓ Created: {output_name}")

# Create composites
create_better_composite(shalik, "shalik_composite.jpeg", "Shalik Ahamed N")
create_better_composite(asha, "asha_composite.jpeg", "Mohamed Ashali A")

print("\n✓ Composite images created successfully with better framing!")
