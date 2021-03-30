import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def sample_standard_norm():
    return stats.norm(0,1).rvs(1)[0]

def standard_brownian_motion(n:int):
    X_is=[sample_standard_norm() for _ in range(1,n)]
    S_ns=[0]+list(np.cumsum(X_is))
    W_ts=[x/np.sqrt(n) for x in S_ns]
    return W_ts

def drift_brownian_motion(n:int,mu:float):
    W_ts=standard_brownian_motion(n)
    W_ts_drift=[W_ts[t]+mu*t for t in range(n)]
    return W_ts_drift

n=1000
for i in range(2):
    plt.plot([x/n for x in range(n)],standard_brownian_motion(n))
plt.show()

plt.plot([x/n for x in range(n)],drift_brownian_motion(n,-3))
plt.plot([x/n for x in range(n)],drift_brownian_motion(n,30))
plt.show()
