import csv
import datetime
import os

from airtable import Airtable

base_key = 'yourbasekey'
api_key = 'yourapikey'

app_time_table = Airtable(base_key, 'AppTime', api_key=api_key)
students_table = Airtable(base_key, 'Students', api_key=api_key)
students = students_table.get_all()
students_lookup = {student["fields"]["Name"]: student["id"] for student in students}

if __name__ == '__main__':
    """
    name = "Connor"
    student_id = students_lookup.get(name)
    row = {
        "Students": [student_id],
        "StartTime": (datetime.datetime.now() - datetime.timedelta(hours=1)).isoformat(),
        "EndTime": datetime.datetime.now().isoformat()
    }
    app_time_table.insert(row)
    """
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), 'parker.csv'))
    file_location = location
    with open(file_location) as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            name = f'{row.get("First Name")} {row.get("Last Name")}'
            if students_lookup.get(name) is None:
                row_to_insert = {
                    "Name": name
                }
                students_table.insert(row_to_insert)
            else:
                print(f'{name} already exists.')
