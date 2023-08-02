from itertools import product

class week3:
    def __init__(self):
        self.ans = ''
        return

    def HammingDistance(self,str1:str,str2:str) -> int:
        distance = 0 
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
        return distance 
    
    def GenerateKmers(self,dna:list, k:int):
        kmers = [] 
        for subsequence in dna:
            for i in range(len(subsequence) - k + 1):
                if subsequence[i:i+k] not in kmers:
                    kmers.append(subsequence[i:i+k])

        return kmers

    def SlidingWindow(self,string:str,k:int):
        for i in range(len(string) - k + 1):
            yield string[i:i+k]


    def MotifEnumeration(self, dna: list, k: int, d: int) -> list:
        motifs = []
        nucleotides = ['A' , 'T' , 'C', 'G']
        kmers = [''.join(c) for c in product(nucleotides,repeat=k)]

        for kmer in kmers:
            if all(any(self.HammingDistance(kmer,pat) <= d for pat in self.SlidingWindow(string,k)) for string in dna):
                motifs.append(kmer)

        return motifs
    
    def PromptMotifEnumeration(self,file_directory:str) -> str:
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            k,d = [int(i) for i in lines[0].rstrip().split()]
            dna = lines[1].rstrip().split()
        
        ans = self.MotifEnumeration(dna,k,d)
        self.ans = ' '.join(ans)
        return self.ans        

    def MedianString(self,dna:list,k:int) -> str:
        distance = 9999999999999999999
        kmers = self.GenerateKmers(dna,k)
        for pattern in kmers:
            for string in dna:
                for i in range(len(string)):
                    if self.HammingDistance(string[i:i+k], pattern) <= distance:
                        distance  = self.HammingDistance(string[i:i+k], pattern)
                        Median = pattern
        return Median
    
    def PromptMedianString(self,file_directory:str) -> str:
        with open(file_directory, 'r') as f:
            line = f.readlines()
            k = int(line[0].rstrip())
            dna = list(line[1].rstrip().split())
        ans = self.MedianString(dna,k)
        self.ans = ans
        return self.ans

    def Profile(self,kmer:str,matrix:dict):
        prob = 1
        for i in range(len(kmer)):
            nucleotide = kmer[i]
            prob *= matrix[nucleotide][i]
        return prob
    
    def ProfileMostProbableKmer(self,dna:str, k:int, matrix:list) -> str:
        kmers = self.GenerateKmers([dna], k)
        prob = 0 
        most_probable = ''

        for mer in kmers:
            mer_prob = self.Profile(mer,matrix)
            if mer_prob > prob:
                prob = mer_prob
                most_probable = mer
        print(f'Most Probable K-mer: {most_probable}\n\
         Probability: {prob}')
        return most_probable
    
    def PromptProfileMostProbableKmer(self,file_directory:str) -> str:

        with open(file_directory, 'r') as f:
            lines = f.readlines()
            dna = lines[0].rstrip()
            k = int(lines[1].rstrip())
            map_ = {
        'A': list(map(float, lines[2].rstrip().split())),
        'T': list(map(float, lines[3].rstrip().split())),
        'C': list(map(float, lines[4].rstrip().split())),
        'G': list(map(float, lines[5].rstrip().split()))}
        self.map_ = map_

        
        ans = self.ProfileMostProbableKmer(dna,k=k,matrix=map_)
        self.ans = ans
        return self.ans

        

prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
print(week3().PromptProfileMostProbableKmer(prompt_file))
print(week3().Profile('CCGAG', {'A': [0.2, 0.2, 0.3, 0.2, 0.3], 'T': [0.4, 0.3, 0.1, 0.5, 0.1], 'C': [0.3, 0.3, 0.5, 0.2, 0.4], 'G': [0.1, 0.2, 0.1, 0.1, 0.2]}))