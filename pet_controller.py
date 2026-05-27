# Part 1: Welcome sa Pet Clinic! Gawa muna tayo ng blueprint para sa Pet class. Naglagay ako ng constructor para may default na tambayan yung mga private variables natin habang wala pang input si user.
class Pet:
    def __init__(self, pet_name="Unknown", pet_type="Unknown", pet_age=0):
        self.__name = pet_name
        self.__animal_type = pet_type
        self.__age = int(pet_age)

        # Part 2: Eto na yung mga setters natin para sa pangalan at type ng hayop. Para kapag naisipan mong palitan yung pangalan ng aso mo from 'Bantay' to 'Dogzilla', pwedeng-pwede at safe ang data.
    def set_name(self, pet_name):
        self.__name = pet_name
        
    def set_animal_type(self, pet_type):
        self.__animal_type = pet_type

        # Part 3: Hiwalay na setter para sa age. Nilagyan ko ng int() cast para sure na number yung papasok, baka kasi may mag-type ng salitang 'twenty' tapos mag-collapse yung system natin.
    def set_age(self, pet_age):
        self.__age = int(pet_age)