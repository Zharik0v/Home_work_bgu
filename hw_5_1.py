import random

class Animal:
    def __init__(self, name, habitat, diet, size, lifespan, sex, age=0, satiety=100, alive=True):
        self.name = name
        self.size = size
        self.sex = sex
        self.diet = diet
        self.satiety = satiety
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = age
        self.alive = alive
    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Size: {self.size}\n'
                f'Habitat: {self.habitat}\n'
                f'Diet: {self.diet}\n'
                f'Lifespan: {self.lifespan}\n'
                f'Age: {self.age}\n'
                f'Fullness: {self.satiety}\n'
                f'Alive: {self.alive}\n'
                f'Sex: {self.sex}')

class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def increase_food(self, amount):
        self.plant_food += amount
        print(f'Food left: {self.plant_food}')

    def reproduce(self, animal_1, animal_2):
        if animal_1.name == animal_2.name and not(animal_1.sex == animal_2.sex):
            if animal_1.habitat == "Water":
                if animal_1.satiety > 50 and animal_2.satiety > 50:
                    for i in range(5):
                        self.add_animal(Animal(animal_1.name, animal_1.size, animal_1.diet,
                                               animal_1.habitat, animal_1.lifespan, animal_1.sex, 23))
                        self.add_animal(Animal(animal_2.name, animal_2.size, animal_2.diet,
                                               animal_2.habitat, animal_2.lifespan, animal_2.sex, 23))
                    print(f'There are 10 new animals! : {animal_1.name}')
                else:
                    print('Animals cannot reproduce because of lack of satiety:(')

            elif animal_1.habitat == "Sky":
                if animal_1.satiety > 42 and animal_2.satiety > 42 and animal_1.age > 3 and animal_2.age > 3:
                    for i in range(2):
                        self.add_animal(Animal(animal_1.name, animal_1.size, animal_1.diet,
                                               animal_1.habitat, animal_1.lifespan, animal_1.sex, animal_1.alive, 64))
                        self.add_animal(Animal(animal_2.name, animal_2.size, animal_2.diet,
                                               animal_2.habitat, animal_2.lifespan, animal_2.sex, animal_2.alive, 64))
                        print(f'There are 4 new animals! : {animal_1.name}')

                else:
                    print('Animals cannot reproduce because of lack of satiety:(')
            else:
                if animal_1.satiety > 20 and animal_2.satiety > 20 and animal_1.age > 5 and animal_2.age > 5:
                    self.add_animal(Animal(animal_1.name, animal_1.size, animal_1.diet,
                                           animal_1.habitat, animal_1.lifespan, animal_1.sex, animal_1.alive, 73))
                    self.add_animal(Animal(animal_2.name, animal_2.size, animal_2.diet,
                                           animal_2.habitat, animal_2.lifespan, animal_2.sex, animal_2.alive, 73))
                    print(f'There are 2 new animals! : {animal_1.name}')
                else:
                    print('Animals cannot reproduce because of lack of satiety:(')
        else:
            print('These anumals cannot reproduce!')

    def time_step_simulation(self):
        new_animals = []
        animals_to_remove = []
        for animal in self.animals:
            animal.age += 1
            if animal.age >= animal.lifespan:
                if animal.size == "Large":
                    self.increase_food(100)
                elif animal.size == "Medium":
                    self.increase_food(50)
                else:
                    self.increase_food(10)
                continue

            if animal.diet == "Plant food":
                if self.plant_food > 0:
                    self.plant_food -= 1
                    animal.satiety += 26
                else:
                    animal.satiety -= 9
            else:
                if random.random() < 0.5:
                    random_animal = random.choice(self.animals)
                    if random_animal != animal and random_animal.habitat == animal.habitat:
                        if random.random() < 0.5:
                            random_animal.alive = False
                            animals_to_remove.append(random_animal)
                            animal.satiety += 53
                        else:
                            animal.satiety -= 16
                else:
                    animal.satiety -= 9

            if animal.satiety < 10:
                if animal.size == "Large":
                    self.increase_food(100)
                elif animal.size == "Medium":
                    self.increase_food(50)
                else:
                    self.increase_food(10)
            else:
                new_animals.append(animal)

        for animal in self.animals:
            if not(animal.alive):
                self.animals.remove(animal)

        self.animals = new_animals


if __name__ == "__main__":
    ecosystem = Ecosystem()
    animals = [
        Animal('Platypus', 'Medium', 'Meat', 'Water', 20, 'm', 100, 5, True),
        Animal('Platypus', 'Medium', 'Meat', 'Water', 20, 'f', 100, 5, True),
        Animal("Орел", 'Medium', 'Meat', 'Sky', 20, 'm', 100, 3),
        Animal("Орел", 'Medium', 'Meat', 'Sky', 20, 'f', 100, 3),
        Animal('Clownfish', 'Small', 'Plant food', 'Water', 10, 'm', 1, True),
        Animal('Clownfish', 'Small', 'Plant food', 'Water', 10, 'f', 1, True),
        Animal('Ostrich', 'Large', 'Plant food', 'Ground', 60, 'm', 20, True),
        Animal('Ostrich', 'Large', 'Plant food', 'Ground', 60, 'f', 20, True),
        Animal('Whale', 'Large', 'Meat', 'Water', 90, 'm', 5, True),
        Animal('Whale', 'Large', 'Meat', 'Water', 90, 'f', 4, True),
        Animal('Tiger', 'Medium', 'Meat', 'Ground', 12, 'm', 1, True),
        Animal('Tiger', 'Medium', 'Meat', 'Ground', 12, 'f', 1, True)
    ]

    for animal in animals:
        ecosystem.add_animal(animal)

    for i in range(len(ecosystem.animals)):
        print(f'\nAmimal {str(i+1)}\n{ecosystem.animals[i]}')

    while True:
        print('\n\na. Add animal')
        print('b. Add food plant')
        print('c. View characteristics of the special animal')
        print('d. View characteristics of animals')
        print('f. Reproduce animals')
        print('g. Add 1 year')
        print('x. Exit')
        choice = input('Please, enter the letter: ')

        if choice == 'a':
            species = input('Name of the animal: ')
            size = input('Size: ')
            diet = input('Diet: ')
            habitat = input('Habitat: ')
            lifespan = int(input('Lifespan: '))
            sex = input('Sex: ')
            ecosystem.add_animal(Animal(species, size, diet, habitat, lifespan, sex))

        elif choice == 'b':
            amount = int(input("Enter the amount of food to add: "))
            ecosystem.increase_food(amount)

        elif choice == 'c':
            n = int(input('Enter the number of the animal: '))
            if 1 <= n <= len(ecosystem.animals):
                print(f'\nAnimal {str(n)}\n{ecosystem.animals[n-1]}')
            else:
                print('Such animal does not exist')

        elif choice == 'd':
            for i in range(len(ecosystem.animals)):
                print(f'\nAnimal {str(i + 1)}\n{ecosystem.animals[i]}')

        elif choice == 'e':
            n1 = int(input('Enter the number of the 1st animal: '))
            n2 = int(input('Enter the nuber of the 2nd animal: '))
            if 1 <= n1 <= len(ecosystem.animals) and 1 <= n2 <= len(ecosystem.animals):
                ecosystem.reproduce(ecosystem.animals[n1-1], ecosystem.animals[n2-1])
            else:
                print('Invalid number!')

        elif choice == 'f':
            ecosystem.time_step_simulation()

        elif choice == 'x':
            break

        else:
            print('Not exist')