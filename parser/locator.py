import re
cities = ['Santa Clara']
def find_location(text, cities_list):
    for city in cities:
        if contains_city(text, city):
            return city
        else:
            return None

def contains_city(text, city="Santa Clara"):
    # Create a regular expression pattern that matches the city name, ignoring case
    pattern = re.compile(re.escape(city), re.IGNORECASE)
    
    # Search the text for the pattern
    if pattern.search(text):
        return True
    else:
        return False

def remove_urls(text):
    # Remove detailed mixedSources with 'jpeg' and 'webp' entries
    mixed_sources_pattern = r'"mixedSources":\s*\{\s*"jpeg":\s*\[\s*{(?:\s*"url":\s*"[^"]*",\s*"width":\s*\d+\s*},?\s*)+\s*\],\s*"webp":\s*\[\s*{(?:\s*"url":\s*"[^"]*",\s*"width":\s*\d+\s*},?\s*)+\s*\]\s*\},?'
    text = re.sub(mixed_sources_pattern, '', text)

    # Optional: General cleanup for possibly now redundant keys like 'caption' if empty
    text = re.sub(r'"caption":\s*""\s*,?', '', text)

    # Remove URLs and empty objects/arrays
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r'\{\s*\}', '', text)
    text = re.sub(r'\[\s*\]', '', text)

    # Clean up trailing and leading commas and correct JSON formatting
    text = re.sub(r',\s*([}\]])', r'\1', text)
    text = re.sub(r'\{,', '{', text)
    text = re.sub(r'\[\s*,', '[', text)
    text = re.sub(r',\s*$', '', text)
    text = re.sub(r"\{\'url[^}]*\}", "", text)
    return text