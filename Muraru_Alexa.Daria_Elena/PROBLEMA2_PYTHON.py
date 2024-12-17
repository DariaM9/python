import matplotlib.pyplot as plt
import pandas as pd 

date = pd.read_csv("./data.csv")

durate = date["Durata"]
pulsuri = date["Puls"]
maxPulsuri = date["MaxPuls"]
calorii = date["Calorii"]

# Toate valorile
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(durate, label="Durata")
axes[0, 0].legend()
axes[0, 1].plot(pulsuri, label="Puls")
axes[0, 1].legend()
axes[1, 0].plot(maxPulsuri, label="MaxPuls")
axes[1, 0].legend()
axes[1, 1].plot(calorii, label="Calorii")
axes[1, 1].legend()

plt.show()

# Primele X valori
X = 11

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(durate[:X], label="Durata")
axes[0, 0].legend()
axes[0, 1].plot(pulsuri[:X], label="Puls")
axes[0, 1].legend()
axes[1, 0].plot(maxPulsuri[:X], label="MaxPuls")
axes[1, 0].legend()
axes[1, 1].plot(calorii[:X], label="Calorii")
axes[1, 1].legend()
plt.show()


# Ultimele Y valori
Y = 10

fig, axes = plt.subplots(1, 2)

axes[0].plot(durate[-Y:], label="Durata")
axes[0].legend()
axes[1].plot(pulsuri[-Y:], label="Puls")
axes[1].legend()
plt.show()