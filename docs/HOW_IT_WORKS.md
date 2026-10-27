# How this GitHub-only project works (beginner guide)

**Goal:** Re-create one anonymous shopper's observed click sequence and visualize broader click patterns without claiming the positions caused the clicks.

## The big picture

```text
UCI original dataset (historical data)
             |
             v
src/data.py                <- read and label fields with pandas
             |
             v
src/analysis.py            <- calculate position counts and session order
             |
             v
scripts/build_site_data.py <- write aggregate JSON for a browser
             |
             v
docs/index.html + docs/site.js + docs/style.css
             |
             v
GitHub Actions -> GitHub Pages (your live portfolio website)
```

## What each tool does

- **GitHub repository** stores all version-controlled source files and records each commit.
- **GitHub Actions** provides a temporary computer to run Python during publishing.
- **GitHub Pages** serves the resulting HTML, CSS, JavaScript and JSON to visitors.
- **Python + pandas** read rows and summarize observed clicks.
- **HTML** provides the website sections and text.
- **CSS** controls typography, layout and mobile responsiveness.
- **JavaScript** loads the calculated JSON and responds to filter changes.
- **Jupyter Notebook** provides an explorable record of the analysis; GitHub displays notebook contents even if you never install Jupyter.

## What we have built so far

1. Created a website structure with story chapters based on Maya and the original storyboard.
2. Designed a screen-position grid and dynamic chart controls.
3. Wrote a script to compute JSON **from the authentic source**, not illustrative values.
4. Wrote a publishing workflow that attempts a fresh UCI download before deploying.
5. Added limitations and the original dataset attribution.

## Your job: activate Pages

1. Go to the GitHub repository and click **Settings**.
2. On the left, click **Pages**.
3. Under **Build and deployment**, choose **GitHub Actions** as the **Source**.
4. Click **Actions** at the top of the repository.
5. Open **Build and publish GitHub Pages story**; if no successful run appears, use **Run workflow**.
6. Verify a green check mark. If red, open the failed step and capture its message to debug.
7. Once published, open the URL shown in **Settings → Pages**.

## How we know the results are not invented

The numbers are calculated from original downloaded rows. The website never hardcodes observed counts or percentages. If the data build does not complete, the charts will not be presented as factual results.

## Questions to ask when you inspect the analysis

- What does one row represent?
- What does one session ID represent?
- How is a screen-location code mapped to a label?
- What is the denominator when we calculate click share?
- Why can't click share be called click-through rate?

## Next development stage

After confirming the workflow, we will review data-quality checks, compare monthly trends, examine transitions between clicks, and expand the explanation of each original storyboard frame.
