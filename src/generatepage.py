def extract_title(markdown):    
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("No heading in markdown file")