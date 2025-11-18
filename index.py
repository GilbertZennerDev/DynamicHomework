import sys
import random as r
import streamlit as st

class Student:
    def __init__(self, name):
        self.name = name

def ReadAllFiles(subjects):
    if 'all_files' in st.session_state: return
    print("Reading from Disk")
    all_files = {}
    for subject in subjects:
        all_files[subject] = {}
        for level in range(1, 11):
            try: all_files[subject][f'level{str(level)}'] = open("subjects/" + subject + '/' + subject + '_level' + str(level) + '.txt', 'r').read().splitlines()
            except Exception as e: print(e); continue
    st.session_state['all_files'] = all_files

def ReadSubjectFile(subject, level):
    return st.session_state['all_files'][subject][f'level{str(level)}']

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
    ReadAllFiles(subjects)
    run('Johnny', subjects)