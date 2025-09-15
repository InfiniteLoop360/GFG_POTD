class Solution:
    def stringStack(self, pat, tar):
        i, j = len(pat) - 1, len(tar) - 1
        skip = 0  # counts pending deletions

        while i >= 0:
            if skip > 0:
                skip -= 1
                i -= 1
            elif j >= 0 and pat[i] == tar[j]:
                # match character
                i -= 1
                j -= 1
            else:
                # delete current character
                skip += 1
                i -= 1

        return j < 0
