class Neuron:
    threshold = 0;
    weights = [];
    
    in_cCount = 0;
    out_cCount = 0;
    
    index = [];
    ptr = [];
    
    activations = [];
    activation = [];

    
def compute(Neuron n):
    a = 0;
    
    for i in range(0, n.in_cCount):
        a += n.activations[i];
        
    if a >= n.threshold:
        return n.weights;
    
    else:
        return [];
