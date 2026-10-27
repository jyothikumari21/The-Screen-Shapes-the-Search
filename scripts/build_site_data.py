"""Build small, transparent aggregates for the static GitHub Pages story.

Usage (from repository root):
    python scripts/build_site_data.py

This downloads the genuine source CSV using src.data.load_data, never uses
synthetic research data, and writes only aggregate results for browser display.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
from src.analysis import session_clicks
from src.data import load_data, POSITIONS

OUTPUT = Path("docs/data/summary.json")

def build_summary(df):
    required = ["month", "page_1_main_category", "location", "session_id", "order"]
    absent = [name for name in required if name not in df.columns]
    if absent:
        raise ValueError("Required source fields missing: " + ", ".join(absent))

    observed = df[df["location"].isin(list(POSITIONS))].copy()
    observed["category_code"] = observed["page_1_main_category"].astype(str)
    grouped = (
        observed.groupby(["month", "category_code", "location"], dropna=False)
        .size().reset_index(name="clicks")
    )
    counts = [
        {"month": int(row.month), "category": str(row.category_code),
         "location": int(row.location), "clicks": int(row.clicks)}
        for row in grouped.itertuples(index=False)
    ]

    maya = []
    for row in session_clicks(df, 18817).itertuples(index=False):
        price = None
        if row.price == row.price:  # Preserve missing values as JSON null
            price = float(row.price)
        maya.append({
            "order": int(row.order),
            "model": str(row.page_2_clothing_model),
            "category": str(row.page_1_main_category),
            "position": POSITIONS.get(row.location),
            "price": price,
        })
    return {
        "source": "https://doi.org/10.24432/C5QK7X",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_clicks": int(len(df)),
        "total_sessions": int(df["session_id"].nunique()),
        "unknown_location_count": int(len(df) - len(observed)),
        "months": sorted(int(value) for value in observed["month"].dropna().unique()),
        "categories": sorted(observed["category_code"].dropna().unique().tolist()),
        "counts": counts,
        "maya_session": maya,
    }

def main():
    df = load_data()
    summary = build_summary(df)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Built {OUTPUT} from {summary['total_clicks']:,} genuine click records.")

if __name__ == "__main__":
    main()
