import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

# Load your reviews CSV
df = pd.read_csv("reviews.csv")

def classify_review(review):
    prompt = f"""
    You are labeling customer reviews.
    For the review below, return a JSON with three booleans: is_ad, is_relevant, is_rant_no_visit.

    Review: "{review}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}  # ensures JSON output
    )

    return response.choices[0].message["content"]

# Apply classification
df[["is_ad", "is_relevant", "is_rant_no_visit"]] = df["review"].apply(
    lambda x: pd.Series(eval(classify_review(x)))
)

# Save to new CSV
df.to_csv("labeled_reviews.csv", index=False)
