import requests
import logging

def get_pokemon_list(logger):
    logger.info("Fetching Pokémon list...")
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    logger.error(f"Failed to fetch Pokémon list: {response.status_code}")
    return []

def get_pokemon_details(url, logger):
    #logger.info(f"Fetching details for Pokémon: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    logger.error(f"Failed to fetch details for URL {url}: {response.status_code}")
    return {}

def extract_pokemon_data(logger):
    pokemon_list = get_pokemon_list(logger)
    pokemon_details = []
    for pokemon in pokemon_list:
        details = get_pokemon_details(pokemon["url"], logger)
        if details:
            pokemon_details.append({
                "ID": details["id"],
                "Name": details["name"].title(),
                "Base Experience": details["base_experience"],
                "Types": [t["type"]["name"].title() for t in details["types"]],
                "HP": details["stats"][0]["base_stat"],
                "Attack": details["stats"][1]["base_stat"],
                "Defense": details["stats"][2]["base_stat"]
            })
    logger.info("Data extraction complete.")
    return pokemon_details
