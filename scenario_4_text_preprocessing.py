# Scenario 4: Text Pre-processing
# Task: Clean a text column in a DataFrame by:

# 1. Converting to lowercase.

# 2. Removing special characters (e.g., !, @).

# 3. Tokenizing the text.

import pandas as pd
import re

def clean_text(df):
    df["text"] = df["text"].str.lower()
    df["text"] = df["text"].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
    df["tokens"] = df["text"].apply(lambda x: x.split())
    return df

data = {
    "text": ["Hello World!", "AI@2026 is Great!!!"]
}

df = pd.DataFrame(data)

result = clean_text(df)

print(result)