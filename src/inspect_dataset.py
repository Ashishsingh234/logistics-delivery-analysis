"""Inspect a CSV dataset for the Week 1 logistics project.

Usage:
    python src/inspect_dataset.py data/your_file.csv
"""
import sys
from pathlib import Path
import pandas as pd


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/inspect_dataset.py path/to/file.csv")
        raise SystemExit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        raise SystemExit(1)

    df = pd.read_csv(file_path)
    print("\n--- Dataset overview ---")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")
    print("\n--- First 5 rows ---")
    print(df.head())
    print("\n--- Column types and non-null counts ---")
    df.info()
    print("\n--- Missing values by column ---")
    print(df.isna().sum().sort_values(ascending=False))
    print("\n--- Exact duplicate rows ---")
    print(int(df.duplicated().sum()))
    print("\nNote: Initial inspection only. Review the dataset schema before cleaning or calculating KPIs.")


if __name__ == "__main__":
    main()
