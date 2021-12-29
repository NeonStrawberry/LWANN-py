from neuron import *

class Network:
    n = [];
    tempN = [];
    
    start = [];
    end = [];
    
    done = [];
    
    def recursiveCompute(i):
        
    
    def computeNN(ac):
        for i in range(0, len(done)):
            done[i] = False;
            
        for i in range(0, len(start)):
            recursiveCompute(start[i]);
            
        n = tempN;
