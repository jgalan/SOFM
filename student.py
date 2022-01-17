import os, sys, time
import ROOT
import numpy as np

import SOFM

Ro = SOFM.netSize/4.
Rf = 1

alpha_o = 0.99
alpha_f = 0.01

Iterations = 10

maxSamples = 500

### reading dataset and initializing network
dataset = np.loadtxt("data/trainSet.txt")
nVars = len(dataset[0]) - 1
nData = len(dataset)

print ("vars: " + str( nVars ) )
print ("data: " + str( nData ) )

## We initialize the network with mean and sigmas from dataset
means = []
for n in range(1,nVars+1):
    means.append(np.mean(dataset[:,n]))
means = np.array(means)

sigmas = []
for n in range(1,nVars+1):
    sigmas.append(np.std(dataset[:,n]))
sigmas = np.array(sigmas)

def initialize_network( ):
    nVars = len(means)

    rootRnd = ROOT.TRandom3()
    rootRnd.SetSeed( int (time.time()) ) 

    network = []
    for i in range(SOFM.netSize): 
        netRow = []
        for j in range( SOFM.netSize):
            vector = []
            for n in range(nVars):
                value = rootRnd.Gaus( means[n], sigmas[n] )
                vector.append( value )
            netRow.append( np.array(vector) )
        network.append(netRow)
    return network

wNetwork = initialize_network(  )

## Winning neuron of first element in the dataset
## print ( "Testing winning neuron identification" )
## print ( SOFM.get_winning_neuron( wNetwork, dataset[0][1:8] ) )

######################################################
### Above code (together with SOFM.py) is given to the student
###
### See student.py
###
### The output file must contain the  weights vector of each network cell.
### Proposed format:
###
### 0 0 w1 .... wN
### 0 1 w1 .... wN
### ...
### 29 29 w1 .... wN
###
### The coming code is work for the student.
### So this is a possible solution to the exercise. 
### This must be removed from the lecture.
###

### Proposed function scheme
def R( t ):
    return Ro + float(t)*(Rf-Ro)/Iterations

def h( dist, t ):
    return ROOT.TMath.Exp(-dist/R(t))

def alpha(t):
    return alpha_o + float(t)*(alpha_f-alpha_o)/Iterations

def update_neuron( n, m, dist, vector, t ):

    ## Update neuron (n,m) using the distance to the winning neuron, iteration number "t" and input vector.

    ## TOBE implemented

    return 0

def update_region( vector, t ):

    ## Update winning neuron and its neighbours using the neighbourhood functions as a function of
    ## the iteration number "t"

    ## TOBE implemented

    return 0

########
## Advice: For each method you write-down write few lines for testing input 
##    and output results
##
## For example. We test the update of neuron (n,m) using first element in the dataset.
## print ( "Testing update neuron " )
## print ( "Input vector : " )
## print ( dataset[0][1:8] )
## print ( "Neuron before : ")
## print ( wNetwork[6][8] )
## print ( update_neuron( 6, 8, 1.5, dataset[0][1:8], 5 ) )
## print ( "Neuron after : ")
## print ( wNetwork[6][8] )


def networkTraining( ):

    ### Iterate over the dataset vectors, get the corresponding winning neuron
    ### and update the weights in an iterative process. Use maxSamples to define
    ### a maximum number of samples to be presented to the network, and test your
    ### code with a reduced version
    for iteration in range(Iterations):
        for v in dataset:

            ## TOBE implemented. Use maxSamples to reduce the computational cost
            ## and reduce the time invested in testing your code

            update_region( v[1:8], iteration )


    f = open("data/network.out", "wt" )
    for n in range(SOFM.netSize):
        for m in range(SOFM.netSize):
            f.write(str(n)+"\t"+str(m) )
            for l in range(len(wNetwork[n][m]) ):
                f.write( "\t" + str(wNetwork[n][m][l]) )
            f.write("\n")
    f.close()
###

networkTraining()
