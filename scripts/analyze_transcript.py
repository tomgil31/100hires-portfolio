"""
analyze_transcript.py

Purpose:
Analyze a YouTube transcript and generate a basic report.

Author: Thomas Peterjohnjoseph
Project: 100Hires AI-Powered SEO Research
"""

from pathlib import Path
import re


def analyze_transcript(expert_name):
    """
    Analyze a transcript and save a markdown report.
    """

    filename = expert_name.lower().replace(" ", "-") + "-transcript.md"

    transcript_file = Path("research/youtube-transcripts") / filename

    if not transcript_file.exists():
        print("❌ Transcript file not found!")
        return

    print(f"\nReading: {transcript_file}")

    with open(transcript_file, "r", encoding="utf-8") as file:
        content = file.read()

    words = re.findall(r"\b[a-zA-Z]+\b", content.lower())

    word_count = len(words)
    line_count = len(content.splitlines())

    keywords = [
        "seo",
        "google",
        "ai",
        "content",
        "search",
        "ranking",
        "traffic",
        "keyword",
        "llm",
        "brand"
    ]

    keyword_counts = {}

    print("\nKeyword Frequency")
    print("-" * 30)

    for keyword in keywords:
        count = words.count(keyword)
        keyword_counts[keyword] = count
        print(f"{keyword:<10}: {count}")

    output_folder = Path("research/analysis")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / (
        expert_name.lower().replace(" ", "-") + "-analysis.md"
    )

    with open(output_file, "w", encoding="utf-8") as report:

        report.write(f"# {expert_name} - Transcript Analysis\n\n")

        report.write("## Statistics\n\n")
        report.write(f"- Total Words: **{word_count}**\n")
        report.write(f"- Total Lines: **{line_count}**\n\n")

        report.write("## Keyword Frequency\n\n")
        report.write("| Keyword | Count |\n")
        report.write("|---------|------:|\n")

        for keyword, count in keyword_counts.items():
            report.write(f"| {keyword} | {count} |\n")

    print("\n✅ Analysis report saved successfully!")
    print(output_file)


def main():
    expert = input("Enter expert name: ")
    analyze_transcript(expert)


if __name__ == "__main__":
    main()