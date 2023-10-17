import csv
import os

file_name = 'notes.csv'


def create_notes_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow(['Name', 'Note', 'Date', 'Time'])


def list_notes(file_path, filter_date=None):
    notes = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        notes = list(csv_reader)
    if filter_date:
        notes = [note for note in notes if note[2] == filter_date]
    return notes

