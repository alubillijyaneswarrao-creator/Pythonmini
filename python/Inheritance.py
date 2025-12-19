class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        self.is_alive = True
    def make_sound(self):
        printf(f"{self.name} makes a sound")
    def info(self):
        return f"{self.name} is a {self.species}."
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"Dog")
        self.breed=breed
    def make_sound(self):
        return "Woof!"
    def info(self):
        return f"{self.name} is a {self.breed} dog."
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name,"Cat")
        self.color=color
    def make_sound(self):
        return "Meow!"
    def info(self):
        return f"{self.name} is a {self.color} cat."

dog = Dog("Buddy","Golden Retriever") 
cat = Cat("Whiskers","Tabby")
dog_sound = dog.make_sound()
cat_sound = cat.make_sound()
dog_info = dog.info()
cat_info = cat.info()
print(dog_sound)  
print(cat_sound)  
print(dog_info)  
print(cat_info)   
