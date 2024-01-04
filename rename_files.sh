#!/bin/bash

# Directory containing the .parquet files
DIRECTORY="data/20240101/fr"

# Change to the directory
cd "$DIRECTORY"

# Loop through all .parquet files and rename them
for file in *.parquet; do
    # Check if the file exists to avoid errors
    if [ -e "$file" ]; then
        mv "$file" "train-wikipedia-fr-$file"
    fi
done

echo "Renaming complete."
