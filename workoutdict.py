import random

# key value variables to access dictionary randomizer 
upper = [0,1,2,3,4,5,6,7,8,9]
lower = ["a", "b", "c", "d", "e", "f","g", "h", "i" ]
intensity_list = ["2 x 4", "3 x 5", "5 x 5", "2 x 8", "4 x 8", "4 x 10", "5 x 10"]

# dictionary of workouts
exercise_dictionary = {"z": "Empty", 0: "Bicep curls", 1: "Preacher ez-bar Curl", 2: "Cable pushdown", 3: "Bench Press", 4: "T Bar Row",
5: "Pull ups", 6: "ez-bar Skull crushers", 7: "Rope cable overhead extension", 8: "Incline bench press", 9: "Overhead press",
"a": "Back squat", "b": "Front squat", "c": "Lunges", "d": "Deadlift", "e": "Leg press", "f": "Bulgarian split squats",
"g": "Leg curls", "h": "Back squat pause rep", "i": "Calf raises" }

# returns value from dictionary
def exercise_key():
    exercise_list = []
    for key, value in exercise_dictionary.items():
        exercise_list.append(value)
    return exercise_list
    
# appends 6 random intensity elements into a list
def random_intensity():
    random_intensity_list = []
    for i in range(6):
        random_intensity_list.append(intensity_list[random.randint(0,6)])
    return random_intensity_list