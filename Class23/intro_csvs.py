"""
We want to calculate the final grade for each student, where:
Average quiz grade is worth 40% of the final grade
Average exam grade is qorth 60% of the final grade
"""

import csv

def main():
    
    file = open("cs010grades.csv", "r")
    
    ### This creates a new CSV reader object to read the CSV
    reader = csv.reader(file)
    
    ### Iterate over a CSV
#     for line in reader:
#         print(line)
    
    ### Note: does not automatically convert numbers into numbers; they're all strings
        
    ### To get rid of the first (header) row:
    header = next(reader)
    print(header)
        
    for line in reader:
        
        name = line[0]
#         print(name)
        quizzes = line[1:11]
#         print(quizzes)
        exams = line[11:]
        
        average_quiz_score = average_list_of_strings(quizzes)
        average_exam_score = average_list_of_strings(exams)
        
#         print(name, average_quiz_score, average_exam_score)

        final_grade = average_exam_score * 0.6 + average_quiz_score * 0.4
        
#         print(name, final_grade)


    ### Write a function that turns a CSV into a grid
    grades = csv_to_grid("cs010grades.csv")
#     print(grades)

    for row in grades:
        print(row)
    
    
    
    
def csv_to_grid(filename):
    """Turns the csv file given by filename into a grid and returns it."""
    
    file = open(filename, "r")
    reader = csv.reader(file)
    
    grid = []
    for row in reader:
        grid.append(row)
        
    return grid
        
        
def average_list_of_strings(num_strings):
    """Finds the average of a list of numbers. But, assumes the list
    has all numbers represented as strings."""
    
    total = 0
    for num_str in num_strings:
        num = int(num_str)
        total += num
        
    return total / len(num_strings)
    
    
    
    



if __name__ == "__main__":
    main()
    