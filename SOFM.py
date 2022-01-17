import numpy as np

netSize = 20

## This method returns all the nodes around a given
## node (n,m) that are found within a distance D.
##
## n,m are the node indexes.
## D is the hexagon size. Or number of neighbours.
## netSize the number of nodes per dimension.
##
## We define the network periodicity using module %netSize
##
def get_list_of_nodes ( n, m, D ):
    nodes = []

    ## Top-hexagon
    for j in range(D+1):
        Np = 2*D+1-j
        Y = m + j
        for i in range(Np):
            X = n - D + i
            node = [X%netSize, Y%netSize]
            nodes.append(node)

    ## Bottom-hexagon
    for j in range(1,D+1):
        Np = 2*D+1-j
        Y = m - j
        for i in range(Np):
            X = n - D + j + i
            node = [X%netSize, Y%netSize]
            nodes.append(node)

    return nodes


## It returns the coordinates of node with vector closest to the one given
def get_winning_neuron( network, vect ):
    v = np.array(vect)
    diff = np.sqrt(np.sum((network[0][0] - v) ** 2))

    neuron = [0,0]
    for n in range(netSize):
        for m in range(netSize):
            if( np.sqrt(np.sum((network[n][m] - v) ** 2)) < diff ):
                diff = np.sqrt(np.sum((network[n][m] - v) ** 2) )
                neuron = [n,m]
    return neuron

## It returns the coordinates of node (n,m)
def node_coordinates( n, m ):
    return np.array([n+0.5*m, m ])

## It returns the distance respect to the node (0,0)
def node_distance( delta_n, delta_m ):
    return np.sqrt( np.sum(node_coordinates(delta_n, delta_m)**2) )
