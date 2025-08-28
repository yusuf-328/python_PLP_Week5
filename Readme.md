<!-- Assignment 1: Design Your Own Class! 🏗
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈). -->

# Smartphone & GamingSmartphone Python Classes

This project demonstrates basic object-oriented programming concepts in Python using classes to represent smartphones and gaming smartphones.

## Features
- **Smartphone class**: Represents a generic smartphone with brand, model, and storage attributes. Includes methods to display information and simulate making a call.
- **GamingSmartphone class**: Inherits from Smartphone and adds a GPU attribute. Includes a method to simulate playing a game.
- **Object creation**: Shows how to instantiate both classes and use their methods.

## Usage
1. Run `class.py` in your Python environment.
2. The script will:
   - Create a `Smartphone` object and display its info and call a number.
   - Create a `GamingSmartphone` object and display its info and simulate playing a game.

## Example Output
```
Apple iPhone 15 with 256GB storage.
Apple iPhone 15 is calling 08012345678...
Asus ROG Phone 7 with 512GB storage.
Playing Call of Duty Mobile on Asus ROG Phone 7 with Adreno 740 GPU.
```

## How It Works
- The `Smartphone` class defines basic phone properties and actions.
- The `GamingSmartphone` class extends `Smartphone` to add gaming capabilities.
- Demonstrates inheritance, method overriding, and object instantiation in Python.

## Requirements
- Python 3.x

## Author
- Example for OOP concepts in Python.