# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:00:18 2019

@author: sergio.amonteiro
"""
#------------------------------------------------------------------------------
#minimize 70x_1 + 80x_2 +85x_3
#{ s.a.} x_1 + 4x_2 + 8x_3   >= 4500
#      40x_1 + 30x_2 + 20x_3 <= 36000
#       3x_1 + 2x_2 + 4x_3   >= 2700
#        x >= 0 
#------------------------------------------------------------------------------
import bovespa
import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve
#------------------------------------------------------------------------------
def resolverPLDesigualdade(c, A_ub, b_ub):
    res = linprog(c, A_ub=A_ub, b_ub=b_ub,
                  bounds=(0, None))
    return res
#------------------------------------------------------------------------------    
def exemplo01():
    A_ub = np.array([[-1, -4, -8],
                     [40,30,20],
                     [-3,-2,-4]])
    b_ub = np.array([-4500, 36000,-2700])
    c = np.array([70, 80, 85])
    return c, A_ub, b_ub

def exemplo02():
    A_ub = np.array([[1, 0],
                     [1, 1],
                     [0, 1],
                     [1, 0],
                     [2, 3]])
    b_ub = np.array([10, 10, 40, 60, 180])
    c = -1 * np.array([1, 1])
    return c, A_ub, b_ub

def exemplo03():
    A_ub = np.array([[1, 0, 2, 2, 1, 2],
                     [0, 1, 3, 1, 3, 2]])
    b_ub = np.array([9, 19])
    c = -1 * np.array([35, 30, 60, 50, 27, 22])
    return c, A_ub, b_ub
#------------------------------------------------------------------------------    
#Programa Principal    
#------------------------------------------------------------------------------    
[c, A_ub, b_ub]=exemplo03()#carregar exemplo 01
#------------------------------------------------------------------------------    
resultado=resolverPLDesigualdade(c, A_ub, b_ub) #resolver PL
#------------------------------------------------------------------------------    
#Read bovespa file
#------------------------------------------------------------------------------
bovespa_file = bovespa.File('bovespa_march.txt')
for bovespa_record in bovespa_file.query():
    print("{} | {} | Open Price: {} | Close Price: {} | Profit: {:.2f}".format(bovespa_record.date, bovespa_record.stock_code, bovespa_record.price_open, bovespa_record.price_close, (bovespa_record.price_close - bovespa_record.price_open)))
#------------------------------------------------------------------------------  
print('Valor otimo:', resultado.fun)
#------------------------------------------------------------------------------    
print("Os valores de x sao:")
nelem=len(resultado.x)
for i in range(nelem):
    print("x[",i+1,"]=",resultado.x[i])
#------------------------------------------------------------------------------        
