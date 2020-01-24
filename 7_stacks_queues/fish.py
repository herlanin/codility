def solution(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream
    for index in xrange(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1
    # Currently, all the downstream-flow fishs in stack
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)
    return alive_count


 def solution(A, B):
    survivals = 0
    stack = []
    for idx in xrange(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    #print "downstream ate candidate"
                    break
                else:
                    #print "upstream ate stack"
                    stack.pop()
            else:
                survivals += 1
                #print "fish size", A[idx], "survived"
        else:
            stack.append(A[idx])
            #print "stack push", A[idx]
    survivals += len(stack)
    #print len(stack), "downstreams survived"
    return survivals

 def solution(A, B):
    survivals = 0
    stack = []
    for idx in xrange(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    #print "downstream ate candidate"
                    break
                else:
                    #print "upstream ate stack"
                    stack.pop()
            else:
                survivals += 1
                #print "fish size", A[idx], "survived"
        else:
            stack.append(A[idx])
            #print "stack push", A[idx]
    survivals += len(stack)
    #print len(stack), "downstreams survived"
    return survivals


def solution(A, B):
    stack = []
    for i in range(len(A)):
        live_fish = i
        while B[live_fish] == 0 and stack and B[stack[-1]] == 1:
            other_fish = stack.pop()
            if A[other_fish] > A[live_fish]:
                live_fish = other_fish
        stack.append(live_fish)
    return len(stack)