import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        archi=open(positives,'r')
        global pos 
        pos=""
        for line in archi.readlines():
            if ";" in line:
                pos=pos
            else:
                pos= pos+line
        
        archi.close()
        
        archi=open(negatives,'r')
        global neg
        neg=""
        for line in archi.readlines():
            if ";" in line:
                neg=neg
            else:
                neg= neg+line
        
        archi.close()
        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        #archi=open('positive-words.txt','r')
        #linea=archi.readline()
        #while linea!="":
            #print(linea, end="")
         #   if text in linea:
           #     return 1
          #  linea=archi.readline()
        #archi.close()

                

            
        
        nega=neg.split()
        posi=pos.split()
        if text in nega:
           return -1
        if text in posi:
           return 1
        #archi=open('negative-words.txt','r')                
        #linea=archi.readline()
        #while linea!="":
            #print(linea, end="")
         #   if text in linea:
          #      return -1
           # linea=archi.readline()
        #archi.close()

        # TODO
        return 0
