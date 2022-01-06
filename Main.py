# Sequence
#def isValidSubsequence(array, sequence):
#    arrIndx = 0
#    seqIndx = 0

#    while arrIndx < len(array) and seqIndx < len(sequence):
#        if array[arrIndx] == sequence[seqIndx]:
 #           arrIndx += 1
 #           seqIndx +=1

 #   return seqIndx == len(sequence)

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx ==len(sequence):
            break
            sequence[seqIdx] == value
            seqIdx +=1
            return seqIdx == len(sequence)












    a




