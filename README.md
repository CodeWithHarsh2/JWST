# Brown Dwarf Candidate Selection in the JWST COSMOS-Web Field

This repository contains the code used to identify brown dwarf candidates in the JWST COSMOS-Web survey using infrared colour–colour selection. The analysis follows the methodology presented in Chen et al. (2025) and reproduces a colour-colour diagram similar to Figure 2 of the paper.

---

## Overview

Brown dwarfs show strong molecular absorption features (H₂O and CH₄) in the near-infrared, which significantly affect the F277W band. These features make colour–colour selection an effective first step for identifying brown dwarf candidates in deep JWST surveys.

This project:
- Processes the COSMOS-Web master catalogue
- Computes NIRCam colours (F115W, F277W, F444W)
- Applies literature-based colour cuts
- Produces a publication-style colour–colour diagram

---

## Data

The analysis uses the **JWST COSMOS-Web 2025 master catalogue** (≈ 8.4 GB), which is not included in this repository.

Data can be downloaded from:  
https://cosmos2025.iap.fr/catalog.html

---

## Methodology

Brown dwarf candidates are selected using the following colour criteria (Chen et al. 2025):

- F277W − F444W > 0.9  
- F115W − F277W + 1 < F277W − F444W  

These cuts isolate sources with strong 2.7 μm molecular absorption characteristic of cool brown dwarfs.

---

## Results

Applying the colour selection to the full COSMOS-Web catalogue yields **4676 colour-selected brown dwarf candidates**. This number represents a conservative upper limit, as no morphological or point-source filtering is applied at this stage.

---

## Repository Structure

```text
.
├── data/raw/        # COSMOS-Web catalogue (not included)
├── figures/         # Output figure
├── output/          # Candidate catalogue
├── color_color_plot.py
└── README.md
