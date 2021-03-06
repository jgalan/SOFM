import os, sys, time
import ROOT
import numpy as np

import SOFM

Ro = SOFM.netSize/2.
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

def R( t ):
    return Ro + float(t)*(Rf-Ro)/Iterations

def h( dist, t ):
    return ROOT.TMath.Exp(-dist/R(t))

def alpha(t):
    return alpha_o + float(t)*(alpha_f-alpha_o)/Iterations

def update_neuron( n, m, dist, vector, t ):
    wNetwork[n][m] = wNetwork[n][m] + alpha(t) * h( dist, t) * ( vector - wNetwork[n][m] );

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

def update_region( vector, t ):

    wN = SOFM.get_winning_neuron( wNetwork, vector ) 

    lNodes = SOFM.get_list_of_nodes ( wN[0], wN[1], int( 2*R(t) ) )

    for node in lNodes:
        d = SOFM.node_distance( wN[0]-node[0], wN[1]-node[1] )
        update_neuron( node[0], node[1], d, vector, t )

    return 0

##### Advice: For each method you write-down write few lines for testing input 
##### and output results
## We test the update of neuron (n,m) using first element in the dataset
## print ( "Testing update neuron " )
## print ( "Input vector : " )
## print ( dataset[0][1:8] )
## print ( "Neuron before : ")
## print ( wNetwork[6][8] )
## print ( update_neuron( 6, 8, 1.5, dataset[0][1:8], 5 ) )
## print ( "Neuron after : ")
## print ( wNetwork[6][8] )


def networkTraining( ):

    for iteration in range(Iterations):
        counter = 0
        print ("Iteration " + str( iteration ) + "\n" )
        for v in dataset:
            counter = counter + 1
            update_region( v[1:8], iteration )
            if counter % 1000 == 0:
                print ("counter: " + str(counter) )
            if counter > maxSamples:        
                print( "Reseting at sample : " + str(counter) )
                break 

    f = open("results/network.out", "wt" )
    for n in range(SOFM.netSize):
        for m in range(SOFM.netSize):
            f.write(str(n)+"\t"+str(m) )
            for l in range(len(wNetwork[n][m]) ):
                f.write( "\t" + str(wNetwork[n][m][l]) )
            f.write("\n")
    f.close()
###

networkTraining()
