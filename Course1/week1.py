# constant file used to prompt different functions throughout week1 class
prompt_file = '/workspace/bioinfo/Course1/prompt.txt'

# Exercise break 
vibrio_cholerae_genome = ''
vibrio_cholerae_pattern = 'CTTGATCAT'

with open('/workspace/bioinfo/Course1/vibrio_cholerae_genome', 'r') as genome:
    vibrio_cholerae_genome += genome.readline().rstrip()

# Start 


class week1:
    def __init__(self):
        self.ans = ''
    
    def PatternCount(self,text:str,pattern:str) -> int:
        '''
        Given a pattern (k-mer, per example) count
        the number of occurences of this particular pattern in 
        text (genome portion)
        '''
        count = 0
        for i in range(len(text) - len(pattern) + 1):
            if text[i:i+len(pattern)] == pattern: 
                count += 1
        
        self.ans = count
        return self.ans
    
    def PromptPatternCount(self, file_directory:str) -> int:

        '''

        Accessory function to PatternCount (reading file prompt)

        '''
        with open(file_directory,'r') as f:
            lines = f.readlines()
            text = lines[0].rstrip()
            pattern = lines[1].rstrip()
        return self.PatternCount(text,pattern)

    def BetterFrequentWords(self,text:str,k:int) -> str:
        '''
        Given text (genome portion, per example) and size
        of k-mer, find most frequents in text,
        '''
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
        '''
        Accesory function to BetterFrequentWords,
        read text and k in prompt file
        '''
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            text = lines[0].rstrip()
            k = int(lines[1].rstrip())
        return self.BetterFrequentWords(text,k)
    
    def ReverseComplement(self,dna:str) -> str:
        '''
        given DNA, get its reverse complementary in result
        '''
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

        ''' 
        Accesory function to ReverseComplement,
        read inputs in prompt file (dna string)
        
        '''
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            dna = lines[0].rstrip()
        return self.ReverseComplement(dna)
    
    def PatternMatching(self,pattern:str,text:str) -> str:
        '''
        Given pattern (specific portion of genome, per example) and text (genome),
        find all repetitions of specific pattern in text
        '''


        matches = [] 

        for i in range(len(text) - len(pattern) + 1):
            if text[i:i + len(pattern)] == pattern:
                matches.append(str(i))
            
        self.ans = ' '.join(matches)
        return self.ans
    
    def PromptPatternMatching(self,file_directory:str) -> str:
        ''' 
        Accessory function to PatternMatching.
        Read pattern and text in prompt file 
         '''
        with open(file_directory, 'r') as f:
            lines = f.readlines()
            pattern = lines[0].rstrip()
            text = lines[1].rstrip()
        
        return self.PatternMatching(pattern,text)
    




print(week1().PatternMatching(vibrio_cholerae_pattern,vibrio_cholerae_genome))

