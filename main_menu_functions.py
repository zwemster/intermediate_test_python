import csv
import os
from datetime import datetime

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


def add_note(file_path, title, body):
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        csv_writer.writerow([title, body, current_date, current_time])


def edit_note(file_path, title, new_title, new_body):
    notes = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        notes = list(csv_reader)

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        csv_writer.writerow(['Name', 'Note', 'Date', 'Time'])
        for note in notes[1:]:
            if note[0] == title:
                csv_writer.writerow([new_title, new_body, note[2], note[3]])
            else:
                csv_writer.writerow(note)

