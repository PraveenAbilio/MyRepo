# 8.Write a program to read two matrices of order 3 * 2, add them and display the resultant matrix in matrix form

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

result = [[X[i][j] + Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

for r in result:
	print(r)


# 9.Write a python program to multiply two 3*3 matrixes.

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):

   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


# 10.Create a class called cricketer with member variables to represent name, age and no of matches played. From this class derive two classes: Bowler and Batsman. Bowler class has no_of_wickets as member variable and Batsman class has no_of_runs and centuries as member variables. Use appropriate member functions in all classes to read and display respective data.


# class Cricketer:
#     def __init__(self, name, age, matches_played):
#         self.name = name
#         self.age = age
#         self.matches_played = matches_played

#     def read_data(self):
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.matches_played = int(input("Enter number of matches played: "))

#     def display_data(self):
#         print(f"\nName: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Matches Played: {self.matches_played}")


# class Bowler(Cricketer):
#     def __init__(self, name, age, matches_played, no_of_wickets):
#         super().__init__(name, age, matches_played)
#         self.no_of_wickets = no_of_wickets

#     def read_data(self):
#         super().read_data()
#         self.no_of_wickets = int(input("Enter number of wickets: "))

#     def display_data(self):
#         super().display_data()
#         print(f"No. of Wickets: {self.no_of_wickets}")


# class Batsman(Cricketer):
#     def __init__(self, name, age, matches_played, no_of_runs, centuries):
#         super().__init__(name, age, matches_played)
#         self.no_of_runs = no_of_runs
#         self.centuries = centuries

#     def read_data(self):
#         super().read_data()
#         self.no_of_runs = int(input("Enter number of runs: "))
#         self.centuries = int(input("Enter number of centuries: "))

#     def display_data(self):
#         super().display_data()
#         print(f"No. of Runs: {self.no_of_runs}")
#         print(f"No. of Centuries: {self.centuries}")


# # Example usage:
# if __name__ == "__main__":
#     # Create objects of Bowler and Batsman classes
#     bowler = Bowler("", 0, 0, 0)
#     batsman = Batsman("", 0, 0, 0, 0)

#     # Read and display data for Bowler
#     print("\nEnter details for Bowler:")
#     bowler.read_data()
#     bowler.display_data()

#     # Read and display data for Batsman
#     print("\nEnter details for Batsman:")
#     batsman.read_data()
#     batsman.display_data()





# 11.Create a class called 'TIME' that has two integer data members for Hours, Minutes initialized using a constructor. Create two objects of this class as t1 and t2. i)Using function to return the proper sum of two times.(i.e.60 minutes =1 hour)., and also                                ii)Overload '+' operator to add the times of two obects and return in proper format.                             iii)overload print function also to display the time.



# class TIME:
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours
#         self.minutes = minutes

#     def add_times(self, t1, t2):
#         total_minutes = t1.hours * 60 + t1.minutes + t2.hours * 60 + t2.minutes
#         hours_sum = total_minutes // 60
#         minutes_sum = total_minutes % 60
#         return TIME(hours_sum, minutes_sum)

#     def __add__(self, other):
#         total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
#         hours_sum = total_minutes // 60
#         minutes_sum = total_minutes % 60
#         return TIME(hours_sum, minutes_sum)

#     def __str__(self):
#         return f"{self.hours} hours and {self.minutes} minutes"

# # Create two objects of the TIME class
# t1 = TIME(2, 30)
# t2 = TIME(1, 45)

# # Using function to return the proper sum of two times
# sum_using_function = TIME().add_times(t1, t2)
# print("Sum using function:", sum_using_function)

# # Overload '+' operator to add the times of two objects
# sum_overloaded_operator = t1 + t2
# print("Sum using overloaded operator:", sum_overloaded_operator)

# # Overload print function to display the time
# print("t1:", t1)
# print("t2:", t2)





# 12.Overload '-' operator to change the vector(x,y,z) to (-x,-y,-z).

# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __neg__(self):
#         return Vector(-self.x, -self.y, -self.z)

#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"


# # Create a Vector object
# v1 = Vector(2, 3, 4)

# # Overload '-' operator to change the sign of the vector
# negated_vector = -v1

# # Display the original and negated vectors
# print("Original Vector:", v1)
# print("Negated Vector:", negated_vector)



# 13.Overload '>=' operator to compare two vector.


# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __ge__(self, other):
#         # Compare vectors based on their magnitudes
#         return self.magnitude() >= other.magnitude()

#     def magnitude(self):
#         # Calculate the magnitude of the vector
#         return (self.x**2 + self.y**2 + self.z**2)**0.5

#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"

# # Create two Vector objects
# v1 = Vector(2, 3, 4)
# v2 = Vector(1, 2, 3)

# # Compare vectors using the '>=' operator
# result = v1 >= v2

# # Display the vectors and the result of the comparison
# print("Vector v1:", v1)
# print("Vector v2:", v2)
# print("Is v1 >= v2?", result)



# 14.Write a program to display Fibonacci series of last term up to 300.


# def fibonacci_series(limit):
#     fib_series = [0, 1]
    
#     while fib_series[-1] + fib_series[-2] <= limit:
#         next_term = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_term)
    
#     return fib_series

# # Set the limit for the last term
# limit = 300

# # Display Fibonacci series up to the last term less than or equal to the limit
# result = fibonacci_series(limit)
# print("Fibonacci Series up to the last term less than or equal to 300:")
# print(result)





# 15.WAP to generate 3 12 27 48 ................10th term



def generate_sequence(n):
    sequence = [1]  # Initialize with the first term

    for i in range(2, n + 1):
        term = sequence[-1] + i**3
        sequence.append(term)

    return sequence

# Generate and print the sequence up to the 10th term
result = generate_sequence(10)
print("Generated Sequence:", result)