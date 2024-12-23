class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
car1= Car("kia" , "jack" , 2019)
car2= Car("honda" , "camry" , 2023)
car3= Car("ford" , "civic" , 2021)

print(f" car1: {car1.make}{car1.model}{car1.year}")
print(f" car2: {car2.make}{car2.model}{car2.year}")
print(f" car3: {car3.make}{car3.model}{car3.year}")
