"""Load historical UCI clickstream data. Keep the original CSV out of GitHub."""
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
import zipfile
import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/553/clickstream%2Bdata%2Bfor%2Bonline%2Bshopping.zip"
COLUMNS = ["year", "month", "day", "order", "country", "session_id",
           "page_1_main_category", "page_2_clothing_model", "colour", "location",
           "model_photography", "price", "price_2", "page"]
POSITIONS = {
    1: "Top left", 2: "Top middle", 3: "Top right",
    4: "Bottom left", 5: "Bottom middle", 6: "Bottom right",
}

def parse_csv(content: bytes) -> pd.DataFrame:
    """Parse the UCI semicolon-delimited original file with its fourteen fields."""
    df = pd.read_csv(BytesIO(content), sep=";", low_memory=False)
    if df.shape[1] != len(COLUMNS):
        raise ValueError(f"Expected {len(COLUMNS)} fields, found {df.shape[1]}")
    df.columns = COLUMNS
    for col in ["year", "month", "day", "order", "session_id", "location", "page", "price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["position_name"] = df["location"].map(POSITIONS)
    df["date"] = pd.to_datetime(df[["year", "month", "day"]], errors="coerce")
    return df

def load_data(cache_dir: str = "data") -> pd.DataFrame:
    """Download the official UCI ZIP once, then read its original CSV on later runs."""
    directory = Path(cache_dir)
    directory.mkdir(parents=True, exist_ok=True)
    csv_path = directory / "e-shop clothing 2008.csv"
    if not csv_path.exists():
        with urlopen(URL, timeout=45) as response:
            archive = response.read()
        with zipfile.ZipFile(BytesIO(archive)) as zf:
            names = [name for name in zf.namelist() if name.lower().endswith(".csv")]
            if not names:
                raise ValueError("Official UCI archive contains no CSV.")
            csv_path.write_bytes(zf.read(names[0]))
    return parse_csv(csv_path.read_bytes())
