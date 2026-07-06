"""
markdown_writer.py

Purpose:
Create Markdown files for the 100Hires AI SEO Research project.

Author: Thomas Peterjohnjoseph
"""

from pathlib import Path


def save_youtube_results(expert_name, videos):
    """
    Save YouTube search results as a Markdown file.

    Parameters:
        expert_name (str): Name of the expert.
        videos (list): List of video dictionaries.

    Returns:
        str: Path of the saved file.
    """

    # Convert "Kevin Indig" → "kevin-indig"
    filename = expert_name.lower().replace(" ", "-") + "-videos.md"

    output_folder = Path("research/youtube-transcripts")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / filename

    with open(output_file, "w", encoding="utf-8") as file:

        file.write(f"# {expert_name} - YouTube Videos\n\n")

        for index, video in enumerate(videos, start=1):

            file.write(f"## {index}. {video['title']}\n\n")
            file.write(f"**Channel:** {video['channel']}\n\n")
            file.write(f"**Published:** {video['published']}\n\n")
            file.write(f"**Link:** {video['link']}\n\n")
            file.write("---\n\n")

    return str(output_file)
def save_transcript(expert_name, transcript):
    """
    Save a YouTube transcript as a Markdown file.
    """

    from pathlib import Path

    filename = expert_name.lower().replace(" ", "-") + "-transcript.md"

    output_folder = Path("research/youtube-transcripts")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / filename

    with open(output_file, "w", encoding="utf-8") as file:

        file.write(f"# {expert_name} - Transcript\n\n")

        for segment in transcript:
            file.write(segment.text + "\n")

    return str(output_file)