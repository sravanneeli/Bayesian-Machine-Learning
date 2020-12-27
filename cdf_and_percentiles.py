import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
np.random.seed(0)

mu = 170
sd = 7

x = norm.rvs(loc=mu, scale=sd, size=100) # generate samples for distribution

print(x.mean()) # maximum likelihood mean

print(x.var()) # maximum likelihood variance

print(((x - x.mean())**2).mean())

print(x.std())

print(x.var(ddof=1))

print(((x - x.mean())**2).sum() / len(x) - 1)

print(x.std(ddof=1))

# at what height are you in the 95th percentile
print(norm.ppf(0.95, loc=mu, scale=sd))

# you are 160 cm tall what percentile are you in 
print(norm.cdf(160, loc=mu, scale=sd))

# you are 180 cm tall, what is the probability that someone is taller than you?
print(1 - norm.cdf(180, loc=mu, scale=sd))

print(norm.sf(180, loc=mu, scale=sd))