# OliVR

Welcome to the Github page of the OliVR project (**Oli**gonucletide **V**erification for **R**esearch)

__This project is currently in active development__
## Background

The assessment of the sensitivity and specificy of molecular assays for the detection and subtyping of viruses can be complicated due to the fact that viruses, particularly single-stranded RNA viruses, have highly variable genomes and multiple subtypes that are sometimes difficult to characterize. Publicly available databases are being populated with many new sequences of whole genomes or fragments of genomes more rapidly than what traditional methods for design and evaluation of current primers and probes are keeping up with.

Although online tools like PrimerBLAST or GUI tools like CLC Workbench can be used to assess primers, the user will typically have to do more work in order to summarise or get more precise information from the large amount of raw data that these tools generate. 

## Objectives

The OliVR project aims to allow users do the following:

1. Assess the sensitivity and specificity of oligos from existing assays. This can be done for each oligo independently or for each primer pair to see how many amplicons will be generated.

2. Screen the NCBI databases and provide coverage data for taxonomical groups (e.g. what percent of Viridae is being covered, what perce 

3. The program will automatically update the databases being tested every certain amount of time. This could be daily, weekly, monthly, etc. This can be discussed as a group.

## Dependencies

This list is not definitive yet. Dependencies might be removed or new dependencies might be added as development progresses. but the dependencies that are being used are:

1. Python 3.4 or newer

2. The `dscp.pl` script for expanding degenerate bases. As a consequence, the `perl` language is also a dependency. I currently work with `perl 5, version 18, subversion 2`.

3. `e-PCR 2.3.9`: the standalone version of the NCBI software for prediction of PCR amplicons and primer binding. Very similar concept to `primerBLAST`

4. The `R` statistical computing language. I am currently working with `R 3.3.0 (2016-05-03)`

5. Depending on how I implement the evaluation, `bowtie` or `bwa` might be added to the pipeline.

6. NCBI taxonomy files will need to be downloaded. It is likely that a script to update them will need to be written as well.

## Ideas for the future

Enhancements to this project will be posted in the __Issues__ tab of this repository. In the meanwhile, these are some ideas that come to mind:

1. Integration with design methods (e.g. SigOli, PriMux, and in-house developed methods) so that design and evaluation become part of a modular process. This will allow users to design new assays and assess them vs. the databases. 

2. Incorporation of ThermoBLAST or IDT data (a bit harder to accomplish since these are proprietary tools, but I will see what I can do).
