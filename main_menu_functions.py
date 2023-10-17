import csv
import os

file_name = 'notes.csv'


def create_notes_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow(['Name', 'Note', 'Date', 'Time'])


