from datetime import datetime

print("=" * 50)
print("100Hires Research Assistant")
print("=" * 50)

expert = input("Enter expert name: ")

filename = expert.lower().replace(" ", "-") + ".md"

content = f"""# {expert}

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

with open(f"research/experts/{filename}", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nSaved successfully to research/experts/{filename}")