import matplotlib.pyplot as plt

class week2:
    def __init__(self):
        self.ans = ''
        return
    
    def Skew(self, dna: str) -> list:
        skew = ['0'] 
        GC = 0
        for i in range(len(dna)):
            if dna[i] == 'G':
                GC += 1
            if dna[i] == 'C':
                GC -= 1
            skew.append(str(GC))
        return skew
    
    def PromptSkew(self, file_directory: str) -> str:
        with open(file_directory, 'r') as r:
            dna = r.readline().rstrip()
            ans = self.Skew(dna)
        
        self.ans = ' '.join(ans)
        return self.ans
    
    def MinimumSkew(self,dna:str) -> list:
        skew = [int(i) for i in self.Skew(dna)]
        minimum_value = min(skew)
        minimum_positions = [] 

        for b in range(len(dna)):
            if skew[b] == minimum_value:
                minimum_positions.append(str(b))

        return minimum_positions

    
    def PromptMinimumSkew(self, file_directory: str) -> str:
        with open(file_directory, 'r') as f:
            dna = f.readline().rstrip()
            ans = self.MinimumSkew(dna)
        
        self.ans = ' '.join(map(str, ans))
        with open('results.txt', 'w') as r:
            r.write(self.ans)
        return self.ans
    
    def HammingDistance(self,str1:str,str2:str) -> int:
        distance = 0 
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
        return distance
    
    def PromptHammingDistance(self,file_directory:str) -> str:
        with open(file_directory, 'r') as r:
            lines = r.readlines()
            str1 = lines[0].rstrip()
            str2 = lines[1].rstrip()
            ans = self.HammingDistance(str1,str2)
        self.ans = str(ans)
        return self.ans
    
    def PatternMatching(self,kmer:str,dna:str, d:int) -> list:
        pos = [] 
        for i in range(len(dna) - len(kmer) + 1):
            if self.HammingDistance(dna[i:i+len(kmer)], kmer) <= d:
                pos.append(i)
        
        return pos 
    
    def PromptPatternMatching(self,file_directory:str) -> str:
        with open(file_directory) as r:
            lines = r.readlines()
            kmer = lines[0].rstrip()
            dna = lines[1].rstrip()
            d = int(lines[2].rstrip())
            ans = self.PatternMatching(kmer,dna,d)
        self.ans = ' '.join(map(str,ans))
        return self.ans
    
    def Count_d(self,kmer:str,dna:str, d:int = 2):
        count = 0 
        for i in range(len(dna) - len(kmer) + 1):
            if self.HammingDistance(dna[i:i+len(kmer)], kmer) <= d:
                count += 1
        return count 
    
    def PromptCount_d(self,file_directory:str):
        with open(file_directory, 'r') as r:
            lines = r.readlines()
            kmer = lines[0].rstrip()
            dna = lines[1].rstrip()
            k = int(lines[2].rstrip())
            ans = self.Count_d(kmer,dna,k)
        self.ans = str(ans)
        return self.ans



prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
print(week2().PromptCount_d(prompt_file))

