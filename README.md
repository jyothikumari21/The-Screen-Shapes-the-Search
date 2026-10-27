# The Screen Shapes the Search

**An independent human-centred clickstream analytics portfolio project by Jyothi Kumari.**

Explore what online shopping click records reveal about observed navigation, and what they do not reveal about why people click. An interactive Streamlit app links Maya, a fictional character based on anonymous session 18817, to the broader historical dataset.

## Questions

- Where were clicked products positioned on the page?
- How does the observed distribution vary across months and categories?
- How can we explore individual anonymous click sequences without inferring motivation?
- What further UX research would help improve product discovery?

## Data and attribution

[UCI Clickstream Data for Online Shopping](https://archive.ics.uci.edu/dataset/553/clickstream+data+for+online+shopping), DOI [10.24432/C5QK7X](https://doi.org/10.24432/C5QK7X); originally recorded in April–August 2008 at a maternity-clothing store, made available by UCI in 2019. Dataset credit: UCI Machine Learning Repository (CC BY 4.0). The original data is downloaded from UCI on first run and cached locally; it is not committed to the repository.

## Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS or Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Requires Python 3.10+ and an internet connection for the initial data download. If UCI is unreachable the app reports the error; it never silently uses synthetic records as research evidence.

## Test

```bash
python -m pytest -q
```

## Repository structure

- `app.py`: interactive storytelling and charts
- `src/data.py`: original-data loader and labels
- `src/analysis.py`: descriptive statistics
- `tests/`: deterministic unit tests
- `docs/METHODOLOGY.md`: interpretive rules and limitations
- `docs/ROADMAP.md`: next steps

## Important limitation

Recorded clicks are **not** impressions. Screen-position counts cannot establish click-through rates or the causal effect of product placement. We do not observe products shown but not clicked, motivations, conversion or sales. This is a historical, one-store dataset, not a representation of current e-commerce behaviour.

## Publish

Push this repository to GitHub, then create a Streamlit Community Cloud app with repository `jyothikumari21/The-Screen-Shapes-the-Search`, branch `main`, entry point `app.py`. Deployment requires the data source to be reachable.

## Project origins

The project builds on Jyothi Kumari's original storyboard and three design iterations. Canva and FigJam were used for those sketches; ChatGPT, Gemini and Claude supported ideation. This repository is an independent technical portfolio project, not the university assignment.
