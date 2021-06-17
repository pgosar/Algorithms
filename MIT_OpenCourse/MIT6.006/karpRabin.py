#run time is O(len(string)+len(pattern))

def karpRabin(string, pattern):
    pat = 0
    text = 0
    hash = 1
    
    for i in range(len(pattern)-1):
        hash = (hash*256) % 101
    
    for i in range(len(pattern)):
        pat = (256*pat + ord(pattern[i])) % 101
        text = (256*text + ord(string[i])) % 101
        
    for i in range(len(string)-len(pattern)+1):
        
        if pat == text:
            for j in range(len(pattern)):
                if string[i+j] != pattern[j]:
                    break
                else:
                    j+=1
            if j==len(pattern):
                print("pattern at index " + str(i))
        if i < len(string)-len(pattern):
            text = (256*(text-ord(string[i])*hash)+ord(string[i+len(pattern)])) % 101
            
            if text < 0:
                text+=101

karpRabin("AABAACAADAABAABA","AABA")