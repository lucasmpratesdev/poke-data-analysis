import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Obter a lista de Pokémon
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10&offset=0")
data = response.json()
pokemon_list = data["results"]

# Lista para armazenar os detalhes dos Pokémon
pokemon_details = []

# Obter os detalhes de cada Pokémon
for pokemon in pokemon_list:
    detail_response = requests.get(pokemon["url"])
    detail_data = detail_response.json()

    pokemon_id = detail_data["id"]
    name = detail_data["name"].title()
    base_experience = detail_data["base_experience"]
    types = [t["type"]["name"].title() for t in detail_data["types"]]
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in detail_data["stats"]}
    hp = stats.get("hp", 0)
    attack = stats.get("attack", 0)
    defense = stats.get("defense", 0)

    pokemon_details.append({
        "ID": pokemon_id,
        "Name": name,
        "Base Experience": base_experience,
        "Types": types,
        "HP": hp,
        "Attack": attack,
        "Defense": defense
    })

# Criar DataFrame com os dados coletados
pokemon_df = pd.DataFrame(pokemon_details)
print(pokemon_df)

# Categorizar os Pokémon por experiência base
def categorize_experience(exp):
    if exp < 50:
        return "Fraco"
    elif 50 <= exp <= 100:
        return "Médio"
    else:
        return "Forte"

pokemon_df["Category"] = pokemon_df["Base Experience"].apply(categorize_experience)

# Explodir os tipos em múltiplas linhas
types_df = pokemon_df.explode("Types")
print(types_df)
# Contagem de Pokémon por tipo
type_counts = types_df["Types"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]
print(pokemon_df.columns)
# Criar gráfico de barras para a distribuição de tipos
sns.barplot(x="Count", y="Type", data=type_counts, hue="Type", palette="viridis", legend=False)
plt.title("Distribution of Pokémon by Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
#plt.show(block=False) #Não mostra o gráfico
plt.savefig("grafico.png")  # Salva o gráfico no disco
plt.close()  # Fecha a janela do gráfico

# Análise estatistica: Média de ataque, defesa e HP por tipo
mean_stats = types_df.groupby("Types")[["Attack", "Defense", "HP"]].mean().reset_index()
mean_stats.columns = ["Type", "Mean Attack", "Mean Defense", "Mean HP"]
print(mean_stats)


# Top 5 Pokémon por experiencia base
top_5_pokemon = pokemon_df.nlargest(5, "Base Experience")
print("Top 5 Pokémon by Base Experience:")
print(top_5_pokemon[["Name", "Base Experience"]])

# Exportar tabela de média de ataque, defesa e HP por tipo
mean_stats.to_csv("mean_stats.csv", index=False)
print("Tabela de médias por tipo exportada para mean_stats.csv")

# Exportar tabela dos 5 Pokémon com maior experiência base
top_5_pokemon[["Name", "Base Experience"]].to_csv("top_5_pokemon.csv", index=False)
print("Tabela dos Top 5 Pokémon exportada para top_5_pokemon.csv")
