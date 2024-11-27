#!/usr/bin/python3
"""  Change comes from within """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
    coins (list): List of coin denominations available
    total (int): Target total amount to make change for
    
    Returns:
    int: Fewest number of coins needed to meet total, or -1 if impossible
    """
    # Handle base cases
    if total <= 0:
        return 0
    
    # Initialize dynamic programming array
    # We use float('inf') to represent impossible combinations
    # Add 1 to total to include 0 as a valid index
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins needed to make 0
    dp[0] = 0
    
    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            # If coin value is less than or equal to current amount
            if coin <= amount:
                # Update minimum number of coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result, using -1 if no solution was found
    return dp[total] if dp[total] != float('inf') else -1