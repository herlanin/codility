def solution(S, P, Q):
    result = []
    DNA_len = len(S)
    mapping = {"A":1, "C":2, "G":3, "T":4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return resultition j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return resultsition j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return resultition j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return result


def solution(S, P, Q):
    n = len(S)
    sumA = [0]*(n+1)
    sumC = [0]*(n+1)
    sumG = [0]*(n+1)
    sumT = [0]*(n+1)
    for idx, nucleotide in enumerate(S):
        sumA[idx+1] = sumA[idx]
        sumC[idx+1] = sumC[idx]
        sumT[idx+1] = sumT[idx]
        sumG[idx+1] = sumG[idx]
        if nucleotide == 'A':
            sumA[idx+1] += 1
        elif nucleotide == 'C':
            sumC[idx+1] += 1
        elif nucleotide == 'G':
            sumG[idx+1] += 1
        else:
            sumT[idx+1] += 1
    result = [0]*len(P)
    for i in range(len(P)):
        AsInRange = sumA[Q[i] + 1]- sumA[P[i]]
        CsInRange = sumC[Q[i] + 1]- sumC[P[i]]
        GsInRange = sumG[Q[i] + 1]- sumG[P[i]]
        #TsInRange = sumT[Q[i] + 1]- sumT[P[i]]
        if AsInRange > 0:
            result[i] = 1
        elif CsInRange > 0:
            result[i] = 2
        elif GsInRange > 0:
            result[i] = 3
        else:
            result[i] = 4
    return result