
class week1:
    def __init__(self):
        self.ans = ''
    
    def PatternCount(self,text:str,pattern:str) -> int:
        count = 0
        for i in range(len(text) - len(pattern) + 1):
            if text[i:i+len(pattern)] == pattern: 
                count += 1
        
        self.ans = count
        return self.ans
    
    def PromptPatternCount(self, file_directory:str) -> int:
        with open(file_directory,'r') as f:
            lines = f.readlines()
            text = lines[0].rstrip()
            pattern = lines[1].rstrip()
        return self.PatternCount(text,pattern)

    def BetterFrequentWords(self,text:str,k:int) -> str:
        kmers = {} 
        most_frequent_kmer = []

        for i in range(len(text) - k + 1):
            pattern = text[i:i+k]
            pattern_occurences = self.PatternCount(text, pattern)
            kmers[pattern] = pattern_occurences
        
        max_value = max(kmers.values())

        for kmer in kmers.keys():
            if kmers[kmer] >= max_value:
                most_frequent_kmer.append(kmer)
        
        self.ans = ' '.join(most_frequent_kmer)
        return self.ans
    
    def PromptBetterFrequentWords(self,file_directory:str) -> str:
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            text = lines[0].rstrip()
            k = int(lines[1].rstrip())
        return self.BetterFrequentWords(text,k)
    
    def ReverseComplement(self,dna:str) -> str:
        complementarity = {'A':'T',
        'T': 'A', 
        'C' : 'G', 
        'G' : 'C'}

        complementary_dna = ''
        for b in dna:
            complementary_dna += complementarity[b]
        
        self.ans = complementary_dna[::-1]
        return self.ans
    
    def PromptReverseComplement(self,file_directory:str) -> str:
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            dna = lines[0].rstrip()
        return self.ReverseComplement(dna)
    
    def PatternMatching(self,text:str,pattern:str):
        return




#prompt_file = '/workspace/bioinfo/Course1/prompt.txt'
#print(week1().PromptReverseComplement(prompt_file))

print('1')
