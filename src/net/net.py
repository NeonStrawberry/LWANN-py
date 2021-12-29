from neuron import *

class Network:
    n = [];
    tempN = [];
    
    start = [];
    end = [];
    
    done = [];
    
    def recursiveCompute(x):
        in = 0; #The indicies for the activations used in the current neuron
        
        for i in range(0, n[x].in_cCount):
            for j in range(0, len(n[n[x].index[i]].ptr)):
                if n[n[x].index[i]].ptr[j] == x:
                    in = j;
                    
        for i in range(0, n[x].in_cCount):
            tempN[x].activations[i] = n[n[x].index[i]].activation[in[]]; #Setting up the proper activatons
            
        tempN[x].activation = compute(tempN[x]);
    
    def computeNN(ac):
        ret = [];
        
        for i in range(0, len(done)):
            done[i] = False;
            
        for i in range(0, len(start)):
            recursiveCompute(start[i]);
            
        n = tempN;
