"""
main.py

Purpose:
Run the complete AI-Powered SEO Research pipeline.

Author: Thomas Peterjohnjoseph
Project: 100Hires AI-Powered SEO Research
"""

from research_assistant import research_expert
from youtube_search import search_youtube
from analyze_transcript import analyze_transcript
from ai_summary import summarize_transcript


def main():

    print("=" * 60)
    print("100Hires AI-Powered SEO Research Assistant")
    print("=" * 60)

    expert = input("\nEnter SEO Expert Name: ")

    print("\nSTEP 1/4 - Researching expert...")
    research_expert(expert)

    print("\nSTEP 2/4 - Searching YouTube...")
    search_youtube(expert)

    print("\nSTEP 3/4 - Analyzing transcript...")
    analyze_transcript(expert)

    print("\nSTEP 4/4 - Generating AI report...")
    summarize_transcript(expert)

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    print("\nGenerated Files:")

    print(f"research/experts/{expert.lower().replace(' ','-')}.md")
    print(f"research/youtube-transcripts/{expert.lower().replace(' ','-')}-transcript.md")
    print(f"research/analysis/{expert.lower().replace(' ','-')}-analysis.md")
    print(f"research/reports/{expert.lower().replace(' ','-')}-report.md")


if __name__ == "__main__":
    main()