#!/bin/bash

set -e

jsonl="assembly_data_report.jsonl"
output_dir="all_longest_proteins"
mkdir -p "$output_dir"

# Create mapping from accession to species name
declare -A acc2species
while IFS=$'\t' read -r acc species; do
    acc2species["$acc"]="$species"
done < <(python3 extract_accession_to_species.py "$jsonl")

# Loop through each GCA_* folder
for dir in GC*; do
    if [[ -d "$dir" && -f "$dir/longest_proteins.faa" ]]; then
        acc=$(basename "$dir")
        species_name="${acc2species[$acc]}"
        if [[ -n "$species_name" ]]; then
            new_name="${species_name}.faa"
            cp "$dir/longest_proteins.faa" "$output_dir/$new_name"
            echo "Copied $dir/longest_proteins.faa -> $output_dir/$new_name"
        else
            echo "Warning: No species name found for $acc"
        fi
    fi
done
