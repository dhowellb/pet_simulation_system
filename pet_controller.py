# Part 1: Welcome sa Pet Clinic! Gawa muna tayo ng blueprint para sa Pet class. Naglagay ako ng constructor para may default na tambayan yung mga private variables natin habang wala pang input si user.
class Pet:
    def __init__(self, pet_name="Unknown", pet_type="Unknown", pet_age=0):
        self.__name = pet_name
        self.__animal_type = pet_type
        self.__age = int(pet_age)