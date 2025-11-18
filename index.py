import sys
import random as r
import streamlit as st

class Student:
    def __init__(self, name, level, subjects):
        self.name = name
        self.level = level
        self.subjects = subjects

def ReadSubjectFile(subject, level):
    try: return open(subject + '_level' + level + '.txt', 'r').read().splitlines()
    except Exception as e: print(e); exit()

def CleanTasks(all_level_tasks):
    return [level for level in all_level_tasks if len(level) and 'END' not in level]

def XTasks(tasks, x):
    return r.sample(tasks, x)

def PrintTasks(tasks):
    for task in tasks: st.write(f'{task}')

def greet(name, level, subject):
    s1 = Student(name, level, subject)
    st.header(f"Welcome {s1.name} to your Dynamic Homework Generator:\nYou are at Level {s1.level} and Subjects {s1.subjects}")
    Tasks = CleanTasks(ReadSubjectFile('german', '1'))
    PrintTasks(XTasks(Tasks, 1))

greet('Johnny', 1, 'german')