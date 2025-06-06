class Solution:
    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        if m > n:
            return []
        
        base = 256  # base for characters
        mod = 10**9 + 7  # large prime to avoid collisions

        # Calculate the hash of pattern and first window of text
        pat_hash = 0
        txt_hash = 0
        h = 1  # base^(m-1)

        for i in range(m-1):
            h = (h * base) % mod

        for i in range(m):
            pat_hash = (base * pat_hash + ord(pat[i])) % mod
            txt_hash = (base * txt_hash + ord(txt[i])) % mod

        result = []
        for i in range(n - m + 1):
            # If the hash values match, compare the actual substring
            if pat_hash == txt_hash:
                if txt[i:i+m] == pat:
                    result.append(i + 1)  # 1-based indexing

            # Calculate hash of next window
            if i < n - m:
                txt_hash = (base * (txt_hash - ord(txt[i]) * h) + ord(txt[i + m])) % mod
                if txt_hash < 0:
                    txt_hash += mod

        return result
