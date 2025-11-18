import sys
import random as r
import streamlit as st

class Student:
    def __init__(self, name, level, subjects):
        self.name = name
        self.level = level
        self.subjects = subjects

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
    return st.session_state['all_files'][subject][f'level{level}']

def CleanTasks(all_level_tasks):
    if all_level_tasks == None: return None
    return ''.join(all_level_tasks).split('**=END=**')

def XTasks(tasks, x):
    if x <= len(tasks): return r.sample(tasks, x)
    return r.sample(tasks, len(tasks))

def PrintTasks(subjects):
    level = str(st.slider('Waehle das Level aus:', 1, 3))
    amount = st.slider('Waehle wieviele Aufgaben:', 1, 10)
    subject = st.selectbox(label="Waehle das Fach: ", options=subjects, index=0)
    Tasks = CleanTasks(ReadSubjectFile(subject, level))
    if Tasks == None: st.error("File not found"); exit()
    tasks = XTasks(Tasks, amount)
    for task in tasks: st.write(f'{task}')

def greet(name):
    st.header(f"Welcome {name} to your Dynamic Teaching Generator:\n")

def run(name, level, subjects):
    s1 = Student(name, level, subjects)
    greet(s1.name)
    PrintTasks(s1.subjects)

if __name__ == '__main__':
    subjects = ['german', 'english', 'math', 'art']
    ReadAllFiles(subjects)
    run('Johnny', 5, subjects)