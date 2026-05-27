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

        # Part 4: Kung may setters, siyempre kailangan ng getters (accessors). Dito natin huhugutin yung pangalan at klase ng hayop kapag kailangan na natin ipagmalaki sa mga kapitbahay.
    def get_name(self):
        return self.__name
        
    def get_animal_type(self):
        return self.__animal_type
    
    # Part 5: Eto yung huling getter para sa edad. Pati yung pag-setup ng main testing function natin para maayos yung flow ng program pag-run sa terminal.
    def get_age(self):
        return self.__age
        

def test_pet_program():
    print("\n[ WELCOME TO THE VIRTUAL PET CLINIC ]\n")

    # Part 6: Oras na para mag-interview! Kukunin natin sa user yung name, type, at age ng pet nila. Gagamit tayo ng descriptive snake_case variables para malinis basahin at walang magagalit.
    user_input_name = input("Enter the name of your pet: ")
    user_input_type = input("Enter the type of animal (e.g., Dog, Cat, Capybara): ")
    user_input_age = input("Enter the age of your pet: ")

    # Part 7: Ang finale! Gagawa tayo ng Pet object, gagamitin ang setters para i-save ang input, at ang getters (accessors) para i-display yung final ID gaya ng inutos ng instructions. Run na natin!
    my_new_pet = Pet()
    
    my_new_pet.set_name(user_input_name)
    my_new_pet.set_animal_type(user_input_type)
    my_new_pet.set_age(user_input_age)
    
    print("\n🐾 ==== OFFICIAL PET RECORD ==== 🐾")
    print(f"| Pet Name    : {my_new_pet.get_name()}")
    print(f"| Animal Type : {my_new_pet.get_animal_type()}")
    print(f"| Pet Age     : {my_new_pet.get_age()} years old")
    print("=================================\n")
    

if __name__ == "__main__":
    test_pet_program()