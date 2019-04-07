import pytest
import random
import os
from percolation import *

def test_closed():
    random.seed(2)
    n = random.randint(1, 300)
    matrix = Percolation(n)
    for i in range(1,n+1):
        assert matrix.opened[i] == 0

def test_open():
    random.seed(2)
    n = random.randint(1, 300)
    matrix = Percolation(n)
    row = random.randint(1, n)
    col = random.randint(1, n)
    matrix.open(row,col)
    assert matrix.opened[(row-1)*n+(col)] == 1

def test_closed_not_percolates():
    random.seed(2)
    n = random.randint(1, 300)
    matrix = Percolation(n)
    assert matrix.percolates() == False
    
def test_open_percolates():
    random.seed(2)
    n = random.randint(1, 300)
    matrix = Percolation(n)
    for row in range(1, n+1):
        for col in range(1, n+1):
            matrix.open(row,col)
    assert matrix.percolates() == True

def test_files():
    for filename in os.listdir(os.getcwd()+'/tests'):
        file = open(os.getcwd()+'/tests/'+filename,"r")
        n =file.readline()
        n = n.strip()
        n = int(n)
        matrix = Percolation(n)
        percolates = file.readline()
        percolates = percolates.strip()
        data = [line.split() for line in file.readlines()]
        for i in data:
            if i != []:
                row = i[0]
                row = int(row)
                col = i[1]
                col = int(col)
                matrix.open(row,col)
        if percolates == "yes":
            assert matrix.percolates() == True
        else:
            assert matrix.percolates() == False
            

# Percolation threshold has been established to be in 0.593
# Adding sigma to account for randmoness
def test_percolation_mean():
    sigma = 0.01
    mean = PercolationStats.PercolationStats(200,10)
    mean_res = mean < (0.593 + sigma) and mean > (0.593 - sigma)
    assert mean_res == True
