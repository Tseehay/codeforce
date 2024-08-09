t = int(input())
for z in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for k in range(n)]
    max_sum = 0 

    # Initialize diagonal sums
    main_diagonal_sum = [0] * (n + m - 1)
    anti_diagonal_sum = [0] * (n + m - 1)
    
    # Calculate diagonal sums
    for i in range(n):
        for j in range(m):
            main_diagonal_sum[i + j] += board[i][j]
            anti_diagonal_sum[i - j + (m - 1)] += board[i][j]
    
    # Initialize maximum sum
    max_sum = 0
    
    # Calculate maximum sum for each position (i, j)
    for i in range(n):
        for j in range(m):
            # Calculate the sum of all cells attacked by the bishop at (i, j)
            current_sum = (main_diagonal_sum[i + j] + anti_diagonal_sum[i - j + (m - 1)] - board[i][j])
            # Update maximum sum if the current sum is larger
            max_sum = max(max_sum, current_sum)
    print(max_sum)
