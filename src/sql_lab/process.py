type_mapping = {
    "int64": "BIGINT",
    "str": "VARCHAR(255)",
    "float64": "DOUBLE",
}

import logging
import os

import pandas as pd
from sqlalchemy import create_engine


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_data(filename):
    """Read a CSV file into a pandas DataFrame."""
    logging.info("Reading CSV file: %s", filename)

    try:
        data = pd.read_csv(filename)
        logging.info("Successfully read %d rows.", len(data))
        return data
    except Exception as e:
        logging.error("Error reading CSV file: %s", e)
        raise


def clean_data(data):
    """Remove rows with missing values and return the cleaned DataFrame."""
    logging.info("Cleaning data.")

    # Remove rows that contain any missing values
    cleaned_data = data.dropna()

    logging.info(
        "Removed %d rows with missing values.",
        len(data) - len(cleaned_data)
    )

    return cleaned_data


def load_data(data, table):
    """Upload a DataFrame to a MySQL database using SQLAlchemy."""
    logging.info("Loading data into table: %s", table)

    # Read database information from environment variables
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]

    try:
        # Create a connection to the MySQL database
        connection_url = (
            f"mysql+mysqlconnector://{user}:{password}"
            f"@{host}:3306/{dbname}"
        )
        engine = create_engine(connection_url)

        # Create the table if it does not exist and upload the data
        data.to_sql(table, engine, if_exists="append", index=False)

        logging.info(
            "Successfully loaded %d rows into %s.",
            len(data),
            table
        )

        # Close the database connection
        engine.dispose()

    except Exception as e:
        logging.error("Error loading data into database: %s", e)
        raise


def main():
    """Read, clean, and load the CSV data into MySQL."""
    logging.info("Starting data processing.")

    # Read the CSV file
    data = read_data("MOCK_DATA.csv")

    # Clean the data
    data = clean_data(data)

    # Always use the mock table
    load_data(data, "mock")

    logging.info("Data processing complete.")


if __name__ == "__main__":
    main()
