
def print_dp(dp, adjust=6):
    for i in range(len(dp)):
        line = [str(v).rjust(adjust) for v in dp[i]]
        print(line)
