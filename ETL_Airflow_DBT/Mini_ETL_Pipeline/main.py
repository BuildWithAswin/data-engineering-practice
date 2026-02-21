from extract import extract_data
from transform import clean_data, transform_data
from load import load_data
from utils import setup_logger

logger = setup_logger()


def run_pipeline():
    logger.info("Starting ETL pipeline")

    df = extract_data()
    logger.info(f"Extracted {len(df)} rows")

    df = clean_data(df)
    logger.info("Data transformed")

    df = transform_data(df)
    logger.info("Data transformed")

    load_data(df)
    logger.info("Data loaded successfully")


if __name__ == "__main__":
    run_pipeline()
