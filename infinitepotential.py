import numpy as np
import matplotlib.pyplot as plt

n = 5
potential_values = np.zeros(n)
delta_x = 1
#matrix = np.zeros((n,n))

#print(matrix)

def hamiltonian(n,delta_x,potential_values):
    hamiltonian = np.zeros((n,n))
    
    
    off_diagonal = -1/2*(delta_x**2)
    
    for i in range(n):
        diagonal_elements = 1/(delta_x**2) + potential_values[i]
        hamiltonian[i,i] = diagonal_elements
        
    for j in range(n-1):
        hamiltonian[j+1,j] = off_diagonal
        hamiltonian[j,j+1] = off_diagonal
        
    return hamiltonian
    
Hamiltonian = hamiltonian(n,delta_x,potential_values)

eigenvalues,eigenvectors = np.linalg.eigh(Hamiltonian)

 