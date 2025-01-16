from logger import setup_logger
from data_extraction import extract_pokemon_data
from data_transformation import transform_pokemon_data, calculate_statistics, get_top_pokemon
from report_generation import generate_report


def main():
    logger = setup_logger()
    try:
        logger.info("Starting Pokémon Data Pipeline...")
        # Step 1: Data Extraction
        pokemon_details = extract_pokemon_data(logger)

        # Step 2: Data Transformation
        df, types_df = transform_pokemon_data(pokemon_details)
        mean_stats = calculate_statistics(types_df)
        top_5_pokemon = get_top_pokemon(df)

        # Step 3: Report Generation
        generate_report(df, types_df, mean_stats, logger)

        logger.info("Pipeline executed successfully!")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    main()
