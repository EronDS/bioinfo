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

    def BetterFrequentWords(self,text:str,k:int):
        kmers = {} 

        for i in range(len(text) - k + 1):
            pattern = text[i:i+k]
            pattern_occurences = self.PatternCount(text, pattern)
            kmers[pattern] = pattern_occurences
        
        return kmers





dic = week1().BetterFrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)
print(dic)
