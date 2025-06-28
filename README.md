This repository contains code used to assess and compare publicly available whole genome sequences.

Amphibian proteomes were downloaded from NCBI using ncbi-datasets. I downloaded proteomes from reference genomes for all amphibians with annotations with the following code:

datasets download genome taxon amphibia --reference --include protein,gtf,cds --annotated

By default, NCBI generates an individual folder per species labeled with their accession numbers.

I used custom python and bash codes (**extract_longest_proteins_all.sh** ; **list_longest_protein.py** ; **extract_proteins.py**) to extract a single longest isoforms per gene from each proteome referencing the genomic.gtf file and then renamed the files by species (**rename_and_collect_by_species.sh** ; **extract_accession_to_species.py**), referencing the json report produced by ncbi-datasets.

The resulting filtered proteomes were used as inputs to Orthofinder.


![Phyllobates](IMG_5056.jpg =250x250)
