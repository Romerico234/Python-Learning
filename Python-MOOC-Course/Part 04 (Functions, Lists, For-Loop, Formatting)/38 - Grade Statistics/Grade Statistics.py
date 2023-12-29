def input_from_user():
    list = []
    while True:
        result = input("Exam points and execrises completed: ")
        if result == "":
            break
        list.append(result)
    return list

def exam(exam: list):
    exam_points  = []
    for i in exam:
        split_values = i.split()
        exam_points.append(int(split_values[0]))
    return exam_points

def exercises(exercises: list):
    exercises_list  = []
    for i in exercises:
        split_values = i.split()
        exercises_list.append(int(split_values[1]))
    return exercises_list

def convert_to_exercise_points(exercises: list):
    exercise_points = []
    for i in exercises:
        if i >= 100:
            exercise_points.append(10)
        elif i >= 90:
            exercise_points.append(9)
        elif i >= 80:
            exercise_points.append(8)
        elif i >= 70:
            exercise_points.append(7)
        elif i >= 60:
            exercise_points.append(6)
        elif i >= 50:
            exercise_points.append(5)
        elif i >= 40:
            exercise_points.append(4)
        elif i >= 30:
            exercise_points.append(3)
        elif i >= 20:
            exercise_points.append(2)
        elif i >= 10:
            exercise_points.append(1)
        else:
            exercise_points.append(0)
    return exercise_points


def grade(exercise_points: list, exam_points: list):
    grade_list = []
    for i in range(len(exercise_points)):
        total_points = exercise_points[i] + exam_points[i]
        if exam_points[i] < 10:
            grade_list.append(0)
        elif total_points in range(28,31):
            grade_list.append(5)
        elif total_points in range(24,28):
            grade_list.append(4)
        elif total_points in range(21, 24):
            grade_list.append(3)
        elif total_points in range(18,21):
            grade_list.append(2)
        elif total_points in range(15,18):
            grade_list.append(1)
        elif total_points in range(0,15):
            grade_list.append(0)
    return grade_list
             
    
def main():
    students_info = input_from_user()
    exercises_list = exercises(students_info)
    exam_points = exam(students_info)
    exercise_points = convert_to_exercise_points(exercises_list)
    grade_list = grade(exercise_points,exam_points)

    average = (sum(exam_points) + sum(exercise_points)) / len(grade_list)
    failed = grade_list.count(0)
    pass_per = 100 * ((len(grade_list) - failed) / len(grade_list))
    print("Statistics: ")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_per:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        count = grade_list.count(i)
        print(f"{i}: {'*' * count}")
    


main()    


    
        


