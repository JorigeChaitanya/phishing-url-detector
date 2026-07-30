import csv
from urllib.parse import urlparse

THREAT_FILE = "known_threats.csv"


def load_threats():

    threats = set()

    try:
        with open(
            THREAT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                threats.add(
                    row["domain"].lower()
                )

    except FileNotFoundError:

        print(
            "Threat database not found."
        )

    return threats


def check_known_threat(url):

    parsed = urlparse(url)

    hostname = (
        parsed.hostname or ""
    ).lower()

    threats = load_threats()

    return hostname in threats