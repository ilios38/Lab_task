import csv
import json

input_filename = "input.csv"
output_filename = "output.json"

def task():

    with open(input_filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = [row for row in csv_reader]

    with open(output_filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    task()

    with open(output_filename) as output_file:
        for line in output_file:
            print(line, end="")

