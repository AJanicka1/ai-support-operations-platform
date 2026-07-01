import pandas as pd

# Read source data

df = pd.read_csv("../data/raw/raw_tickets.csv")

print("\n=== FIRST ROWS ===")
print(df.head())

print("\n=== DATA INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DUPLICATES ===")
print(df.duplicated().sum())

# Remove duplicates

df = df.drop_duplicates()

# Rename columns

df.columns = [
    "timestamp",
    "reporter_name",
    "reporter_email",
    "department",
    "request_type",
    "priority",
    "business_impact",
    "detailed_description",
    "attachment_needed",
    "category"
]

# Reorder columns

df = df[
    [
        "timestamp",
        "reporter_name",
        "reporter_email",
        "department",
        "request_type",
        "category",
        "priority",
        "business_impact",
        "detailed_description",
        "attachment_needed"
    ]
]

# Create Ticket ID

df.insert(
    0,
    "ticket_id",
    [f"TCK-{i:04}" for i in range(1, len(df)+1)]
)

# Add Status

df["status"] = "New"

print("\n=== CLEAN DATA ===")
print(df.head())

# Save output

df.to_csv(
    "../data/processed/clean_tickets.csv",
    index=False
)

print("\nFile saved successfully.")