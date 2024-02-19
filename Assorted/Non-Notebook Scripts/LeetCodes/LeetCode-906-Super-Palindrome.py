#906. Super Palindromes
class Solution:
    def palindrome(n):
        n = str(n)
        return n==n[::-1]
    def superpalindromesInRange(self, left: str, right: str) -> int:
        p = 0
        n = 0
        left = int(left)
        right = int(right)
        while n**2 <= right:
            n += 1
            if n**2 < left:
                continue
            elif n**2 > right:
                return p
            else:
                if n**2 <= right and palindrome(n) and palindrome(n**2):
                    # p_list.append((n,n**2))
                    p += 1