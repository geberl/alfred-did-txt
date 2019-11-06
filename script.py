#!/usr/bin/env python3

import datetime
import sys

RESULTS_FILE = "/Users/guenther/Library/Mobile Documents/com~apple~CloudDocs/Documents/did.txt"

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
