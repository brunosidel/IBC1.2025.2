import numpy as np


n_personas = 100
n_jugadas = 1000
prob_cara = 0.5
capitales = np.full(n_personas, 100.0)


for _ in range(n_jugadas):
    tiradas = np.random.rand(n_personas) < prob_cara

    capitales[tiradas] *= 1.5
    capitales[~tiradas] *= 0.6

    total_fondo = np.sum(capitales)

    capitales[:] = total_fondo / n_personas


print(
    f"Capital final por persona después de {n_jugadas} jugadas: {capitales[0]:.8f}")
