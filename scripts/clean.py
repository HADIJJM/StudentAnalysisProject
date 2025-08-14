import pandas as pd
from pathlib import Path

import pandas as pd
from pathlib import Path

# Check pandas version
print("Pandas version:", pd.__version__)

# Check Path availability (simply test creation)
p = Path(".")
print("Path works, current directory:", p.resolve())


# ==== Define paths ====
BASE_DIR = Path(__file__).resolve().parent.parent  # Project root
RAW_FILE = BASE_DIR / "data" / "raw" / "student_data_dirty.csv"
INTERIM_FILE = BASE_DIR / "data" / "interim" / "student_data_NotFull.csv"
FINAL_FILE = BASE_DIR / "data" / "processed" / "student_data_Final.csv"

# ==== File existence check ====
def check_file_exists(file_path: Path):
    """Check if file exists before processing."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    print(f"File found: {file_path}")

# ==== Cleaning functions ====

def clean_age():
# Clean Age column and replace invalid/missing values with mean age.
    check_file_exists(RAW_FILE)
    df = pd.read_csv(RAW_FILE)

    print("== Age values before cleaning ==")
    print(df['Age'].unique())

    # Fill NaN with mean of valid ages first
    valid_age = df[(df['Age'] >= 15) & (df['Age'] <= 18)]
    mean_age = int(valid_age['Age'].mean())
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # ensure numeric
    df['Age'] = df['Age'].fillna(mean_age)
    df.loc[(df['Age'] < 15) | (df['Age'] > 18), 'Age'] = mean_age

    df.to_csv(INTERIM_FILE, index=False)

    print("== Age values after cleaning ==")
    print(df['Age'].unique())
    
def clean_gender():
# Standardize Gender column and fill missing values.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['Gender'] = df['Gender'].astype(str).str.strip().str.lower()
    df['Gender'] = df['Gender'].replace({
        'male': 'M', 'm': 'M',
        'female': 'F', 'f': 'F'
    })
    # Fill missing or invalid values with 'Unknown'
    df['Gender'] = df['Gender'].replace(['', 'nan', 'na', 'none'], 'Unknown')

    df.to_csv(INTERIM_FILE, index=False)
    print("Gender values after cleaning:")
    print(df['Gender'].unique())

def clean_scores(file_path: Path, columns):
# Clean score columns: convert words to numbers, fill missing values.
    check_file_exists(file_path)
    df = pd.read_csv(file_path)

    replacements = {
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
    }

    for col in columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
        df[col] = df[col].replace(replacements)
        df[col] = pd.to_numeric(df[col], errors='coerce')  # convert to numeric
        # Fill NaN with mean
        df[col] = df[col].fillna(round(df[col].mean()))

    df.to_csv(file_path, index=False)
    
    print(f"Scores cleaned for columns: {columns}")
    for col in columns:
        print(f"Unique values in '{col}' after cleaning: {df[col].unique()}")

def attendance_rate():
# Ensure AttendanceRate is <= 100 and fill missing values.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['AttendanceRate'] = pd.to_numeric(df['AttendanceRate'], errors='coerce')
    df['AttendanceRate'] = df['AttendanceRate'].fillna(df['AttendanceRate'].mean())
    df.loc[df['AttendanceRate'] > 100, 'AttendanceRate'] = 100

    df.to_csv(INTERIM_FILE, index=False)

    print("AttendanceRate after cleaning:")
    print(df['AttendanceRate'].unique())

def behavior_notes():
# Clean BehaviorNotes column and fill missing values.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['BehaviorNotes'] = df['BehaviorNotes'].astype(str).str.strip()
    df['BehaviorNotes'] = df['BehaviorNotes'].replace(['', ' ', 'null', 'NaN', 'nan'], pd.NA)
    df['BehaviorNotes'] = df['BehaviorNotes'].fillna('Unknown')

    df.to_csv(INTERIM_FILE, index=False)
    
    print("BehaviorNotes after cleaning:")
    print(df['BehaviorNotes'].unique())

def parental_support():
# Standardize ParentalSupport column and fill missing values.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['ParentalSupport'] = df['ParentalSupport'].astype(str).str.strip().str.lower()
    df['ParentalSupport'] = df['ParentalSupport'].replace({
        'yes': 'Y', 'y': 'Y', 'true': 'Y',
        'no': 'N', 'n': 'N', 'false': 'N'
    })
    df['ParentalSupport'] = df['ParentalSupport'].replace(['', 'nan', 'none'], 'Unknown')

    df.to_csv(INTERIM_FILE, index=False)
    
    print("ParentalSupport after cleaning:")
    print(df['ParentalSupport'].unique())

def normalize_city(city):
# Normalize city names to standard form.
    city = str(city).strip().lower()
    if city.startswith('riy'):
        return 'Riyadh'
    elif city.startswith('jed'):
        return 'Jeddah'
    elif city.startswith('dam'):
        return 'Dammam'
    else:
        return city.title()

def process_city_normalization():
# Apply city normalization to the City column and fill missing values.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['City'] = df['City'].apply(normalize_city)
    df['City'] = df['City'].fillna('Unknown')

    df.to_csv(INTERIM_FILE, index=False)
    
    print("City values after normalization:")
    print(df['City'].unique())

def clean_dates():
# Convert RegisteredDate to datetime and report invalid entries.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)

    df['RegisteredDate'] = pd.to_datetime(df['RegisteredDate'], errors='coerce')

    invalid_dates = df[df['RegisteredDate'].isna()]
    if not invalid_dates.empty:
        print(f"Found {len(invalid_dates)} invalid date(s):")
        print(invalid_dates[['RegisteredDate']])
    else:
        print("All dates are valid.")

    df.to_csv(INTERIM_FILE, index=False)
    print("RegisteredDate cleaned and saved to final file.")

# Call it at the END! 
def finalize_file():
# Simply save NotFull file to Final file.
    check_file_exists(INTERIM_FILE)
    df = pd.read_csv(INTERIM_FILE)
    df.to_csv(FINAL_FILE, index=False)
    print(f"{FINAL_FILE} file saved.")
