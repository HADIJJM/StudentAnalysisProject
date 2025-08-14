import pandas as pd
from pathlib import Path

# Final data file path
DATA_FILE = Path("data") / "processed" / "student_data_Final.csv"

def load_data():
    # Load & Check file 
    try:
        if not DATA_FILE.exists():
            raise FileNotFoundError(f"The file {DATA_FILE} does not exist.")
        
        df = pd.read_csv(DATA_FILE)
        
        if df.empty:
            print("Warning: The DataFrame is empty.")
            return None
        
        return df
    
    except Exception as e:
        print(f"An error occurred while loading data: {str(e)}")
        return None


def topworst():
    df = load_data()
    if df is None:
        return
    
    # 10 Student
    print("== Top Students: ==")
    top_students = df.sort_values(by='GPA', ascending=False).head(10)
    print(top_students[['Name', 'GPA']])
    
    # Worst Student
    print("\n== Worst Students: ==")
    worst_students = df.sort_values(by='GPA', ascending=True).head(10)
    print(worst_students[['Name', 'GPA']])
    
    # Mean
    mean_gpa = df['GPA'].mean()
    print(f"\nMean GPA: {mean_gpa:.2f}")


def beswor_in_gender():
    df = load_data()
    if df is None:
        return
    
    # أفضل وأسوأ الرجال
    best_men  = df[df['Gender'] == 'M'].nlargest(5, 'GPA')[['Name', 'Gender', 'GPA']]
    worst_men = df[df['Gender'] == 'M'].nsmallest(5, 'GPA')[['Name', 'Gender', 'GPA']]
    print("\nBest Men:\n", best_men)
    print("\nWorst Men:\n", worst_men)

    # أفضل وأسوأ النساء
    best_women  = df[df['Gender'] == 'F'].nlargest(5, 'GPA')[['Name', 'Gender', 'GPA']]
    worst_women = df[df['Gender'] == 'F'].nsmallest(5, 'GPA')[['Name', 'Gender', 'GPA']]
    print("\nBest Women:\n", best_women)
    print("\nWorst Women:\n", worst_women)


def best_in_subject(sub_name):
    df = load_data()
    if df is None:
        return
    
    if sub_name not in df.columns:
        print(f"Course '{sub_name}' not found in data.")
        return

    top_std = df.nlargest(5, sub_name)[['Name', sub_name]]
    dow_std = df.nsmallest(5, sub_name)[['Name', sub_name]]

    print(f"\nBest in {sub_name}:\n", top_std)
    print(f"\nWorst in {sub_name}:\n", dow_std)


# if __name__ == "__main__":
topworst()
    # beswor_in_gender()
    # best_in_subject("MathScore")
