# Study Tracker System

# Overview of the Project
This project is a simple command-line Python program that helps students track their daily study hours.  
The user can add study data, view records, and see a graph of study time.  
All data is stored in a text file (study.txt), so it remains saved even after closing the program.

# Features
The system provides the following options:

1. Add Study (Option 1):
   User enters subject name and hours studied.
   Data is saved in a file.

2. View Study (Option 2):
   Displays all study records.
   Also shows total study hours.

3. Show Graph (Option 3):
   Displays a bar graph of subjects and hours using matplotlib.

4. Exit (Option 4):
   Closes the program.

# Technologies/Tools Used
Language: Python 3  
Library: Matplotlib  
Storage: Text File (study.txt)

# Steps to Install & Run the Project

## Prerequisites
Python 3 should be installed.

## Installation and Execution
1. Save the code in a file named:
   study_tracker.py

2. Open terminal or command prompt.

3. Install matplotlib:
   pip install matplotlib

4. Run the program:
   python study_tracker.py

5. Follow menu options (1, 2, 3, 4)

# Instructions for Testing

1. Test Adding Study
Choose option 1  
Enter subject and hours  

Expected Output:
Data should be saved in study.txt file  

2. Test Viewing Study
Choose option 2  

Expected Output:
All records should be displayed  
Total hours should be calculated  

3. Test Graph
Choose option 3  

Expected Output:
A bar graph should open showing subjects and hours  

4. Test Empty Data
Run program without adding data  

Expected Output:
Message like "No data found" should appear  

# Example
Input:
English, 2  
Math, 3  

Output:
Total = 5 hours  
