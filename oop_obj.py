#!/usr/bin/env python3
class Robot:
    pass

x = Robot()
y = Robot()
x.name = "GPT-1"
x.year = "1999"
y.name = "GPT-2"
y.year = "2000"
print(f"{x.name} is made in {x.year} and {y.name} is made in {y.year}")
print(x.__dict__)
print(y.__dict__)
print(Robot.__dict__)