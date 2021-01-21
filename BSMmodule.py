# FILE BSMmodule.py
from numpy import *


# Black-Scholes-Merton monte-carlo calculator
class BSMMonteCarlo:

    def __init__(self, s_0=100.0, strike=105.0, t=1.0, r=0.05, sigma=0.2, number_of_simulations=100000):
        # Required parameters for the model
        self.s_0 = s_0
        self.strike = strike
        self.t = t
        self.r = r
        self.sigma = sigma
        self.number_of_simulations = number_of_simulations

    def calculate_call_price(self):
        # Normal law N(0,1) pseudorandom draws
        z = random.standard_normal(self.number_of_simulations)

        # European Black-Scholes-Merton model
        # Monte-carlo
        s_t = self.s_0 * exp((self.r - 0.5 * self.sigma ** 2) * self.t + self.sigma * sqrt(self.t) * z)
        h_t = maximum(s_t - self.strike, 0)
        c_0 = exp(-self.r * self.t) * sum(h_t) / self.number_of_simulations
        return c_0
