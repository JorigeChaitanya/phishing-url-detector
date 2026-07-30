def calculate_score(features, threat_match=False):

    score = 0

    if features["ip_address"]:
        score += 30

    if features["no_https"]:
        score += 15

    if features["long_url"]:
        score += 10

    if features["many_subdomains"]:
        score += 20

    score += features["keyword_count"] * 5

    if features["suspicious_tld"]:
        score += 20

    if features["brand_spoofing"]:
        score += 30

    if features["encoded_chars"]:
        score += 10

    if features["redirect"]:
        score += 20

    return min(score, 100)


def get_verdict(score):

    if score >= 60:
        return "PHISHING"

    elif score >= 30:
        return "SUSPICIOUS"

    else:
        return "SAFE"