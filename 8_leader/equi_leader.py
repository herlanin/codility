def solution(A):
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1
    # Find out a leader candidate
    for index in xrange(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= A_len//2:
        # The candidate is not the leader
        return 0
    else:
        leader = candidate
    equi_leaders = 0
    leader_count_so_far = 0
    for index in xrange(A_len):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 and
           leader_count-leader_count_so_far > (A_len-index-1)//2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            equi_leaders += 1
    return equi_leaders

def solution(A):
    # write your code in Python 2.7
    size = len(A)
    cnt, cnt1, s, ans = 0, 0, 0, 0
    for i in A:
        if 0 == cnt:
            s = i
        if s == i:
            cnt += 1
        else:
            cnt -= 1
    cnt = A.count(s)
    if cnt > size // 2:
        for i in range(size):
            if A[i] == s:
                cnt1 += 1
            if cnt1 > (i + 1) // 2 and cnt - cnt1 > (size - 1 - i) // 2:
                ans += 1
    return ans