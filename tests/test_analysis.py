"""Small controlled fixtures test the logic, not the dataset's empirical findings."""
import pandas as pd
from src.analysis import position_summary, session_clicks
from src.data import parse_csv

def test_position_summary_all_six():
    df = pd.DataFrame({"location": [1, 1, 6]})
    result = position_summary(df)
    assert result["clicks"].tolist() == [2, 0, 0, 0, 0, 1]
    assert round(result["share_pct"].sum(), 6) == 100.0

def test_empty_position_summary():
    result = position_summary(pd.DataFrame({"location": []}))
    assert result["clicks"].sum() == 0
    assert result["share_pct"].sum() == 0

def test_session_sorted():
    df = pd.DataFrame({"session_id": [7, 7, 8], "order": [2, 1, 1]})
    assert session_clicks(df, 7)["order"].tolist() == [1, 2]

def test_parse_csv():
    row = ["2008", "4", "1", "1", "29", "18817", "1", "A1", "1", "6", "1", "33", "1", "1"]
    header = ";".join("x" + str(i) for i in range(14))
    df = parse_csv((header + "\n" + ";".join(row) + "\n").encode())
    assert df.loc[0, "position_name"] == "Bottom right"
