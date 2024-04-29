import argparse
class Transfer() :
    """ Transfer little of knowledge 
        Neural Network Surgery (NNS)
        Transfer sub network """
    
    def __init__(self) -> None :
        pass
    
    def checkFile(self) -> bool :
        """ check exists model file """
        pass
    
    def run(self) -> None :
        """ run sequence of commands """
        pass
    
if __name__ == "__main__" :
    """ CLI mode run """
    print("\n[Transfer CLI mode]\n")
    parser = argparse.ArgumentParser(description = "Transfer little of knowledge \
        Neural Network Surgery (NNS) \
        Transfer sub network")
    parser.add_argument('input', metavar = "inputFile", help = "input file (only model file [*.h5])")
    parser.add_argument('-o', '--output', metavar = "fileName", default = 'outputTransfer',   
                        help = "output file name after Surgery")
    args = parser.parse_args()
    print(args)