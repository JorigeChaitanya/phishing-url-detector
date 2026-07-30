from detector import extract_features

url = input("Enter URL: ")

result = extract_features(url)

print("\nFeatures Found:\n")

for key, value in result.items():
    print(key, ":", value)