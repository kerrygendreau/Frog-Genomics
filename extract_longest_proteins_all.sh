#!/bin/bash

python_dir="/path/to/python/dir"

# Run this in the parent directory containing all GCA_* folders
for dir in GC*; do
  if [ -d "$dir" ]; then
    echo "Processing $dir"
    cd "$dir" || exit

    # Run Python script to extract longest proteins per gene
    python3 $python_dir/list_longest_protein.py genomic.gtf longest_proteins_per_gene.tsv

    # Run Python script to extract longest protein sequences
    python3 $python_dir/extract_proteins.py protein.faa longest_proteins_per_gene.tsv genomic.gtf

    cd ..
  fi
done
