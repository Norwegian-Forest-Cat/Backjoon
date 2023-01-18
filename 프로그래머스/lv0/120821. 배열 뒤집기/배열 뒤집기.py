def solution(num_list):
    N = len(num_list) // 2
    
    for i in range(N):
        num_list[i], num_list[-1-i] = num_list[-1-i], num_list[i]
        
    return num_list