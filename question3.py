# Build a grade calculator that uses loops and functions to process student scores.

# Requirements:

    # Create a function calculate_average(scores) that:
        # Takes a list of scores as a parameter
        # Calculates and returns the average
    # Create a function get_letter_grade(average) that:
        # Takes an average score as a parameter
        # Returns letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60)
    # Use a while loop to:
        # Ask how many test scores to enter
        # Collect each score from the user
        # Store scores in a list
    # Display the average and letter grade using your functions

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    length = len(scores)
    return total/length

def get_letter_grade(average):
    if average < 60:
        return "Grade: F"
    elif average <=69:
        return "Grade: D"
    elif average <=79:
        return "Grade: C"
    elif average <=89:
        return "Grade: B"
    else:
        return "Grade A"

reported_scores = []
counter = 1
try:
    scores_count = int(input("How many scores do you want to report?"))
    while counter <= scores_count:
        new_score = float(input(f"Enter Score {counter}: "))
        reported_scores.append(new_score)
        counter += 1
    average_score = calculate_average(reported_scores)

    print("******************************************")
    print(f"Average of {scores_count} reported scores: {average_score:.2f}")
    print(get_letter_grade(average_score))

except ValueError:
    print("Invalid input!")





# calculate_average ([100,200,300])
# print(tunde)

# get_letter_grade(59)
# print(tayo)



