import subprocess
from datetime import datetime


def sync_to_github():

    try:

        subprocess.run(
            ["git", "add", "."],
            check=True
        )

        commit_msg = (
            "Log update "
            + datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            check=True
        )

        subprocess.run(
            ["git", "push"],
            check=True
        )

        print(
            "\n[INFO] Logs synced to GitHub."
        )

    except Exception as e:

        print(
            "\n[ERROR] GitHub sync failed:",
            e
        )