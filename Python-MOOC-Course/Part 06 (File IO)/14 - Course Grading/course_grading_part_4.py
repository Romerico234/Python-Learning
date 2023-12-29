def main():
    stdnt_info = input('Student information: ')
    exer_completed = input('Exercises completed: ')
    exam_points = input('Exam points: ')
    course_info = input('Course information: ')
    id_list = []

    student_dict = {}
    with open(stdnt_info) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            student_dict[parts[0]] = parts[1] + " " + parts[2]
            id_list.append(parts[0])
            
    exer_dict_count = {}
    exer_dict_points = {}
    with open(exer_completed) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            total = 0
            for i in parts[1:]:
                total += int(i)
            if total >= 40:
                points = 10
            elif total >= 36:
                points = 9
            elif total >= 32:
                points = 8
            elif total >= 28:
                points = 7
            elif total >= 24:
                points = 6
            elif total >= 20:
                points = 5
            elif total >= 16:
                points = 4
            elif total >= 12:
                points = 3
            elif total >= 8:
                points = 2
            elif total >= 4:
                points = 1
            else: 
                points = 0
            exer_dict_count[parts[0]] = total
            exer_dict_points[parts[0]] = points
    
    exam_dict = {}
    with open(exam_points) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            total = 0
            for i in parts[1:]:
                total += int(i)
            exam_dict[parts[0]] = total
    
    course = []
    with open(course_info) as new_file:
        for line in new_file:
            line = line.strip().split(": ")
            course.append(line[1])
            
    course_string = course[0] + ", " + course[1] + " credits"
    with open("results.txt", "w") as file:
        file.write(course_string+"\n")
        file.write("="*len(course_string)+"\n")
        file.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")   
        for i in id_list:
            total = exam_dict[i] + exer_dict_points[i]
            if total >= 28:
                grade = 5
            elif total >= 24:
                grade = 4
            elif total >= 21:
                grade = 3
            elif total >= 18:
                grade = 2
            elif total >= 15:
                grade = 1
            else:
                grade = 0
            file.write(f"{student_dict[i]:<30}{exer_dict_count[i]:<10}{exer_dict_points[i]:<10}{exam_dict[i]:<10}{total:<10}{grade:<10}\n")    
        
    with open("results.csv", "w") as file:
        for i in id_list:
            total = exam_dict[i] + exer_dict_points[i]
            if total >= 28:
                grade = 5
            elif total >= 24:
                grade = 4
            elif total >= 21:
                grade = 3
            elif total >= 18:
                grade = 2
            elif total >= 15:
                grade = 1
            else:
                grade = 0
            file.write(i+";"+student_dict[i]+";"+str(grade)+"\n")

    print("Results written to files results.txt and results.csv")
main()