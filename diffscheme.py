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

#v1
class Explicit:

    q = np.pi / 2

    def __init__(self, R=8, k=0.59, c=1.65, T=10, I=10, K=10):
        self.R = R
        self.k = k
        self.c = c
        self.T = T
        self.I = I
        self.K = K

    def createModel(self):
        self.v = np.empty((0, self.I + 1), dtype=float)
        qi = np.linspace(0, self.q, self.I + 1)

        hq = self.q / self.I
        ht = self.T / self.K

        self.v = np.vstack([self.v, np.cos(qi) ** 2])
        alpha = (self.k * ht) / (self.R ** 2 * self.c)
        for k in range(0, self.K):
            self.v = np.vstack([self.v, np.zeros(self.I + 1)])
            self.v[k + 1][0] = 4 * alpha * (self.v[k][1] - self.v[k][0]) / (hq ** 2) + self.v[k][0]
            for i in range(1, self.I):
                self.v[k + 1][i] = alpha * (
                            np.cos(qi[i]) * (self.v[k][i + 1] - self.v[k][i - 1]) / (np.sin(qi[i]) * 2 * hq) + (
                                self.v[k][i + 1] - 2 * self.v[k][i] + self.v[k][i - 1]) / (hq ** 2)) + self.v[k][i]
            self.v[k + 1][self.I] = 2 * alpha * (self.v[k][self.I - 1] - self.v[k][self.I]) / (hq ** 2) + self.v[k][
                self.I]

    def getModel(self):
        return self.v[self.K]

#v2
class Expl:

    q = np.pi / 2

    def __init__(self, R=8, k=0.59, c=1.65, T=10, I=10, K=10):
        self.R = R
        self.k = k
        self.c = c
        self.T = T
        self.I = I
        self.K = K

    def createModel(self):
        self.vk1 = np.empty(self.I + 1, dtype=float)
        qi = np.linspace(0, self.q, self.I + 1)

        hq = self.q / self.I
        ht = self.T / self.K

        self.vk = np.cos(qi) ** 2
        alpha = (self.k * ht) / (self.R ** 2 * self.c)
        for k in range(0, self.K):
            self.vk1[0] = 4 * alpha * (self.vk[1] - self.vk[0]) / (hq ** 2) + self.vk[0]
            for i in range(1, self.I):
                self.vk1[i] = alpha * (np.cos(qi[i]) * (self.vk[i + 1] - self.vk[i - 1]) / (np.sin(qi[i]) * 2 * hq) + (self.vk[i + 1] - 2 * self.vk[i] + self.vk[i - 1]) / (hq ** 2)) + self.vk[i]
            self.vk1[self.I] = self.vk1[self.I-1]
            self.vk = self.vk1

    def getModel(self):
        return self.vk1