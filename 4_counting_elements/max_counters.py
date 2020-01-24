def solution(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result



def solution2(N, A):
    counters = [0] * N
    max_val = 0
    current_max = 0
    for v in A:
        if 1 <= v <= N:
            if max_val > counters[v-1]:
                counters[v-1] = max_val
            counters[v-1] += 1
            if current_max < counters[v-1]:
                current_max = counters[v-1]
        else:
            max_val = current_max
    counters = [max(max_val,i) for i in counters]
    return counters