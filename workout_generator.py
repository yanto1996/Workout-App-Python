import random
from workoutdict import *

# Chooses random number 1 to 2
chooser1 = random.choice(range(1,3))
chooser2 = random.choice(range(1,3))
chooser3 = random.choice(range(1,3))
chooser4 = random.choice(range(1,3))
chooser5 = random.choice(range(1,3))
chooser6 = random.choice(range(1,3))


class Workout:
    # constructor
    def __init__(self):
        self

    # getter method that has a optional attribute which randomizes the workouts with a chooser variable
    def get_workout_today(self, workout1=chooser1, workout2=chooser2, workout3=chooser3, workout4=chooser4,
    workout5=chooser5, workout6=chooser6):
        workout_list = []
        self.workout1 = workout1
        self.workout2 = workout2
        self.workout3 = workout3
        self.workout4 = workout4
        self.workout5 = workout5
        self.workout6 = workout6
        
        # depending on the value of the chooser, it will generate a random workout from the dictionary
        if chooser1 == 1:
            self.workout1 = exercise_dictionary[random.choice(upper)]
        elif chooser1 == 2:
            self.workout1 = exercise_dictionary[random.choice(lower)]
        if chooser2 == 1:
            self.workout2 = exercise_dictionary[random.choice(upper)]
        elif chooser2 == 2:
            self.workout2 = exercise_dictionary[random.choice(lower)]
        if chooser3 == 1:
            self.workout3 = exercise_dictionary[random.choice(upper)]
        elif chooser3 == 2:
            self.workout3 = exercise_dictionary[random.choice(lower)]
        if chooser4 == 1:
            self.workout4 = exercise_dictionary[random.choice(upper)]
        elif chooser4 == 2:
            self.workout4 = exercise_dictionary[random.choice(lower)]
        if chooser5 == 1:
            self.workout5 = exercise_dictionary[random.choice(upper)]
        elif chooser5 == 2:
            self.workout5 = exercise_dictionary[random.choice(lower)]
        if chooser6 == 1:
            self.workout6 = exercise_dictionary[random.choice(upper)]
        elif chooser6 == 2:
            self.workout6 = exercise_dictionary[random.choice(lower)]

        # checks to see if there are repeats in the workouts, if there are it will go back and choose again
        while self.workout1 == self.workout2 or self.workout1 == self.workout3 or self.workout1 == self.workout4 or self.workout1 == self.workout5 or self.workout1 == self.workout6:
                if chooser1 == 1:
                    self.workout1 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout1 = exercise_dictionary[random.choice(lower)]    

        while self.workout2 == self.workout1 or self.workout2 == self.workout3 or self.workout2 == self.workout4 or self.workout2 == self.workout5 or self.workout2 == self.workout6:
                if chooser1 == 1:
                    self.workout2 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout2 = exercise_dictionary[random.choice(lower)] 

        while self.workout3 == self.workout1 or self.workout3 == self.workout2 or self.workout3 == self.workout4 or self.workout3 == self.workout5 or self.workout3 == self.workout6:
                if chooser1 == 1:
                    self.workout3 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout3 = exercise_dictionary[random.choice(lower)]          

        while self.workout4 == self.workout1 or self.workout4 == self.workout2 or self.workout4 == self.workout3 or self.workout4 == self.workout5 or self.workout4 == self.workout6:
                if chooser1 == 1:
                    self.workout4 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout4 = exercise_dictionary[random.choice(lower)]     

        while self.workout5 == self.workout1 or self.workout5 == self.workout2 or self.workout5 == self.workout3 or self.workout5 == self.workout4 or self.workout5 == self.workout6:
                if chooser1 == 1:
                    self.workout5 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout5 = exercise_dictionary[random.choice(lower)]  

        while self.workout6 == self.workout1 or self.workout6 == self.workout2 or self.workout6 == self.workout3 or self.workout6 == self.workout5 or self.workout6 == self.workout4:
                if chooser1 == 1:
                    self.workout6 = exercise_dictionary[random.choice(upper)]  
                else:
                    self.workout6 = exercise_dictionary[random.choice(lower)]  

        # for loop to append the workout attributes to a list
        for i in range(1):
            workout_list.append(self.workout1)
            workout_list.append(self.workout2)
            workout_list.append(self.workout3)
            workout_list.append(self.workout4)
            workout_list.append(self.workout5)
            workout_list.append(self.workout6)

        # returns the list of workouts based 
        return workout_list

workout = Workout()