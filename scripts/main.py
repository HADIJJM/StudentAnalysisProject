
# Import all cleaning & analysis functions
from clean import *
from analysis import *

def main():
# Run full pipeline: cleaning → finalize → analysis
    print("=== START CLEANING ===")
    clean_age()
    clean_gender()
    # Example: clean scores for selected subjects
    clean_scores(INTERIM_FILE, ['MathScore', 'EnglishScore', 'ScienceScore'])
    attendance_rate()
    behavior_notes()
    parental_support()
    process_city_normalization()
    clean_dates()

    # Convert NotFull to Final
    finalize_file()

    print("\n=== START ANALYSIS ===")
    topworst()
    beswor_in_gender()
    best_in_subject("MathScore")  # example, can change subject

if __name__ == "__main__":
    main()
