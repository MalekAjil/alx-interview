#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds"""
    def sieve(n):
        """Generate a list of primes up to n using the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """Simulate the game for a given n and return the winner."""
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return "Maria" if moves % 2 != 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
