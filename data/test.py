from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyBUKiqE4FOE9bJZ7HCoh715DDz3SytoGGg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(title, options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=title,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            print(search_result["id"]["videoId"])


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()

    try:
        youtube_search("toy story (1995) trailer", args)
    except HttpError:
        print("An HTTP error %d occurred:\n%s")
