from datetime import datetime
from typing import List
import json
import pandas as pd


class Exam:
    teacher: str
    exam_name: str
    exam_date: datetime
    room: str

    def __init__(self, teacher: str, exam_name: str, exam_date: datetime, room: str) -> None:
        self.teacher = teacher
        self.exam_name = exam_name
        self.exam_date = exam_date
        self.room = room


class Welcome1:
    exams: List[Exam]

    def __init__(self, exams: List[Exam]) -> None:
        self.exams = exams

with open("practice.json","r") as f:
    data = json.load(f)

print(data[5].values())
df = pd.read_json (r'practice.json')
df.to_csv (r'exam_table.csv',index=None)
