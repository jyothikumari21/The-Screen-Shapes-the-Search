"""Descriptive summaries of observed clicks only."""
import pandas as pd
from .data import POSITIONS

def position_summary(df: pd.DataFrame) -> pd.DataFrame:
    counts = df['location'].value_counts().reindex(range(1,7),fill_value=0)
    total = counts.sum()
    return pd.DataFrame({'location': counts.index, 'position': [POSITIONS[i] for i in counts.index],
                         'clicks': counts.to_numpy(), 'share_pct': (counts.to_numpy()/total*100 if total else [0]*6)})

def session_clicks(df: pd.DataFrame, session_id: int) -> pd.DataFrame:
    return df[df['session_id'] == session_id].sort_values('order').copy()
