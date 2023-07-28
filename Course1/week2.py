# lagging strand (single-stranded life) -> higher mutation rate (C->T throuth deamination)
# forward half-strand -> shortage of C, normal G
# reverse half-strand -> shortage of G, normal C
import matplotlib.pyplot as plt 

class week2:
    def __init__(self):
        self.ans = ''
        return
    
    def Skew(self,dna:str) -> list:
        skew = ['0'] 
        GC = 0
        for i in range(len(dna)):
            if dna[i] == 'G':
                GC += 1
            if dna[i] == 'C':
                GC -= 1
            skew.append(str(GC))
        return skew
    
    def PromptSkew(self,file_directory:str) -> str:
        with open(file_directory,'r') as r:
            dna = r.readline().rstrip()
            ans = self.Skew(dna)
        
        self.ans = ' '.join(ans)
        return self.ans
    
    def MinimumSkew(self,dna:str):
        skew = self.Skew(dna)

            
prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
print(week2().PromptSkew(prompt_file))