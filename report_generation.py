import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Generates the report by creating a distribution chart
def generate_report(df, types_df, mean_stats, logger):
    logger.info("Generating distribution chart...")
    type_counts = types_df["Types"].value_counts().reset_index()
    type_counts.columns = ["Type", "Count"]

    # Create a bar plot for the distribution of Pokémon types
    sns.barplot(x="Count", y="Type", data=type_counts, palette="viridis", hue="Type", legend=False)
    plt.title("Distribution of Pokémon by Type")
    plt.xlabel("Count")
    plt.ylabel("Type")
    plt.tight_layout()
    plt.savefig("outputs/grafico.png")
    plt.close()

    logger.info("Saving data to CSV...")
    mean_stats.to_csv("outputs/mean_stats.csv", index=False, float_format="%.1f")
    top_5_pokemon = df.nlargest(5, "Base Experience")
    top_5_pokemon[["Name", "Base Experience"]].to_csv("outputs/top_5_pokemon.csv", index=False)
    logger.info("Report generation complete.")
