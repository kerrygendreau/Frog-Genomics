#!/usr/bin/env python3

import sys
from Bio import SeqIO

def get_genome_build(gtf_file):
    with open(gtf_file) as fin:
        for line in fin:
            if line.startswith("#!genome-build"):
                return line.strip().split(None, 1)[1]
    return None

if len(sys.argv) != 4:
    print("Usage: extract_longest_proteins_fasta.py protein.faa longest_proteins_per_gene.tsv genomic.gtf")
    sys.exit(1)

proteins_fasta = sys.argv[1]
longest_proteins_tsv = sys.argv[2]
gtf_file = sys.argv[3]

genome_build = get_genome_build(gtf_file)
if genome_build is None:
    print(f"Warning: genome-build not found in {gtf_file}, using default name")
    genome_build = "unknown_genome"

output_fasta = f"longest_proteins_{genome_build}.faa"
print(f"Output FASTA will be: {output_fasta}")

protein_ids_to_keep = set()
with open(longest_proteins_tsv) as fin:
    next(fin)  # skip header
    for line in fin:
        gene_id, protein_id, transcript_id, total_len = line.strip().split('\t')
        protein_ids_to_keep.add(protein_id)

print(f"Extracting {len(protein_ids_to_keep)} protein sequences...")

with open(output_fasta, "w") as fout:
    for record in SeqIO.parse(proteins_fasta, "fasta"):
        prot_id = record.id.split()[0]
        if prot_id in protein_
