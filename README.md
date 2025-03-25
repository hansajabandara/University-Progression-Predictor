Overview

The University Progression Predictor is a Python-based application designed to evaluate student academic performance and determine their progression status. The program operates in a staff-student mode, allowing staff to input multiple student records, generate histograms, and store progression history, while students can check their individual progression status.

Features

1. User Roles

Staff Mode:

Allows multiple student records to be entered.
Generates a histogram to visualize progression trends.
Reads and displays stored progression history from a file.
Requires staff login authentication.

Student Mode:

Enables students to input their Pass, Defer, and Fail credits.
Predicts their academic progression outcome.

2. Progression Outcomes
Based on entered credits, the program determines one of the following:

Progress (Pass: 120)
Progress (Module Trailer) (Pass: 100)
Do not Progress - Module Retriever (Fail < 80)
Exclude (Fail ≥ 80)

3. Credit Validation
   
Ensures valid credit values (0, 20, 40, 60, 80, 100, 120).
Validates that the total credits always sum to 120.

4. Histogram Visualization (Staff Mode Only)
   
Uses the graphics.py module to display a bar chart.
Color-coded categories:

Green: Progress
Yellow: Module Trailer
Blue: Module Retriever
Red: Exclude

Displays the total number of students analyzed.

5. Data Storage
   
Progression results are stored in histogram_data.txt for historical reference.

Installation & Requirements
Prerequisites
Python 3.x installed
graphics.py module (for histogram visualization)
Installing graphics.py
To install the graphics.py module, run:
bash
Copy
Edit
pip install graphics.py
How to Run the Program
Run the Python script:

bash
Copy
Edit
python progression_predictor.py
Select user type:

Enter "staff" for staff mode.
Enter "student" for student mode.

For Staff Mode:

Login with username: "staff" and password: "welcome".
Enter student records.
View histogram and stored progression results.

For Student Mode:

Enter Pass, Defer, and Fail credits.
View progression outcome.

Error Handling

Invalid inputs: Users must enter only integers.
Out-of-range values: Credit values must be from {0, 20, 40, 60, 80, 100, 120}.
Total credit validation: Ensures total is always 120.
Login authentication: Incorrect staff credentials prompt re-entry.
Graphics errors: Any issues with histogram rendering will not crash execution.

File Structure
bash
Copy
Edit
/progression_predictor
│── University_Predictor.py    # Main Python script
│── histogram_data.txt         # Stores student progression records
│── README.md                  # Documentation

Future Enhancements
GUI implementation for improved user interaction.
Database integration for long-term storage.
Additional analytics for performance trends.

Author
Developed as part of a Individual project
By: Hansaja Bandara
