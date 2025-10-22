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
        return "Letter Grade: F"
    elif average <=69:
        return "Letter Grade: D"
    elif average <=79:
        return "Letter Grade: C"
    elif average <=89:
        return "Letter Grade: B"
    else:
        return "Letter Grade A"

reported_scores = []
counter = 1
try:
    scores_count = int(input("How many test scores do you want to enter? "))
    while counter <= scores_count:
        new_score = float(input(f"Enter score {counter}: "))
        reported_scores.append(new_score)
        counter += 1
    average_score = calculate_average(reported_scores)

    print("\n===GRADE REPORT ===")
    print(f"Test Scores: {reported_scores}")
    print(f"Average Score: {average_score:.1f}")
    print(get_letter_grade(average_score))

except ValueError:
    print("Invalid input!")



