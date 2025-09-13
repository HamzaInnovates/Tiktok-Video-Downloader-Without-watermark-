import requests
import os

def download_tiktok_no_watermark(video_url, output_dir="downloads"):
    try:
        api_url = "https://www.tikwm.com/api/"
        params = {"url": video_url}
        response = requests.get(api_url, params=params)

        if response.status_code != 200:
            print("Failed to fetch video data.")
            return

        data = response.json()
        if data.get("code") != 0:
            print("Error:", data.get("msg"))
            return

        no_watermark_url = data["data"]["play"]

        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"{data['data']['id']}.mp4")

        video_response = requests.get(no_watermark_url, stream=True)
        with open(file_path, "wb") as f:
            for chunk in video_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print(f"✅ Download complete: {file_path}")

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    tiktok_link = input("Enter TikTok video URL: ").strip()
    download_tiktok_no_watermark(tiktok_link)
