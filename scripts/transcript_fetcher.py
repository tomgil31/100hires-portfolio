"""
transcript_fetcher.py

Purpose:
Download YouTube transcripts.

Author: Thomas Peterjohnjoseph
"""

from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    """
    Download transcript for a YouTube video.

    Parameters:
        video_id (str)

    Returns:
        list | None
    """

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        return transcript

    except Exception as error:
        print(f"Could not download transcript: {error}")
        return None