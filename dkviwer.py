import requests
import sys
import time
import random
from urllib.parse import urlparse, parse_qs

# Basic headers to make requests appear as if they are coming from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.youtube.com',
    'Accept-Language': 'en-US,en;q=0.9',
}

# YouTube video watch URL pattern
watch_url = "https://www.youtube.com/watch?v="

def increase_views(video_url, num_views=100):
    """ Simulate view increase by sending multiple requests """
    
    # Parse video ID from the URL
    parsed_url = urlparse(video_url)
    video_id = parse_qs(parsed_url.query).get("v")[0]
    if not video_id:
        print(f"Invalid YouTube URL: {video_url}")
        return
    
    print(f"Starting to increase views for video: {video_url}")
    
    for i in range(num_views):
        # Simulate a view by sending GET requests to YouTube
        response = requests.get(watch_url + video_id, headers=headers)
        
        if response.status_code == 200:
            print(f"[{i+1}] Successfully simulated view for {video_url}")
        else:
            print(f"[{i+1}] Failed to simulate view. Status code: {response.status_code}")
        
        # Sleep randomly between 5 and 30 seconds to simulate human-like behavior
        sleep_time = random.randint(5, 30)
        print(f"Sleeping for {sleep_time} seconds before next view...")
        time.sleep(sleep_time)

    print("Finished simulating views.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dkviews.py <youtube_video_url> start")
        sys.exit(1)

    video_url = sys.argv[1]
    action = sys.argv[2]

    if action == "start":
        # Increase views by simulating 100 views as an example
        increase_views(video_url, num_views=100)
    else:
        print("Unknown action. Use 'start' to begin.")
