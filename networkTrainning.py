import os, sys
import ROOT

netSize = 30
nodeDistance = 1.5

positions = []

row = []
#
#row.append([0.0, 1.0])
#row.append([0.1, 1.0])
#row.append([0.2, 1.0])
#row.append([0.3, 1.0])
#
#positions.append(row)
#
#row = []
#
#row.append([0.0, 2.0])
#row.append([0.1, 2.0])
#row.append([0.2, 2.0])
#row.append([0.3, 2.0])

#positions.append(row)

## We define the coordinates of node n,m for an hexagonal network
## n identifies the row (y-direction)

## n,m are the node coordinates
## D is the hexagon dimension. Number of neighbours
## netDimension the number of nodes
def get_list_of_nodes ( n, m, D, netDimension = 30 ):
    nodes = []

    ## Top-hexagon
    for j in range(D+1):
        Np = 2*D+1-j
        Y = m + j
        for i in range(Np):
            X = n - D + i
            node = [X%netDimension, Y%netDimension]
            if( X != n or Y != m ):
                nodes.append(node)

    ## Bottom-hexagon
    for j in range(1,D+1):
        Np = 2*D+1-j
        Y = m - j
        for i in range(Np):
            X = n - D + j + i
            node = [X%netDimension, Y%netDimension]
            if( X != n or Y != m ):
                nodes.append(node)

    return nodes

nodes = get_list_of_nodes( 9, 9, 2, 10 )

print (nodes)
