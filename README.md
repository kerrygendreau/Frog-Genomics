
This repository contains code used to assess and compare publicly available whole genome sequences.

<p align="center">
<img width="200" height="280" src="IMG_3959.jpg">
</p>


# Assessing Genome Quality

We used [Merqury](https://github.com/marbl/merqury) for kmer based evaluation of assembly quality. While the *Dendrobates tinctorius* genome assembly [NCBI RefSeq assembly GCF_039654945.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_039654945.1/) has a high number of kmers mapping only once to the genome, many of the kmers present in the PacBio reads used to produce the *Allobates femoralis* assembly [NCBI submitted assembly GCA_033576535.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_033576535.1/) do not map to the genome assembly.

<p align="center">
  <img src="Dendrobates-merqury-out.GCF_039654945.1_ASM3965494v1_genomic.fna.gz.spectra-cn.fl.png" width="45%" />
  <img src="Allobates_merquery_orig_.fl.png" width="45%" />
</p>



Furthermore, the estimated error rates are much higher for the *Allobates* assembly.


| Species    | Error Rate   | QV Phred |
| -------- | ------- | ------- |
| *Allobates femoralis*  | 3.22e-4  | 34.9   |
| *Dendrobates tinctorius* | 2.14e-7  |  66.7  |


I will attempt to improve the *Allobates* assembly with gap filling and polishing.

# Filling Gaps with SAMBA

# Preparing Proteomes for Orthofinder

Amphibian proteomes were downloaded from NCBI using ncbi-datasets. I downloaded proteomes from reference genomes for all amphibians with annotations with the following code:

> datasets download genome taxon amphibia --reference --include protein,gtf,cds --annotated

By default, NCBI generates an individual folder per species labeled with their accession numbers.

I used custom python and bash codes:

[**bash loop to extract longest proteins**](extract_longest_proteins_all.sh) ; [**python code to identify longest proteins in genomic gtf**](list_longest_protein.py) ; [**python code to pull longest proteins from proteomes**](extract_proteins.py) to extract a single longest isoforms per gene from each proteome. 


In order to run the bash code, you need to have both of the python codes in the same folder. You also need to have Biopython installed and loaded.

I then renamed the files by species and put them all in a shared folder to give as an input to Orthofinder. [**bash loop to rename species**](rename_and_collect_by_species.sh) ; [**python code to rename species referencing the NCBI json report**](extract_accession_to_species.py).

The resulting filtered proteomes were used as inputs to Orthofinder.

