import pickle

def save(network,filename):
    save = open(filename,'wb')
    pickle.dump(network,save)

def load(filename):
    file = open(filename,'rb')
    net = pickle.load(file)
    return net
