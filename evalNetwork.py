import ROOT

from ROOT import (
    TChain, TFile, TTree, TCanvas, TPad,
    TH1D, TH2D, TH3D,
    TProfile, TProfile2D, TProfile3D,
    TGraph, TGraph2D,
    TF1, TF2, TF3, TFormula,
    TLorentzVector)

import numpy as np

import SOFM

netSize = SOFM.netSize

dataNetwork = np.loadtxt("results/network.out")
nSizeX = len(dataNetwork[0])
nSizeY = len(dataNetwork)
# print ( nSizeX )
# print ( nSizeY )
# print ( len( dataNetwork[0][2:]) )
wNetwork = []

for n in range(SOFM.netSize):

    netRow = []
    for m in range(SOFM.netSize):
        print ( "n: " + str(n) + " m: " + str(m) + "\n" )
        print ( dataNetwork[n*netSize+m] )
        if ( n != int(dataNetwork[n*netSize+m][0]) or m != dataNetwork[n*netSize+m][1] ):
            print ( "N: " + str(int(dataNetwork[n*netSize+m][0])) + " M: " + str(int(dataNetwork[n*netSize+m][1])) )
            print ( "Error reading dataset. Node coordinates do not correspond!" )
        netRow.append( dataNetwork[n*netSize+m][2:] )
    wNetwork.append( netRow )

populationA = np.loadtxt("data/populationA.txt")
populationB = np.loadtxt("data/populationB.txt")
populationC = np.loadtxt("data/populationC.txt")
populationD = np.loadtxt("data/populationD.txt")
populationE = np.loadtxt("data/populationE.txt")
populationF = np.loadtxt("data/populationF.txt")
populationG = np.loadtxt("data/populationG.txt")

#for data in populationA:
#    print( SOFM.get_winning_neuron( wNetwork, data ) )

c1 = TCanvas( 'c1', 'My canvas', 1600,1000 )
#c1.SetFillColor( 42 )
#c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 6 )
c1.GetFrame().SetBorderMode( -1 )

pad1 = TPad("pad1","This is pad1",0.05,0.02,0.95,0.97);
pad1.Divide(3,2)
pad1.Draw()

hist_A = TH2D("popA", "Population A", netSize, 0, netSize, netSize, 0, netSize )
for data in populationA:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_A.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(1)
hist_A.SetStats(0)
hist_A.Draw("box")

hist_B = TH2D("popB", "Population B", netSize, 0, netSize, netSize, 0, netSize )
for data in populationB:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_B.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(2)
hist_B.SetStats(0)
hist_B.Draw("box")

hist_C = TH2D("popC", "Population C", netSize, 0, netSize, netSize, 0, netSize )
for data in populationC:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_C.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(3)
hist_C.SetStats(0)
hist_C.Draw("box")

hist_D = TH2D("popD", "Population D", netSize, 0, netSize, netSize, 0, netSize )
for data in populationD:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_D.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(4)
hist_D.SetStats(0)
hist_D.Draw("box")

hist_E = TH2D("popE", "Population E", netSize, 0, netSize, netSize, 0, netSize )
for data in populationE:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_E.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(5)
hist_E.SetStats(0)
hist_E.Draw("box")

hist_F = TH2D("popF", "Population F", netSize, 0, netSize, netSize, 0, netSize )
for data in populationF:
    winNeuron = SOFM.get_winning_neuron( wNetwork, data ) 
    hist_F.Fill( winNeuron[0], winNeuron[1] )

pad1.cd(6)
hist_F.SetStats(0)
hist_F.Draw("box")

c1.Update()

#print (wNetwork )
#print( populationB )
#print( nSizeX )
#print( nSizeY )

input("Press enter to continue…")
