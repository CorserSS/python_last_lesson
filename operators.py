import random

cars = ["BMW", "Mercedes", "Lada"," Renault", "Haval", "Cherry", "Honda", "Chevrole", "Nissan"]

a = str(input('Введите марку машины\n'))

print('Есть' if a in cars else 'Нет')