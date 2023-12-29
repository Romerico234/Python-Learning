import urllib.request
import json
 
def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats/api/courses")
    course_data = json.loads(request.read())
    courses = []
    for course in course_data:
        if not course['enabled']:
            continue
 
        exercises = 0
        for exercise in course['exercises']:
            if exercise:
                exercises += exercise
 
        courses.append((course['fullName'], course['name'], course['year'], exercises))
 
    return courses
 
def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats/api/courses/{course_name}/stats")
    course_weeks = json.loads(request.read())
    students = 1
    exercises = 0
    hours = 0 
    for no, week in course_weeks.items():
        if week['students'] > students:
            students = week['students']
        hours += week['hour_total']
        exercises += week['exercise_total']
 
    return {
        "weeks": len(course_weeks),
        "students": students,
        "hours": hours,
        "hours_average": hours//students,
        "exercises": exercises,
        "exercises_average": exercises//students,
    }
