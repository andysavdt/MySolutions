import pandas as pd

cars = pd.read_csv('cars.csv', index_col = 0)

print (cars['cars_per_cap'])

print (cars[['cars_per_cap']])

print(cars[['cars_per_cap' , 'country']])

print(cars)
