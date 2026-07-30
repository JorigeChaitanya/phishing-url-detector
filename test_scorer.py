from detector import extract_features
from scorer import calculate_score, get_verdict

url = input("Enter URL: ")

features = extract_features(url)

score = calculate_score(features)

verdict = get_verdict(score)

print("\nScore:", score)
print("Verdict:", verdict)