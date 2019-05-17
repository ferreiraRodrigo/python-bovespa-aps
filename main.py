import random
import numpy as np
from scipy.optimize import linprog
from bovespa_records import get_company_data

# Set the companys data on arrays
[companys_deviation, companys_profit ,companys_name] = get_company_data('bovespa_march.txt')

def maximize_arrays():
    risk_accepted = 10

    A_ub = np.array([companys_deviation, np.ones(len(companys_deviation))])
    b_ub = np.array([risk_accepted, 1])
    c = np.array(companys_profit)

    # c * -1 to maximize instead of minimize
    return c * -1, A_ub, b_ub

def maximize(c, A_ub, b_ub):
    res = linprog(c, A_ub, b_ub = b_ub, bounds = (0, None))
    return res

[c, A_ub, b_ub] = maximize_arrays()
results = maximize(c, A_ub, b_ub) 

print("Investiments: \n")
for i in range(len(results.x)):
    if(results.x[i] > 0):
        print("{} : {:.5f}%".format(companys_name[i] ,results.x[i] * 100))
        print("Risk: {:.5f}%".format(companys_deviation[i]))
        print("Average profit: {:.5f}%\n".format(companys_profit[i]))