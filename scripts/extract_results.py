"""Extract the model accuracy summary from the notebook's saved outputs."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "ICIST-70_30(MM).ipynb"
OUTPUT = ROOT / "results" / "metrics.csv"
CELLS = {
    "KNN": (15, 18),
    "Random forest": (27, 29),
    "MLP": (38, 40),
    "SVM (linear)": (49, 51),
    "XGBoost": (60, 62),
}


def output_text(cell: dict) -> str:
    return "\n".join(
        "".join(output["text"]) if isinstance(output["text"], list) else output["text"]
        for output in cell.get("outputs", [])
        if "text" in output
    )


def value(pattern: str, text: str) -> str:
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        raise ValueError(f"Missing result matching {pattern}")
    return match.group(1)


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    rows = []
    for model, (train_index, test_index) in CELLS.items():
        train = output_text(notebook["cells"][train_index])
        test = output_text(notebook["cells"][test_index])
        rows.append({
            "model": model,
            "training_cv_accuracy": value(r"Best Cross-Validation Accuracy:\s*([0-9.]+)", train),
            "test_accuracy": value(r"Testing Accuracy(?: \(XGBoost\))?:\s*([0-9.]+)", test),
            "training_n": "707",
            "test_n": "303",
        })
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
