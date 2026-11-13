
from pathlib import Path

import pandas as pd


def analyze_csv(file_path: str) -> dict:
    """Read a CSV file and calculate dataset statistics."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("The input file must have a .csv extension.")

    df = pd.read_csv(path)

    report = {
        "file": path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "missing_values": {
            str(key): int(value)
            for key, value in df.isnull().sum().items()
        },
        "numeric_statistics": {},
    }

    numeric_columns = df.select_dtypes(include="number")

    for column in numeric_columns.columns:
        values = numeric_columns[column].dropna()

        if values.empty:
            report["numeric_statistics"][column] = None
            continue

        report["numeric_statistics"][column] = {
            "mean": float(values.mean()),
            "median": float(values.median()),
            "minimum": float(values.min()),
            "maximum": float(values.max()),
        }

    return report
