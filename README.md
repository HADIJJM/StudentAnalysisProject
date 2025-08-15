# Student Analysis Project

## Description
This project cleans and analyzes student data. It handles missing values, normalizes columns, and performs basic analysis such as top/worst students, gender-based analysis, and subject-specific rankings.

## Requirements
- Python 3.11+
- Pandas 2.3.1

## Installation
To get started with the project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HADIJJM/StudentAnalysisProject.git
    cd StudentAnalysisProject
    ```

2.  **Install dependencies:**
    The project uses a `requirements.txt` file to manage its dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the project:**
    To execute the data cleaning and analysis pipeline, run the main script.
    ```bash
    python main.py
    ```

## Project Structure
The repository is organized as follows:

StudentAnalysisProject/
├─ data/
│  ├─ raw/            # Original dirty data
│  ├─ interim/        # NotFull (partially cleaned) data
│  └─ processed/      # Final cleaned data
├─ clean.py           # Data cleaning functions
├─ analysis.py        # Analysis functions
├─ main.py            # Pipeline execution
├─ requirements.txt   # Python dependencies
├─ README.md          # Project description
└─ .gitignore         # Git ignore rules


## How It Works
* **`main.py`**: This is the entry point of the project. It orchestrates the entire workflow by calling functions from `clean.py` and `analysis.py`.
* **`clean.py`**: Contains all the functions necessary for data preprocessing, including handling missing values, standardizing column names, and normalizing data types.
* **`analysis.py`**: Contains the core analysis functions, which read the processed data and perform tasks like calculating top students, gender-based performance, and generating subject-wise rankings.

## License
This project is licensed under the MIT License.
