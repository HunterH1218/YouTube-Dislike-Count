## Simple YouTube Dislike Fetcher

This Python script fetches the dislike count for a given YouTube video ID using the Return YouTube Dislike API

**Please note that this relies on a third-party API and the accuracy of the dislike count may vary.**

### Requirements

- Python 3.6+
- `requests` library

### Installation

1. Install the `requests` library:
   ```bash
   pip install requests
   ```

### Usage

1. Replace `"your video id here"` in the `video_id` variable with the actual YouTube video ID.
2. Run the script:
   ```bash
   python get_dislikes.py
   ```

### Example

```python
import requests

def get_dislikes(video_id):
    # ... (code remains the same)

if __name__ == "__main__":
    video_id = "dQw4w9WgXcQ"  # Replace with the actual video ID
    dislikes = get_dislikes(video_id)
    print(f"Dislikes: {dislikes}")
```
