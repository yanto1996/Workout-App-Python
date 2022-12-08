from workoutdict import *
from workout_generator import *
from workoutapp import *
import unittest
import random

# initialize unittest.TestCase
class Test_workoutapp(unittest.TestCase):

# tests with random seed, index 1 should = "2 x 4" if random is seeded 10
    def test_random_intensity(self):
        random.seed(10)
        b = random_intensity()
        self.assertEqual(b[1],"2 x 4")

# tests element [0] of final list to see if dictionary appended correctly
    def test_exercise_key(self):
        a = exercise_key()
        self.assertEqual(a[0],"Empty")

# tests the workout generator - it is technically already pre handled as it can only be values in dictionary
# Should raise assertion error if value is not something already in the dictionary
    def test_get_workout_today(self):
        x = workout.get_workout_today()
        with self.assertRaises(AssertionError) as exception_context:
            self.assertEqual(x, "test")

# test the url - if url is not real like a random string, it should throw None
    def test_url(self):
        z = add_bg_fromm_url("test")
        self.assertEqual(z, None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()