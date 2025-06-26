def extract_features(url, html_content):
    features = []
    features.append(len(url))
    features.append(url.count('@'))
    features.append(url.count('-'))
    features.append(url.count('//'))
    features.append(1 if "https" in url else 0)
    features.append(1 if "login" in html_content.lower() else 0)
    return features