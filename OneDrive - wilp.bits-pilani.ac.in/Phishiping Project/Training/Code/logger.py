import csv
import os
from datetime import datetime

LOG_FILE = "phishing_log.csv"


def create_log():

    if not os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "timestamp",
                "url",
                "score",
                "verdict"
            ])


def log_result(
    url,
    score,
    verdict
):

    create_log()

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            url,
            score,
            verdict
        ])

def show_logs():

    try:
        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            print(file.read())

    except FileNotFoundError:
        print("No logs found.")