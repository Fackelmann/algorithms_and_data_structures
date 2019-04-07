# Quick Union-Find

Weighted Union-Find implementation with path compression implemented in Python following [Algorithms, Part 1. Princeton University. Coursera](https://www.coursera.org/learn/algorithms-part1/)

## Problem description
- Given a set of N objects:
  - Union command: connect two objects
  - Find/connected query: is there a path connectin the two objects?


## Implementation
The data structure chosen for this algorithm is an integer array of size N, id. For a node i, j=id[i] represents the node j that is the parent of i.

## Time complexity
In order to improve the time complexity, 2 optimizations are implemented.

### Weighting
We want to avoid tall trees, so the worst-case for finding the root is less than O(n). We can achieve a balanced tree by linking the root of the smaller tree to the root of the larger tree when performin a Union.

This way we can achieve a maximum height of the tree of lg N, which means that the union and connected methods are O(lg N) (since we have to find the roots for the two nodes)

## Path compression
We can further decrease the height of the tree by pointing the parent of each node to point to the root. Intuitively, it makes sense that this will reduce the time complexity, since we'll have to go through less nodes to reach the root in future operations.

Mathematically this is an iterate log function (not proved here), which has almost constant time complexity.


# Percolation

We apply the quick Union Find algorithm to the percolation problem. This problem can be stated as follows:

- We have a N-by-N grid of sites
- Each site is open with probability p
- System percolates iff top and bottom are connected by open sites

A test bench for the the implementation of this percolation solver is provided. To launch the test simply run:

% pytest

You will need to have _pytest_ installed. If you don't, you can install it via:

% pip install pytest