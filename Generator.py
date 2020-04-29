import tkinter as tk
from tkinter.filedialog import askopenfilename
import random

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

exercises = []

input('Welcome to RandomWorkoutGenerator! Press "enter" to open file chooser and choose a workout')

file_name = askopenfilename()
file_content = open(file_name,"r")

def addExercise(inputExercise):
    inputExercise = inputExercise.split(';')
    exercise_name = inputExercise[0]
    exercise_min_reps = int(inputExercise[2])
    exercise_max_reps = int(inputExercise[3])
    exercise = [exercise_name,exercise_min_reps,exercise_max_reps]
    exercise_sets = int(inputExercise[1])
    
    for x in range(0,exercise_sets):
        exercises.append(exercise)

for exe in file_content:
    addExercise(exe)

def startWorkout():
    random.shuffle(exercises)
    for exercise in exercises:
        input(exercise[0] + ': ' + str(random.randint(exercise[1],exercise[2])))   
    input('\nWorkout finished. Good job!')

startWorkout()
