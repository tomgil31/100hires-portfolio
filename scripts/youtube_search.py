"""
youtube_search.py

Purpose:
Search YouTube for videos related to an SEO expert.

Author: Thomas Peterjohnjoseph
Project: 100Hires AI-Powered SEO Research
"""

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

from markdown_writer import save_youtube_results, save_transcript
from transcript_fetcher import get_transcript

# Load environment variables
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


def search_youtube(expert_name):
    """
    Search YouTube for an expert.
    """

    print("=" * 50)
    print("YouTube Search Module")
    print("=" * 50)

    print(f"\nSearching YouTube for: {expert_name}\n")

    request = youtube.search().list(
        part="snippet",
        q=expert_name,
        type="video",
        maxResults=10
    )

    response = request.execute()

    videos = []
    first_video_id = None

    for index, item in enumerate(response["items"], start=1):

        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        published = item["snippet"]["publishedAt"]
        video_id = item.get("id", {}).get("videoId")

        if not video_id:
         continue

        # Save the first video's ID
        if first_video_id is None:
            first_video_id = video_id

        videos.append({
            "title": title,
            "channel": channel,
            "published": published,
            "link": f"https://www.youtube.com/watch?v={video_id}"
        })

        print(f"{index}. {title}")
        print(f"   Channel: {channel}")
        print(f"   Published: {published}")
        print(f"   Link: https://www.youtube.com/watch?v={video_id}")
        print()

    # Save video list
    saved_file = save_youtube_results(expert_name, videos)

    print("=" * 50)
    print("Markdown saved successfully!")
    print(saved_file)

    # Download transcript of first video
    if first_video_id:

        print("\nDownloading transcript...")

        transcript = get_transcript(first_video_id)

        if transcript:

            transcript_file = save_transcript(expert_name, transcript)

            print("Transcript saved successfully!")
            print(transcript_file)

        else:
            print("Transcript not available.")


def main():
    expert = input("Enter expert name: ")
    search_youtube(expert)


if __name__ == "__main__":
    main()