from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data" / "products.csv"
OUT = ROOT / "outputs"


def make_tags(row: dict[str, str]) -> str:
    words = [row["category"], row["style"], row["audience"], row["product_name"].lower()]
    tags = []
    for item in words:
        tags.extend(part.strip() for part in item.replace("-", " ").split() if len(part.strip()) > 2)
    return ", ".join(list(dict.fromkeys(tags))[:13])


def main() -> None:
    OUT.mkdir(exist_ok=True)
    products = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    listings: list[dict[str, str]] = []
    qa_lines = ["# QA Report", ""]

    for row in products:
        title = f"{row['style'].title()} {row['product_name']} for {row['audience'].title()}"
        description = (
            f"{row['product_name']} is a {row['category']} built for {row['audience']}. "
            f"It includes {row['features'].replace(';', ',')} and is prepared as a review-ready listing draft."
        )
        tags = make_tags(row)
        checks = {
            "title_under_140": len(title) <= 140,
            "has_price": bool(row["price"]),
            "has_tags": bool(tags),
            "human_review_required": True,
        }
        listings.append({**row, "generated_title": title, "description": description, "tags": tags})
        qa_lines.extend([f"## {row['product_name']}", *[f"- {key}: {value}" for key, value in checks.items()], ""])

    with (OUT / "generated_listings.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(listings[0].keys()))
        writer.writeheader()
        writer.writerows(listings)
    (OUT / "qa_report.md").write_text("\n".join(qa_lines), encoding="utf-8")
    print("Wrote generated_listings.csv and qa_report.md")


if __name__ == "__main__":
    main()
