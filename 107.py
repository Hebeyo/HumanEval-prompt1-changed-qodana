def even_odd_palindrome(n):
    even_palindrome_count = 0
    odd_palindrome_count = 0
    for i in range(1, n+1):
        if i%2 == 1 and str(i) == str(i)[::-1]:
            odd_palindrome_count += 1
        elif i%2 == 0 and str(i) == str(i)[::-1]:
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)
