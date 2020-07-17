import sys
def next_permutation(n):
    index = n - 1
    while index > 0 and n_arr[index-1] >= n_arr[index]: # 순열의 구조를 파악 내림차순이 어디까지 위치하는지
        index -= 1
    if index <= 0:      # 입력받은 순열의 구조가 내림차순이면 마지막 순열
        return False
    j = n - 1
    while n_arr[j] <= n_arr[index-1]:   # 내림차순이 끝나는 위치는 i이고 내림차순은 마지막 순열을 뜻하므로
        j -= 1                      # i-1번째의 숫자를 바꿔야 하는데 앞의 수가 아닌 뒤에 있는 수 중에서 가장 작은수를 선택
    n_arr[index-1], n_arr[j] = n_arr[j], n_arr[index-1]
    j = n - 1
    while index < j:        # 바꿔준 순열의 형태가 첫번째 수열이 아닌 마지막 순열일 경우 첫번째 순열로 변경
        n_arr[index],n_arr[j] = n_arr[j],n_arr[index]
        index += 1
        j -= 1
    return True
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
if next_permutation(n):
    print(' '.join(map(str, n_arr)))
else:
    print(-1)