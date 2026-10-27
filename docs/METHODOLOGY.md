# Methodology and responsible interpretation

## Source and unit of analysis

The source is [UCI Clickstream Data for Online Shopping](https://archive.ics.uci.edu/dataset/553/clickstream+data+for+online+shopping), DOI [10.24432/C5QK7X](https://doi.org/10.24432/C5QK7X), made available under CC BY 4.0. The observations were collected from one maternity-clothing e-commerce store in 2008.

Each row represents **one recorded product click**, not a product impression, unique visitor, purchase, or conversion. Session IDs identify anonymous sessions, not verified individual people.

## Processing

The original source CSV has fourteen semicolon-separated fields. `src/data.py` loads the file and assigns documented field names, converts numeric fields, derives a date and provides labels for screen position codes 1–6. The raw source data is not modified in place.

The six positions are: top left, top middle, top right, bottom left, bottom middle, bottom right. Click share is calculated as the number of clicks in a position divided by all clicks in the currently filtered data, multiplied by 100.

## Maya's story

Maya is a fictional narrative device. Her sequence is based on anonymous session ID 18817. We can trace recorded clicks by order, but **cannot reconstruct the unobserved interface, the products she saw but ignored, her intentions, or any completed transaction**.

## Interpretation safeguards

- Click share is not click-through rate; the denominator of impressions is missing.
- Comparisons between locations do not prove location caused clicks.
- The dataset lacks direct records of unseen products, actual visual attention, and purchases.
- The observations represent one store and are from 2008. Avoid presenting them as universal or current e-commerce behaviour.
- Filters and figures in this repository are descriptive, not causal or predictive.

## Future study design

A better test of the effect of product positioning would capture impression-level exposure, inventory, placement, page layout, click events and purchases, followed by a properly designed randomized experiment where feasible. Those data are *not* present here.
