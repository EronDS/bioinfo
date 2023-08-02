from itertools import product
import copy

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
    
    def ProfileMostProbableKmer(self, dna: str, k: int, matrix: dict) -> str:
        kmers = self.GenerateKmers([dna], k)
        
        prob = 0.0
        most_probable = ''
        for mer in kmers:
            mer_prob = self.Profile(mer, matrix)
            if mer_prob > prob:
                prob = mer_prob
                most_probable = mer

        return most_probable

    
    def PromptProfileMostProbableKmer(self,file_directory:str) -> str:

        with open(file_directory, 'r') as f:
            lines = f.readlines()
            dna = lines[0].rstrip()
            k = int(lines[1].rstrip())
            map_ = {
        'A': list(map(float, lines[2].rstrip().split())),
        'C': list(map(float, lines[3].rstrip().split())),
        'G': list(map(float, lines[4].rstrip().split())),
        'T': list(map(float, lines[5].rstrip().split()))}
        self.map_ = map_
        
        ans = self.ProfileMostProbableKmer(dna,k=k,matrix=map_)
        self.ans = ans
        return self.ans

    def GenerateProfileMatrix(self, kmers: list):
        # initiate counting dictionary
        k = len(kmers[0])
        map_ = {'A': [0 for _ in range(k)],
                'C': [0 for _ in range(k)],
                'G': [0 for _ in range(k)],
                'T': [0 for _ in range(k)]}

        # count kmer in dictionary (for each position)
        for kmer in kmers:
            for i in range(len(kmer)):
                nucleotide = kmer[i]
                map_[nucleotide][i] += 1

        # create a separate map_freq dictionary to store frequencies
        map_freq = {'A': [0 for _ in range(k)],
                    'C': [0 for _ in range(k)],
                    'G': [0 for _ in range(k)],
                    'T': [0 for _ in range(k)]}

        # transform count into frequencies
        for nucleotide in map_.keys():
            for i in range(len(map_[nucleotide])):
                total = map_['A'][i] + map_['T'][i] + map_['C'][i] + map_['G'][i]
                map_freq[nucleotide][i] = map_[nucleotide][i] / total

        return map_freq
    
    def Score(self,kmers:list):
        k = len(kmers[0])
        map_ = {'A': [0 for _ in range(k)],
                'C': [0 for _ in range(k)],
                'G': [0 for _ in range(k)],
                'T': [0 for _ in range(k)]}

        # count kmer in dictionary (for each position)
        for kmer in kmers:
            for i in range(len(kmer)):
                nucleotide = kmer[i]
                map_[nucleotide][i] += 1
        
        c = 0
        most_frequents = [] 

        for i in range(k):
            max_value = 0
            for nucl in map_.keys():
                if map_[nucl][i] > max_value:
                    max_value = map_[nucl][i]
                    most_frequent = nucl

            most_frequents.append(most_frequent)

        for mer in kmers:
            for i in range(len(mer)):
                if mer[i] != most_frequents[i]:
                    c += 1
        return c
    

    def GreedyMotifSearch(self, k: int, t: int, dna: list) -> list:
        best_motifs = [string[:k] for string in dna]
        motifs = [string[:k] for string in dna]
        kmers = self.GenerateKmers([dna[0]], k)

        for i in range(len(kmers)):
            motifs[0] = kmers[i]
            for u in range(1, t):
                profile = self.GenerateProfileMatrix(motifs[:u])
                most_probable_motif = self.ProfileMostProbableKmer(dna[u], k, profile)
                if most_probable_motif!='': motifs[u] = most_probable_motif


            if self.Score(motifs) < self.Score(best_motifs):
                best_motifs = motifs.copy()  # Create a new list for best_motifs

        return best_motifs

    def PromptGreedyMotifSearch(self,file_directory:str) -> str:
        with open(file_directory,'r') as f:
            lines = f.readlines()
            k,t = [int(i) for i in lines[0].rstrip().split()]
            dna = list(lines[1].rstrip().split())

        ans = self.GreedyMotifSearch(k,t,dna)
        self.ans = ' '.join(ans)
        with open('/workspace/bioinfo/results.txt', 'w') as w:
            w.write(self.ans)
        return self.ans

prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
print(week3().PromptGreedyMotifSearch(prompt_file))

