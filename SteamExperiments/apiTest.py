import requests
import json
import os

with open("../secrets.json", "r") as file:
    secret = json.load(file)

steam_token = secret["STEAM_TOKEN"]
steam_id = secret["STEAM_ID"]
response = requests.request("GET",
                            f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v002/?key={steam_token}&steamids={steam_id}")
print(response.content)

# Set the URL of the image you want to download
response = response.json()
image_url = response["response"]["players"][0]["avatar"]

# Set the directory where you want to save the image
save_directory = os.getcwd()

try:
    # Send a GET request to the URL to fetch the image
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the file extension from the URL
        file_extension = os.path.splitext(image_url)[1]

        # Construct the full file path
        full_save_path = os.path.join(save_directory, f"image{file_extension}")

        # Save the image to the file system
        with open(full_save_path, "wb") as file:
            file.write(response.content)

        print(f"Image saved to: {full_save_path}")
    else:
        print(f"Failed to download image from URL: {image_url}")
except requests.exceptions.RequestException as e:
    print(f"Error occurred while downloading image: {e}")

response2 = requests.request("GET",
                            f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_token}&steamid={steam_id}")

print(response2.content)