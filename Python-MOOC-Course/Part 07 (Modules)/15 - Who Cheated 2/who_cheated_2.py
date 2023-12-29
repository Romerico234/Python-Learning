import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student time and points is saved to a dictionary
        # Time and points is saved as tuple.
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
 
            # If cheating has happened, submission is not handled
            if time - start_times[name] > timedelta(hours=3):
                continue
 
            # If student is not handled yet, add student directly to the dictionary
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
 
            # If student already exists, more points than earlier is required
            elif p > points[name][tno]:
                points[name][tno] = p
 
        final_points = {}
        # Iterate through students one by one
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
 
        return final_points