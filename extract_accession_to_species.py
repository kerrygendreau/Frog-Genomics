#!/usr/bin/env python3

import json
import sys

if len(sys.argv) != 2:
    print("Usage: extract_accession_to_species.py assembly_data_report.jsonl", file=sys.stderr)
    sys.exit(1)

jsonl_file = sys.argv[1]

with open(jsonl_file) as fin:
    for line in fin:
        data = json.loads(line)
        accession = data.get("accession")
        organism = data.get("organism", {}).get("organismName", "")
        if accession and organism:
            clean_name = organism.replace(" ", "_")
            print(f"{accession}\t{clean_name}")
