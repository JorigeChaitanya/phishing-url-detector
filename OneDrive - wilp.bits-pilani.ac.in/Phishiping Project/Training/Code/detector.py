import re
from urllib.parse import urlparse, parse_qs

PHISHING_KEYWORDS = [
    "login",
    "signin",
    "verify",
    "secure",
    "update",
    "confirm",
    "account",
    "password"
]

SUSPICIOUS_TLDS = [
    ".tk",
    ".ml",
    ".ga",
    ".cf",
    ".gq",
    ".xyz",
    ".top",
    ".click",
    ".site"
]


def extract_features(url):

    parsed = urlparse(url)

    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""

    features = {}

    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"

    features["ip_address"] = bool(
        re.match(ip_pattern, hostname)
    )

    features["no_https"] = (
        parsed.scheme != "https"
    )

    features["long_url"] = (
        len(url) > 75
    )

    features["many_subdomains"] = (
        hostname.count(".") > 3
    )

    features["keyword_count"] = sum(
        1
        for word in PHISHING_KEYWORDS
        if word in url.lower()
    )

    features["suspicious_tld"] = any(
        hostname.endswith(tld)
        for tld in SUSPICIOUS_TLDS
    )

    trusted_brands = [
        "paypal",
        "amazon",
        "google",
        "apple",
        "microsoft",
        "netflix"
    ]

    root_parts = hostname.split(".")

    if len(root_parts) >= 2:
        root_domain = (
            root_parts[-2]
            + "."
            + root_parts[-1]
        )
    else:
        root_domain = hostname

    features["brand_spoofing"] = any(
        brand in hostname
        and brand not in root_domain
        for brand in trusted_brands
    )

    features["encoded_chars"] = bool(
        re.search(
            r"%[0-9A-Fa-f]{2}",
            path + query
        )
    )

    redirect_params = {
        "url",
        "redirect",
        "next",
        "goto",
        "return"
    }

    params = parse_qs(query)

    features["redirect"] = bool(
        redirect_params.intersection(
            params.keys()
        )
    )

    return features