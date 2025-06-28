#!/usr/bin/env python3

import re
import sys
from collections import defaultdict, Counter

def get_attr_value(attrs, keys):
    for key in keys:
        m = re.search(rf'{key} "([^"]+)"', attrs)
        if m:
            return m.group(1)
    return "NA"

def detect_feature_type(gtf_file, features_to_check):
    """
    Detect which feature (from features_to_check) exists in the GTF file.
    Returns the first feature found.
    """
    feature_counts = Counter()
    with open(gtf_file) as fin:
        for line in fin:
            if line.startswith("#"):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 3:
                continue
            feature = fields[2]
            if feature in features_to_check:
                feature_counts[feature] += 1
            # Early exit if we found all features at least once
            if all(f in feature_counts for f in features_to_check):
                break
    for f in features_to_check:
        if feature_counts[f] > 0:
            return f
    return None

def main(gtf_file, output_file):
    # Features to try in order
    features_priority = ["CDS", "transcript"]
    
    chosen_feature = detect_feature_type(gtf_file, features_priority)
    if not chosen_feature:
        print(f"No features {features_priority} found in {gtf_file}. Exiting.")
        sys.exit(1)
    print(f"Using feature '{chosen_feature}' for length calculation.")

    lengths = defaultdict(int)
    transcripts = {}

    with open(gtf_file) as fin:
        for line in fin:
            if line.startswith("#"):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue

            feature = fields[2]
            if feature != chosen_feature:
                continue
            
            start = int(fields[3])
            end = int(fields[4])
            length = end - start + 1

            attrs = fields[8]

            # Attempt multiple attribute keys for gene, transcript, and protein IDs
            gene_id = get_attr_value(attrs, ["gene_id", "gene", "locus_tag"])
            transcript_id = get_attr_value(attrs, ["transcript_id", "transcript", "standard_name"])
            protein_id = get_attr_value(attrs, ["protein_id", "orig_protein_id", "product"])

            lengths[(gene_id, protein_id)] += length
            transcripts[(gene_id, protein_id)] = transcript_id

    # Find longest protein per gene
    longest_proteins = {}

    for (gene_id, protein_id), total_len in lengths.items():
        if gene_id not in longest_proteins or total_len > longest_proteins[gene_id][2]:
            longest_proteins[gene_id] = (protein_id, transcripts[(gene_id, protein_id)], total_len)

    with open(output_file, "w") as fout:
        fout.write("gene_id\tprotein_id\ttranscript_id\ttotal_length\n")
        for gene_id, (protein_id, transcript_id, total_len) in longest_proteins.items():
            fout.write(f"{gene_id}\t{protein_id}\t{transcript_id}\t{total_len}\n")

    print(f"Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: extract_longest_proteins_autodetect.py genomic.gtf output.tsv")
        sys.exit(1)
    gtf_file = sys.argv[1]
    output_file = sys.argv[2]
    main(gtf_file, output_file)
