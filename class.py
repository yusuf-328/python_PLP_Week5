# Class representing a Smartphone
class Smartphone:
    def _init_(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."
    
    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."


# Inheritance Example: GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def _init_(self, brand, model, storage, gpu):
        super()._init_(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU."


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, "Adreno 740")

print(phone1.info())
print(phone1.call("08012345678"))

print(phone2.info())
print(phone2.play_game("Call of Duty Mobile"))