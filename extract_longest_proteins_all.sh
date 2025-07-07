#!/bin/bash
# Run this in the parent directory containing all GCA_* folders


# Either run this in the same directory as the genome files or write in the full path in front of "GC*"
for dir in GC*; do
  if [ -d "$dir" ]; then
    echo "Processing $dir"
    cd "$dir" || exit

    # Run Python script to extract longest proteins per gene
    python3 list_longest_protein.py genomic.gtf longest_proteins_per_gene.tsv

    # Run Python script to extract longest protein sequences
    python3 extract_proteins.py protein.faa longest_proteins_per_gene.tsv genomic.gtf

    cd ..
  fi
done
