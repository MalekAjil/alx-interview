#!/usr/bin/env python3
"""
Script to print all characters of a Star Wars movie
"""

import sys
import requests

def get_characters(movie_id):
    """Fetch and print characters of a Star Wars movie"""
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data from the API")
        return

    data = response.json()
    characters = data.get("characters", [])
    for character_url in characters:
        character_response = requests.get(character_url)
        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data.get("name"))

def main():
    """Main function to handle input and start fetching characters"""
    if len(sys.argv) != 2:
        print("Usage: Movie ID")
        sys.exit(1)

    try:
        movie_id = int(sys.argv[1])
    except ValueError:
        print("Movie ID must be a number")
        sys.exit(1)

    get_characters(movie_id)

if __name__ == "__main__":
    main()

