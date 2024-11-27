Author: Naomi
CRISPRmap mito pilot data

Data storage:
Raw mitochondria images stored in cmap15_P1_B3A_tifs folder
Segmented mitochondria images stored in cmap15_P1_B3A_out folder
Cell data stored in mitocontrolset.csv
Cell name (matches with tif names)
Guide_ID = sgRNA guide (Single-guide RNA (sgRNA))
Gene = Gene sgRNA targets
The rest of the columns are data output from the mitochondria analysis I adapted from Mito Hacker pipeline https://www.nature.com/articles/s41598-020-75899-5

In current dataset:
579 cells with core fission gene KO identified for analysis (KO stands for knockout)
220 cells with core fusion gene KO identified for analysis
346 cells with non-targeting controls identified for analysis
1145 cells in total, which matches my data.

fission_genes = ['DNM1L', 'FIS1', 'MFF', 'MIEF1', 'MIEF2']
fusion_genes = ['OPA1', 'MFN1', 'MFN2']
nontargeting = [‘NTC’]

Notes:
So far, the segmented dataset only contains the mitochondria images the core fission and fusion genes, and nontargeting controls for ⅛ of the total dataset
- I can send DAPI (DAPI is a fluorescent stain that binds strongly to adenine–thymine-rich regions in DNA.), membrane stains as well if they would be useful
There are ~1000 more cells that have KOs in the same montage dataset with less well documented mitochondrial phenotypes that could be relatively easily sent as well
The rest of the dataset still needs a lot of processing


