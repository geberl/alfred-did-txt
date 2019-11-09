#!/usr/local/bin/python3

import datetime
import sys

# TODO make this dynamic
RESULTS_FILE = "/Users/guenther/Library/Mobile Documents/com~apple~CloudDocs/Documents/did.txt"


def calc_attendance_times(separator="---"):
    with open(file=RESULTS_FILE, mode="r") as file_handler:
        input_lines = file_handler.readlines()

    output_lines = []
    last_arrive_datetime = None
    last_leave_datetime = None
    attendance_already_calculated = False

    for line in input_lines:
        if line.strip() == separator:
            # Calculate attendance time when encountering a separator
            if last_arrive_datetime != None and last_leave_datetime != None and attendance_already_calculated == False:
                time_difference = last_leave_datetime - last_arrive_datetime
                date_string = last_leave_datetime.strftime("%Y-%m-%d")
                output_lines.append("%s 23:59:59 - attendance (TODO account for breaks) %s" % (date_string, time_difference))

            # Never get rid of the separator
            output_lines.append(separator)

            # Always reset variables that hold times of previous lines
            last_arrive_datetime = None
            last_leave_datetime = None
            attendance_already_calculated = False

            continue

        line_segments = line.strip().split(" - ")
        date_string = line_segments[0]

        keyword_string = line_segments[1]
        this_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

        if keyword_string.startswith("arrive"):
            last_arrive_datetime = this_datetime
        elif keyword_string.startswith("leave"):
            last_leave_datetime = this_datetime
        elif keyword_string.startswith("attendance"):
            attendance_already_calculated = True
    
        output_lines.append(line.strip())
    
    with open(file=RESULTS_FILE, mode="w") as file_handler:
        for line in output_lines:
            file_handler.write("%s\n" % line)


def format_results(separator="---"):
    with open(file=RESULTS_FILE, mode="r") as file_handler:
        input_lines = file_handler.readlines()
    
    output_lines = []
    last_date = None

    for line in input_lines:
        if line.strip() == separator:
            continue
        
        date_string = line.strip().split(" - ")[0]
        this_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").date()

        if last_date != None:
            if last_date.day != this_date.day:
                output_lines.append(separator)
        last_date = this_date
        
        output_lines.append(line.strip())
    
    with open(file=RESULTS_FILE, mode="w") as file_handler:
        for line in output_lines:
            file_handler.write("%s\n" % line)


def append_message(message="n/a"):
    current_datetime = datetime.datetime.today()
    with open(file=RESULTS_FILE, mode="a") as file_handler:
        file_handler.write("%s - %s\n" % (current_datetime.isoformat(" ", "seconds"), message))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # The called script itself is always argument 0, so len is always at least 1.
        append_message()
    elif len(sys.argv) == 2:
        append_message(message=str(sys.argv[1]))
    else:
        print("Only pass one message")

    format_results()
    calc_attendance_times()
