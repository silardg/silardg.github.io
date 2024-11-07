#!/bin/bash

# Loop through all .webp files in the current directory
for file in *.webp; do
  # Temporary filename
  temp_file="${file%.webp}_temp.webp"

  # Use ImageMagick to strip metadata and save as a temporary file
  convert "$file" -strip "$temp_file"

  # Rename the temporary file back to the original filename
  mv "$temp_file" "$file"

  echo "Processed $file"
done

echo "All .webp images have been stripped of metadata."