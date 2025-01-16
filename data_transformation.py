import pandas as pd

# Pokémon strength categorization
def categorize_experience(exp):
    if exp < 50:
        return "Fraco"
    elif 50 <= exp <= 100:
        return "Médio"
    else:
        return "Forte"

# Creating a DataFrame and categorizing the experience.
def transform_pokemon_data(pokemon_details):
    df = pd.DataFrame(pokemon_details)
    df["Category"] = df["Base Experience"].apply(categorize_experience)
    types_df = df.explode("Types")
    return df, types_df

# Calculates the mean statistics
def calculate_statistics(types_df):
    mean_stats = types_df.groupby("Types")[["Attack", "Defense", "HP"]].mean().reset_index()
    return mean_stats

# Returns the top 5 Pokemóns based on their Base Experience.
def get_top_pokemon(df, n=5):
    return df.nlargest(n, "Base Experience")
