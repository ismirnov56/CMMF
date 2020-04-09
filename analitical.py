# -*- coding: utf-8 -*-
import numpy as np


class Analitical:

    def __init__(self,  R=8, k=0.59, c=1.65, T=10):
        self.R = R
        self.k = k
        self.c = c
        self.T = T

    def getAnalitical(self, x):
        y = (1 + (3 * np.cos(x) * np.cos(x) - 1) * np.exp((-self.k * self.T * 6) / (self.c * (self.R * self.R)))) / 3
        return y