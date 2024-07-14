import numpy as np
import matplotlib.pyplot as plt
import scorpion_tgs_matrix as stm

data = open('test.txt', 'r')

count_matrix = np.array([[0.0] * 8] * 8)
energy_matrix = np.array([[0.0] * 8] * 8)

for i in data:
    string = data.readline().split(', ')
    string = [line.rstrip() for line in string]
    string = list(map(float, string))
    stm.create_energy_matrix(energy_matrix, string)
    stm.create_events_count_matrix(count_matrix, string)

print("ENERGY SUMMARY MATRIX:")
print(energy_matrix)
print("COUNT SUMMARY MATRIX:")
print(count_matrix)

fig, ax = plt.subplots()

cax = ax.imshow(count_matrix, cmap='YlOrBr', interpolation='none')

fig.colorbar(cax)

# plt.title("Распределение количества регистрации на матрице GAGG:Cr +Pol 1МэВ 0deg:")
plt.show()
