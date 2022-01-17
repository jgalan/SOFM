import os, sys, time
import ROOT

from secrets import randbelow


N = 5000
nVars = 7

populations = [[21.5, 35.1, 3.8, 87.3, 19, 24.2, -7.8 ]
              ,[11.5, -15.1, 3.4, 86.7, 12, 25.2, -8.8 ]
              ,[-1.5, 25.1, 4.4, 85.9, 12, 25.6, -10.8 ]
              ,[31.5, -5.1, 2.4, 87.2, 21, 23.2, 2.8 ]
              ,[6.5, -5.1, 1.4, 87.8, 18, 13.8, 3.8 ]
              ,[21.5, 25.1, 2.4, 86.6, 14, 13.2, 1.8 ]
              ,[21.5, 87.1, 1.4, 87.7, 15, 13.6, 0.8 ]]

nPopulations = len(populations)
nVars = len(populations[0])

sigmas = [2.1, 5.5, 0.4, 3.2, 1.1, 0.5, 3.3 ]

rootRnd = ROOT.TRandom3()
rootRnd.SetSeed( int (time.time()) ) 

f = open("data/populationA.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[0][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationB.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[1][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationC.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[2][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationD.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[3][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationE.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[4][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationF.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[5][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/populationG.txt", "w")
for n in range(N):
    for m in range(nVars):
        value = rootRnd.Gaus( populations[6][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/trainSet.txt", "w")
for n in range(5*N):
    var = randbelow(nVars)
    f.write( str(var) + "\t" )
    for m in range(nVars):
        value = rootRnd.Gaus( populations[var][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

f = open("data/testSet.txt", "w")
for n in range(5*N):
    var = randbelow(nVars)
    f.write( str(var) + "\t" )
    for m in range(nVars):
        value = rootRnd.Gaus( populations[var][m], sigmas[m] )
        f.write( str(value) + "\t" )
    f.write( "\n" )
f.close()

print( "Populations have been re-generated inside the 'data' directory" )
