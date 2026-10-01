import logging
import os
import mysql.connector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_data_by_group(value):
    """Return all rows from mock where the group column equals value."""
    # Read database credentials from environment variables
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            database=dbname,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # Use a parameterized query to safely filter by group
        query = """
            SELECT id, `group`, name, gender, email, score
            FROM mock
            WHERE `group` = %s
        """

        cursor.execute(query, (value,))

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        logging.info(
            "Retrieved %d rows for group '%s'.",
            len(results),
            value
        )

        return results

    except Exception as e:
        logging.error("Error retrieving data by group: %s", e)
        raise

def plot_counts(groupby):
    """Count rows in mock grouped by the specified column."""
    # read database credentials from environment variables
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]

    try:
        # connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            database=dbname,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # only allow known column names to be used in the query
        allowed_columns = {
            "id",
            "group",
            "name",
            "gender",
            "email",
            "score"
        }

        if groupby not in allowed_columns:
            raise ValueError(f"Invalid column name: {groupby}")

        # backticks safely quote the column name
        query = f"""
            SELECT `{groupby}`, COUNT(*)
            FROM mock
            GROUP BY `{groupby}`
        """

        cursor.execute(query)

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        logging.info(
            "Counted rows grouped by '%s'.",
            groupby
        )

        return results

    except Exception as e:
        logging.error("Error counting rows: %s", e)
        raise


def main():
    """Run example queries against the mock table."""
    # get all records belonging to one group
    group_results = get_data_by_group("A")
    print("Rows in group A:")
    for row in group_results:
        print(row)

    # count records by gender
    gender_counts = plot_counts("gender")
    print("\nCounts by gender:")
    for row in gender_counts:
        print(row)


if __name__ == "__main__":
    main()
