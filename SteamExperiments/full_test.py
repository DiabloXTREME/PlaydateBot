import os
import requests
import json

# Setup
with open("../secrets.json", "r") as file:
    secret = json.load(file)

steam_token = secret["STEAM_TOKEN"]
steam_id = secret["STEAM_ID"]

"""
Objective:
Get player data and download their pfp, images from top 5 games, and add that to a Markdown document

Objective Flow:
Get player avatar
=>
Get games list -> Sort by time -> Find top 5 most played -> Store top 5 -> Get image URLs through appIDs -> Download and save the images
=>
Add all to markdown file with f""
"""

# Player Data