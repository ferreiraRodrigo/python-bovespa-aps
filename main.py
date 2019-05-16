import random
import numpy as np
from scipy.optimize import linprog
from bovespa_records import get_company_data

[companys_deviation, companys_name] = get_company_data('bovespa_march.txt')

# Set the companys data on arrays
def maximize_arrays():
    accepeted_risk = 1

    A = np.array([companys_deviation, np.ones(len(companys_deviation))])
    b = np.array([accepeted_risk, 1])

    random_array = []
    for i in range(0, len(companys_deviation)):
        random_array.append(random.randint(1, 5))
    c = np.array(random_array)

    # c * -1 to maximize instead of minimize
    return c * -1, A, b

def maximize(c, A, b):
    resp = linprog(c, A_ub, b_ub = b, bounds = (0, None))
    return resp

[c, A_ub, b_ub] = maximize_arrays()
results = maximize(c, A_ub, b_ub) 

for i in range(len(results.x)):
    if(results.x[i] > 0):
        print("{} : {:.6f}%".format(companys_name[i] ,results.x[i] * 100))