# Intelligent Study Planner using AI and ML

## Overview of the Project

This project is an advanced Python-based study tracker that helps students monitor and improve their study habits using Artificial Intelligence (AI) and Machine Learning (ML).

The system allows users to:

* Record daily study hours
* View and analyze study patterns
* Get intelligent recommendations
* Predict future study time using machine learning

All data is stored in a text file (`study.txt`), ensuring persistence even after the program is closed.

---

## Features

### 1. Add Study (Option 1)

* User enters subject name and hours studied
* Data is stored in `study.txt`

---

### 2. View Study (Option 2)

* Displays all study records
* Calculates total study hours

---

### 3. Timer (Option 3)

* GUI-based study timer using Tkinter
* Automatically saves study time after completion

---

### 4. Show Graph (Option 4)

* Displays a bar graph of subjects vs hours
* Uses Matplotlib for visualization

---

### 5. ML Prediction (Option 5)

* Uses Linear Regression algorithm
* Predicts next day study hours based on past data
* Learns study trends automatically

---

### 6. AI Recommendation (Option 6)

* Suggests which subjects need more focus
* Compares study time with average

---

### 7. Performance Analysis (Option 7)

* Identifies:

  * Weakest subject
  * Strongest subject

---

### 8. Exit (Option 8)

* Closes the program safely

---

## Technologies / Tools Used

* Language: Python 3
* Libraries:

  * Matplotlib (Graph)
  * Tkinter (GUI Timer)
  * NumPy (Data Handling)
  * scikit-learn (Machine Learning)
* Storage: Text File (`study.txt`)

---

## Steps to Install & Run

### Prerequisites

* Python 3 installed

---

### Installation

Open terminal / command prompt and run:

pip install matplotlib numpy scikit-learn

---

### Execution

1. Save the file as:
   study_tracker.py

2. Run the program:
   python study_tracker.py

3. Follow menu options (1–8)

---

## Instructions for Testing

### Test Add Study

* Choose Option 1
* Enter subject and hours
* Expected Output: Data should be saved in `study.txt`

---

### Test View Study

* Choose Option 2
* Expected Output:

  * All records displayed
  * Total hours calculated

---

### Test Graph

* Choose Option 4
* Expected Output: A bar graph should open

---

### Test ML Prediction

* Choose Option 5
* Expected Output:

  * Predicted study hours displayed
  * Based on past data

---

### Test AI Recommendation

* Choose Option 6
* Expected Output:

  * Subjects needing improvement displayed

---

### Test Empty Data

* Run program without adding data
* Expected Output: Message like "No data found"

---

## Example

Input:
English,2
Math,3
Science,1.5

Output:
Total = 6.5 hours

AI Recommendation:
English → Good
Math → Good
Science → Needs more focus

ML Prediction:
Next Day ≈ 2.8 hours

---

## Project Concept

This project combines:

* Artificial Intelligence (AI):

  * Decision-making through recommendations
  * Performance analysis

* Machine Learning (ML):

  * Predicts future study hours using past data

---

## Conclusion

This system helps students:

* Track study habits
* Improve weak areas
* Plan future study schedules intelligently

It demonstrates a practical implementation of Artificial Intelligence and Machine Learning in a real-world application.
