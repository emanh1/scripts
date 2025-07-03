#!/bin/bash

# Prompt for filenames
read -p "Enter file names (separated by space): " -a filenames

# Loop through each filename and create the file
for file in "${filenames[@]}"; do
    echo "Generating $file with 1MB of random data..."
    head -c 500k /dev/urandom > "$file"
    echo "$file created."
done

echo "All files generated."
