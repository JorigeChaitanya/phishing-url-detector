from detector import extract_features
from scorer import calculate_score, get_verdict
from threat_intel import check_known_threat
from logger import log_result, show_logs
from github_sync import sync_to_github


def scan_url():

    url = input("\nEnter URL: ").strip()

    if not url.startswith(
        ("http://", "https://")
    ):
        url = "http://" + url

    features = extract_features(url)

    threat_match = check_known_threat(url)

    score = calculate_score(
        features,
        threat_match
    )

    verdict = get_verdict(score)

    print("\n===== ANALYSIS RESULT =====")

    print("URL:", url)
    print("Score:", score)
    print("Verdict:", verdict)

    print("\nTriggered Indicators:")

    for key, value in features.items():

        if value:
            print("-", key)

    if threat_match:
        print("- known malicious domain")

    log_result(
        url,
        score,
        verdict
    )

    print("\nResult saved to log.")


def menu():

    while True:

        print("\n==============================")
        print("PHISHING URL DETECTOR")
        print("==============================")

        print("1. Scan URL")
        print("2. View Logs")
        print("3. Sync Logs to GitHub")
        print("4. Exit")

        choice = input(
            "\nSelect option: "
        )

        if choice == "1":

            scan_url()

        elif choice == "2":

            show_logs()

        elif choice == "3":

            sync_to_github()
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    menu()