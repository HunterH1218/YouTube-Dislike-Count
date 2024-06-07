import requests

def get_dislikes(video_id):
    api_url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        dislikes = data.get('dislikes', 'No data found')
        return dislikes
    else:
        return "Failed to fetch data"

if __name__ == "__main__":
    video_id = "your video id here"
    dislikes = get_dislikes(video_id)
    print(f"Dislikes: {dislikes}")