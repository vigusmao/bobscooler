from time import time
import sys

def clock(method, arguments):
    start = time()
    result = method(arguments)
    duration = time() - start
    print("Result = %d --- elapsed: %.6f seconds (%s)" %
          (result, duration, method.__name__))

def cont_seq_enumeration(n):
    count = 0
    for x in range(2**n):
        bin_x = bin(x)[2:]
        ok = True
        for pos in range(len(bin_x) - 1):
            if bin_x[pos] == bin_x[pos + 1] == '1':
                ok = False
                break
        if ok:
            count += 1
    return count



def cont_seq_backtracking(n):
    
    def backtrack(n, current, count_ptr):
        if len(current) == n:
            count_ptr[0] += 1
            return

        # loop through all candidate next steps
        for next_bit in [0, 1]:
            if next_bit == 0 or \
               len(current) == 0 or \
               current[-1] == 0:

                current.append(next_bit)
                backtrack(n, current, count_ptr)
                del(current[-1])


    result = [0]
    backtrack(n, [], result)
    return result[0]
        


def cont_seq_recursive(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return cont_seq_recursive(n-1) + cont_seq_recursive(n-2)



def cont_seq_memo(n):
    
    def run_memo(n, memo):
        result_from_memo = memo.get(n)
        if result_from_memo is not None:
            return result_from_memo
        
        if n == 1:
            result = 2
        elif n == 2:
            result = 3
        else:
            result = run_memo(n-1, memo) + run_memo(n-2, memo)
        memo[n] = result
        return result

    return run_memo(n, {})


    



N = 4500
sys.setrecursionlimit(N + 10)
##clock(cont_seq_enumeration, N)
##clock(cont_seq_backtracking, N)
##clock(cont_seq_recursive, N)
clock(cont_seq_memo, N)




        
