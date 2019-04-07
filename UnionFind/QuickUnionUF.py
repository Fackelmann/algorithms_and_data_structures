class QuickUnionUF:
    """
    A class used to represent a Union-Find data structure

    ...

    Attributes
    ----------
    N : int
    Number of elements in the structure

    Methods
    -------
    root(i: int)
    Returns the root of element i

    connected(p: int, q: int)
    Returns True if elements p and q are connected, False if not.

    union (p: int, q: int)
    Merges elements p and q
    """
    
    def __init__(self, N: int):
        """
        Parameters
        ----------
        N : int
        Number of elements in the structure
        """
        self.N = N
        self.id = []
        self.id = list(range(N))
        self.__sz = [1] * N

    def root(self, i: int) -> int:
        """
        Returns the root of element i

        Args
        ----
        i : int
        Element whose root we want to find
            

        Returns
        -------
        Root element (int) of element i
        """
        
        while i != self.id[i]:
            # One pass variant path compression
            # Make every other node in path point to it's granparent
            # Halves path length
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    
    def connected(self, p: int, q: int) -> bool:
        """
        Checks if elements p and q are connected

        Args
        ----
        p : int, q : int
        Elements of the structure
            

        Returns
        -------
        True if p and q are connected, False otherwise
        """        
        return self.root(p) == self.root(q)


    def union(self, p: int, q: int):
        """
        Merges elements p and q

        Args
        ----
        p : int, q : int
        Elements of the structure
            

        Returns
        -------
        Nothing
        """                
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return
        if self.__sz[i] < self.__sz[j]:
            self.id[i] = j
            self.__sz[j] += self.__sz[i]
        else:
            self.id[j] = i
            self.__sz[i] += self.__sz[j]



    

if __name__ == "__main__":            

    quick=QuickUnionUF(5)
    print(quick.id)
    print("Union 0 and 1")
    quick.union(1,0)
    print(quick.id)
    print("Union 2 and 1")
    quick.union(1,2)
    print(quick.id)
    print("Union 3 and 1")
    quick.union(1,3)
    print(quick.id)
    print("Union 0 and 4")
    quick.union(4,0)
    print(quick.id)
