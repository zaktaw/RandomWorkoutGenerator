# RandomWorkoutGenerator

 A script used to generate random workouts
 
 The script loads a text file containing information about which exercises the workout should inclide, how many sets each exercise has and the minmum and maximum repetitions of each exercise.  
 The script will then randomize the order of the sets and number of repetitions for each exercise.  
 The user can choose from different workouts located in the "Example workouts" directory or make their own workout files.  

How to open:

Download and extract zip package.  
Run Generator.py (requires Python to be installed on computer).

How to use:

When opening the script, press enter and a file dialog will be opened.  
Choose one of the workouts located in the "Example workouts" directory.  
Press 'enter' to go through the workout sets.  

How to create your own workout:

Make a new text file.  
Write the workout in the following format:

Exercise 1;number of sets;minimum reps;maximum reps  
Exercise 2;number of sets;minimum reps;maximum reps  
Exercise 3;number of sets;minimum reps;maximum reps  

Make sure the text file does not include any blank lines and that every exercise starts on a new line.

Example:

Pull-ups;3;5;8  
Push-ups;3;8;12  
Squats;3;10;15  
