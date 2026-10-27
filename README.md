# The Screen Shapes the Search

**An independent human-centred clickstream analytics and UX portfolio project by Jyothi Kumari.**

**A question:** When someone shops online, what can recorded clicks tell us about their journey through a designed screen — and what stays invisible?

This repository turns the original storyboard into a reproducible, public GitHub Pages data story. **No Streamlit account or server is needed.** Python is run by GitHub Actions, and a static website displays the results.

## 🌐 Project website

After GitHub Pages has been enabled, the website will be published at:

https://jyothikumari21.github.io/The-Screen-Shapes-the-Search/

The URL above is the intended address, **not yet confirmed as deployed**.

## The project in five steps

1. **Data:** `src/data.py` downloads the real [UCI Clickstream Data for Online Shopping](https://archive.ics.uci.edu/dataset/553/clickstream+data+for+online+shopping) dataset.
2. **Analysis:** `src/analysis.py` computes observed click distributions and anonymous session sequences.
3. **Prepare website data:** `scripts/build_site_data.py` writes small aggregate summaries (JSON) from the original records.
4. **Presentation:** `docs/index.html`, `docs/style.css` and `docs/site.js` present Maya's story and interactive charts.
5. **Publish:** `.github/workflows/pages.yml` runs the Python analysis and publishes the website using GitHub Actions + GitHub Pages.

Raw data is **not** uploaded to this repository. When the publishing workflow runs, its temporary build environment downloads the source and generates the chart data. No synthetic counts are shown as real findings.

## Publish using GitHub only — one-time settings

1. Open your repository's **Settings** tab.
2. Select **Pages** from the left sidebar.
3. Under **Build and deployment → Source**, select **GitHub Actions**.
4. Open the repository's **Actions** tab, select **Build and publish GitHub Pages story**, then click **Run workflow → Run workflow** (only if deployment did not run automatically).
5. Check whether the workflow completes successfully; if it fails, read the failed step's logs. Do not assume the data was fetched.
6. Return to **Settings → Pages** for the actual published URL.

[Learn more: GitHub Pages publishing settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## How to inspect the project

| File | Meaning |
|---|---|
| `notebooks/01_understanding_the_data.ipynb` | Beginner-friendly walkthrough of the variables and core exploration |
| `src/data.py` | Retrieve and validate the genuine source CSV |
| `src/analysis.py` | Convert click records to descriptive summaries |
| `scripts/build_site_data.py` | Prepare aggregate JSON for the website |
| `docs/index.html` | The story's text and structure |
| `docs/style.css` | The website's visual design |
| `docs/site.js` | Loads the JSON and updates charts when filters change |
| `.github/workflows/pages.yml` | Automates build and publication |
| `docs/METHODOLOGY.md` | Data limitations and decisions |
| `docs/ROADMAP.md` | Improvements still to complete |

See [HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md) for a line-by-line learning path.

## Source and research limitations

**Dataset:** *Clickstream Data for Online Shopping*, UCI Machine Learning Repository (2019), DOI [10.24432/C5QK7X](https://doi.org/10.24432/C5QK7X), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The dataset records 165,474 product clicks from one maternity-clothing e-commerce store in April–August 2008. Session 18817 is used as the basis for Maya's fictional narrative. Maya is **not an identifiable person**.

Click share is **not** click-through rate: the dataset does not include a complete record of product impressions, ignored products, user intent, purchases, or causal evidence about placement. See [methodology](docs/METHODOLOGY.md).

## Check the code

If you also have Python on your computer, you can run:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m scripts.build_site_data
```

Local execution is optional; GitHub Actions does the data build for the deployed website.

## Project origins

The project expands Jyothi's original story, *The Screen Shapes the Search*, with an independent implementation. Canva and FigJam were used in storyboard drafts, and ChatGPT, Gemini and Claude supported ideation. This is a portfolio project, **not an assignment submission**.
