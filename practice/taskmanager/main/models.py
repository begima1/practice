from datetime import datetime
from typing import List
import json
import pandas as pd

from django.db import models

class Task(models.Model):
    title = models.CharField('Name',max_length=50)
    tsk = models.TextField('description')

    def __str__(self):
        return self.title

    with open('/home/comp10/Desktop/practice/taskmanager/main/practice.json',"r") as f:
        data = json.load(f)

    print(data[1].values())
    df = pd.read_json (r'/home/comp10/Desktop/practice/taskmanager/main/practice.json')
    df.to_csv (r'/home/comp10/Desktop/practice/taskmanager/main/exam_table.csv',index=None)