#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:50:32 2019

@author: mohitbeniwal
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

Y = mpimg.imread('Bayesnoise_grayscale.png')
imgplot = plt.imshow(Y)
Y[Y == 0] = -1
beta = 2
eta = .1
h = 0.1
print('Beta: '+str(beta)+', eta: '+str(eta)+', h: '+str(h) )
X = Y
rows, cols = X.shape
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= rows-1 and
                                   -1 < y <= cols-1 and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= rows-1) and
                                   (0 <= y2 <= cols-1) and not (abs(x2-x)>0 and abs(y2 -y)) )]
def summation(xi, neighbours):
    summation_xi_xj = 0 
    for neig in neighbours:
        summation_xi_xj += xi * X[neig[0]][neig[1]]
    return summation_xi_xj 
                               
def energy(xi, neighbours):
    summation_xi_xj = beta * summation(xi, neighbours)
    eta_xi_yi = eta * xi * Y[row][col]
    h_Xi = h * xi 
    return h_Xi - summation_xi_xj  - eta_xi_yi

def error(X,Y1):
    mis_match = 0       
    for row in range(rows):
        for col in range(cols):
            if(X[row][col] != Y1[row][col]):
                mis_match +=1  
    return mis_match/(311*420)

#clean image
Y1 = mpimg.imread('Bayes_grayscale.png')
Y1[Y1 == 0] = -1    
    
status = True 
print('Similarity in given noise image with origional image: '+str((1 - error(Y, Y1))*100)+' %')
iteration = 0       
while(status):
    count = 0
    for row in range(rows):
        for col in range(cols):
            xi = X[row][col]
            neighbours = neighbors(row, col)
            energy_ = energy(xi, neighbours)
            xi_flip = xi * -1
            energy_flip = energy(xi_flip, neighbours)
            if(energy_flip < energy_):
                X[row][col]  = xi_flip
                count += 1
    if(count == 0):
        status = False
    iteration += 1    
    print("No. of pixel fliped in iteration "+str(iteration)+' is '+str(count))
    print('Similarity now with origional image: '+str((1 - error(X, Y1))*100)+' %')
imgplot = plt.imshow(X)
plt.savefig('cleaned.png')

        



        

