"""Descriptive statistics on observed product clicks (not impressions)."""
import pandas as pd
from .data import POSITIONS

def position_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return counts and click shares, preserving all six screen locations."""
    counts = df["location"].value_counts().reindex(range(1, 7), fill_value=0)
    total = counts.sum()
    shares = counts.to_numpy() / total * 100 if total else [0.0] * 6
    return pd.DataFrame({
        "location": counts.index,
        "position": [POSITIONS[i] for i in counts.index],
        "clicks": counts.to_numpy(),
        "share_pct": shares,
    })

def session_clicks(df: pd.DataFrame, session_id: int) -> pd.DataFrame:
    """Return one anonymous session in recorded click order."""
    return df.loc[df["session_id"] == session_id].sort_values("order").copy()
