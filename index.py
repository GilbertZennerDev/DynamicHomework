import sys
import random as r
import streamlit as st

class Student:
    def __init__(self, name):
        self.name = name

def ReadAllFiles(subjects):
    all_files = []
    for subject in subjects:
        for level in range(1, 11):
            open("subjects/" + subject + '/' + subject + '_level' + level + '.txt', 'r').read().splitlines()

def ReadSubjectFile(subject, level):
    try: return open("subjects/" + subject + '/' + subject + '_level' + level + '.txt', 'r').read().splitlines()
    except Exception as e: print(e); return -1

def CleanTasks(all_level_tasks):
    if all_level_tasks == -1: return -1
    return [level for level in all_level_tasks if len(level) and 'END' not in level]

def XTasks(tasks, x):
    if x <= len(tasks): return r.sample(tasks, x)
    return r.sample(tasks, len(tasks))

def PrintTasks(subjects):
    level = st.slider('Waehle das Level aus:', 1, 10)
    amount = st.slider('Waehle wieviele Aufgaben:', 1, 30)
    subject = st.selectbox(label="Waehle das Fach: ", options=subjects, index=0)
    Tasks = CleanTasks(ReadSubjectFile(subject, str(level)))
    if Tasks == -1: st.error("File not found"); exit()
    tasks = XTasks(Tasks, amount)
    for task in tasks: st.write(f'{task}')

def greet(name):
    s1 = Student(name)
    st.header(f"Welcome {s1.name} to your Dynamic Homework Generator:\n")

def run(name, subjects):
    greet(name)
    PrintTasks(subjects)

if __name__ == '__main__':
    subjects = ['german', 'english', 'math', 'art']
    run('Johnny', subjects)