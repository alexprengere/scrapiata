import csv
import time
import random

import httpx
from bs4 import BeautifulSoup


URL = "https://www.iata.org/en/publications/directories/code-search/?airport.page={}"
MIN_PAGE_NB = 1
MAX_PAGE_NB = 10_000  # currently it should stop around 1829 pages


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--min-page-number", type=int, default=MIN_PAGE_NB)
    parser.add_argument("--max-page-number", type=int, default=MAX_PAGE_NB)
    args = parser.parse_args()

    with open("output.csv", "w") as out:
        csv_writer = csv.writer(out, delimiter=",")

        for page_nb in range(args.min_page_number, 1 + args.max_page_number):
            result = httpx.get(URL.format(page_nb))
            soup = BeautifulSoup(result.text, "html.parser")

            # Airports table is the second table
            # Airports table rows start with a header that we skip
            airports_table = soup.find_all("table")[1]
            airports_table_rows = airports_table.find_all("tr")[1:]

            print(f"Getting page #{page_nb}, found {len(airports_table_rows)} elements")
            if not airports_table_rows:  # No rows means the page number is now too big
                print(f"Breaking at page #{page_nb}, no more data")
                break

            for row in airports_table_rows:
                csv_writer.writerow(col.text for col in row.find_all("td"))

            # Sleeping randomly in 0-1s
            time.sleep(random.random())
        else:
            # Never broke means we did not reach the end of data
            print(f"Reached the max page #{args.max_page_number}, increase it?")


if __name__ == "__main__":
    main()
