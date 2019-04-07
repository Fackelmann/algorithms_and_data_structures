import random
import math
from QuickUnionUF import *

class Percolation:
    """
    A class used to represent an instance of the percolation problem

    ...

    Attributes
    ----------
    n : int
    Size of the matrix (nxn)

    opened : list
    List containing list[i] = 0 if node i is closed, 1 if open

    connection : QuickUnionUF
    QuickUnionUF object containing information of which nodes are connected

    open : int
    Number of open sites

    Methods
    -------
    open(row: int, col: int)
    Open node in row,col

    percolates()
    Returns True if problem percolates, False if not

    print()
    Prints ASCII representation of the problem, using '.' for closed sites, and ' ' for open sites
    """    
    def __init__(self, n: int):
        """
        Parameters
        ----------
        n : int
        Size of the matrix (nxn)
        """        
        self.n=n
        self.opened = [0]*(n*n+2)
        self.connection = QuickUnionUF(n*n+2)
        self.opened[0]=1
        self.opened[n*n+1]=1
        self.open_sites=0
        for i in range(0,n):
            self.connection.union(0,i+1)
        for i in range(n*n-n,n*n):
            self.connection.union(n*n+1,i+1)

    def open(self, row: int, col: int):
        """
        Opens node in row=row, col=col

        Args
        ----
        row, col : int
        Row and column to be opened
            

        Returns
        -------
        Nothing
        """        
        site = (row-1)*self.n+(col)
        lsite = (row-1)*self.n+(col-1)
        rsite = (row-1)*self.n+col+1
        tsite = (row-2)*self.n+(col)
        if row != self.n :
            bsite = (row)*self.n+(col)
        else:
            bsite = self.n
        if self.opened[site] != 1:    
            self.opened[site]=1
            self.open_sites+=1
            if self.opened[lsite] == 1 and col != 1:
                self.connection.union(site,lsite)
            if self.opened[rsite] == 1 and col != self.n:
                self.connection.union(site,rsite)
            if self.opened[tsite] == 1 and row != 1:
                self.connection.union(site,tsite)
            if self.opened[bsite] == 1 and row != self.n:
                self.connection.union(site,bsite)            

    def percolates(self):
        """
        Check if problem percolates

        Args
        ----

        Returns
        -------
        True if percolates, False if not
        """            
        return self.connection.connected(0,self.n*self.n+1)
        
    def print(self):
        """
        Prints ASCII representation of the problem, using '.' for closed sites, and ' ' for open sites

        Args
        ----

        Returns
        -------
        Nothing
        """
        for i in range(1, self.n*self.n+1):
            if (i-1)%self.n ==0:
                print("|",end='')
            if self.opened[i] == 0:
                print('.',end='')
            elif self.opened[i] == 1:
                print(' ',end='')
            else:
                print(';',end='')
            if i%self.n == 0:
                print("|\n", end='')
        print("")

class PercolationStats:

    @classmethod
    def PercolationStats(cls, n: int, trials: int):
        prob = 0.01
        incr = 0.01
        trialthres=0
        trial = [""] * trials
        for i in range(0, trials):
            print ("Trial: ",i)
            per=Percolation(n)            
            prob = 0.01
            while per.percolates() != True:
                per=Percolation(n)
                for row in range(1, n+1):
                    for col in range(1, n+1):
                        if random.random() < prob:
                            per.open(row,col)
                prob=prob+incr
            trial[i] = per.open_sites/(n*n)
            trialthres = trialthres + trial[i]

        mean=trialthres/trials
        
        stdv=0
        for i in trial:
            stdv=(i-mean)**2 + stdv
        stdv=stdv/(trials-1)

        confidenceLo = mean -(1.96*math.sqrt(stdv))/math.sqrt(trials)
        confidenceHi = mean +(1.96*math.sqrt(stdv))/math.sqrt(trials)        
        print("Mean: ",mean)
        print("Standard deviation: ",stdv)
        print("95% confidence interval:  [",confidenceLo,',',confidenceHi,']')                
        return mean
        
                
        
if __name__ == "__main__":                            
    PercolationStats.PercolationStats(200,100)
