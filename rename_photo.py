import os

# The path to your folder
folder_path = "static/img/robotic_camp"
prefix = "camp"

# Check if folder exists
if os.path.exists(folder_path):
    # Get all files in the directory
    files = os.listdir(folder_path)
    
    # Filter only image files (jpg, jpeg, png)
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort() # Sort them so they stay in order

    print(f"Found {len(images)} images. Renaming...")

    for i, filename in enumerate(images):
        # Get the file extension (e.g., .jpg)
        ext = os.path.splitext(filename)[1]
        
        # Create the new name: camp_1.jpg, camp_2.jpg, etc.
        new_name = f"{prefix}_{i+1}{ext}"
        
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

    print("Done! All photos renamed.")
else:
    print(f"Error: Folder '{folder_path}' not found. Make sure you created it!")