"""
ai_summary.py

Purpose:
Generate an AI summary from a YouTube transcript.

Author: Thomas Peterjohnjoseph
Project: 100Hires AI-Powered SEO Research
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_transcript(expert_name):
    """
    Read transcript and generate AI summary.
    """

    filename = expert_name.lower().replace(" ", "-") + "-transcript.md"

    transcript_path = Path("research/youtube-transcripts") / filename

    if not transcript_path.exists():
        print("Transcript not found!")
        return

    # Read transcript
    with open(transcript_path, "r", encoding="utf-8") as file:
        transcript = file.read()

    print("\nGenerating AI Summary...\n")

    prompt = f"""
You are an expert SEO Research Analyst.

Analyze the following YouTube transcript.

Return your answer in Markdown format.

Include these sections:

# Executive Summary

# Key SEO Insights

# AI Tools Mentioned

# Content Strategy

# Action Items

# Content Ideas

# Best Quotes

Transcript:

{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Save report
    output_folder = Path("research/reports")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / (
        expert_name.lower().replace(" ", "-") + "-report.md"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(response.text)

    print("=" * 60)
    print("AI REPORT GENERATED SUCCESSFULLY!")
    print("=" * 60)
    print(output_file)


def main():
    expert = input("Enter expert name: ")
    summarize_transcript(expert)


if __name__ == "__main__":
    main()