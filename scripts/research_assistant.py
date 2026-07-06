"""
research_assistant.py

Purpose:
Create a research template for an SEO expert.

Author: Thomas Peterjohnjoseph
Project: 100Hires AI-Powered SEO Research
"""

from pathlib import Path
from datetime import datetime


def research_expert(expert_name):
    """
    Create a markdown research template for an expert.
    """

    filename = expert_name.lower().replace(" ", "-") + ".md"

    output_folder = Path("research/experts")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / filename

    content = f"""# {expert_name}

## Research Date
{datetime.today().strftime("%Y-%m-%d")}

## Professional Profile

(To be completed)

## Current Role

(To be completed)

## Expertise

(To be completed)

## Why Selected

(To be completed)

## AI SEO Insights

(To be completed)
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Research file created: {output_file}")

    return str(output_file)


def main():
    print("=" * 60)
    print("100Hires Research Assistant")
    print("=" * 60)

    expert = input("Enter expert name: ")

    research_expert(expert)


if __name__ == "__main__":
    main()