#!/usr/bin/python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"Result: {add(num1, num2)}")
elif operation == "-":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "*":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "/":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Unknown operation. Please use: +, -, *, or /.")