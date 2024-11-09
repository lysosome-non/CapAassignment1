import matplotlib.pyplot as plt

Tom = [62,67,65,78,80,74,76,83,85,78,88,89]
Peter = [87,63,67,78,71,62,88,72,73,84,88,65]

x_coord = range(len(Tom))
plt.plot(x_coord, Tom, label='Tom', color = 'r')
plt.plot(x_coord, Peter, label='Peter', color = 'b')

plt.ylim(50,100)
plt.xlabel('Month')
plt.ylabel('score')

plt.legend()
plt.show()

