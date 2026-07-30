import subprocess
from datetime import datetime


def sync_to_github():

    try:

        # Check for changes
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True
        )

        if not status.stdout.strip():

            print("\n[INFO] No new changes to sync.")
            return

        # Stage all changes
        subprocess.run(
            ["git", "add", "."],
            check=True
        )

        # Create commit
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

        # Push to GitHub
        subprocess.run(
            ["git", "push"],
            check=True
        )

        print(
            "\n[INFO] Logs synced to GitHub successfully."
        )

    except subprocess.CalledProcessError as e:

        print(
            "\n[ERROR] Git command failed:",
            e
        )

    except Exception as e:

        print(
            "\n[ERROR] GitHub sync failed:",
            e
        )