#!/bin/bash

# Directory to store all renamed copies
output_dir="all_longest_proteins"
mkdir -p "$output_dir"

# Loop over all GCA_* folders
for dir in GC*; do
  if [[ -d "$dir" && -f "$dir/longest_proteins.faa" ]]; then
    # Set new filename based on directory name
    base_name=$(basename "$dir")
    new_name="longest_proteins_${base_name}.faa"

    # Copy and rename
    cp "$dir/longest_proteins.faa" "$output_dir/$new_name"
    echo "Copied $dir/longest_proteins.faa -> $output_dir/$new_name"
  else
    echo "Skipping $dir (missing longest_proteins.faa)"
  fi
done
