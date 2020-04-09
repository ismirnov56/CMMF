# -*- coding: utf-8 -*-
import numpy as np

class Implicit:


    q = np.pi/2

    def __init__(self, R=8, k=0.59, c=1.65, T=10, I=10, K=10):
        self.R = R
        self.k = k
        self.c = c
        self.T = T
        self.I = I
        self.K = K


    def createModel(self):
        self.qi = np.linspace(0, self.q, self.I + 1)
        self.u = np.cos(self.qi) * np.cos(self.qi)
        hq = self.q / self.I
        ht = self.T / self.K
        a = (self.k * ht)/(self.c * ((self.R * hq)*(self.R * hq)))
        Ai = np.zeros((self.I + 1, self.I + 1))
        Ai[0][0] = 1 + 4*a
        Ai[0][1] = -4 * a
        for i in range(1, self.I):
            b = (self.k * ht * np.cos(self.qi[i])) / (self.c * (self.R * self.R) * 2 * hq * np.sin(self.qi[i]))
            Ai[i][i-1] = b - a
            Ai[i][i] = 1 + 2*a
            Ai[i][i+1] = -b - a
        Ai[self.I][self.I-1] = -2 * a
        Ai[self.I][self.I] = 1 + 2 * a
        for k in range(0, self.K):
            u = np.linalg.solve(Ai, self.u)
            self.u = u


    def getModel(self):
        return self.u
