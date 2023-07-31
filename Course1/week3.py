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
        





prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
print(week3().PromptMotifEnumeration(prompt_file))




