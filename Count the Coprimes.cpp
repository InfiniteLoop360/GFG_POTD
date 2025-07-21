class Solution {
    static const int MAX = 10000;
    int mobius[MAX + 1];

public:
    void computeMobius() {
        fill(mobius, mobius + MAX + 1, 1);
        vector<bool> isPrime(MAX + 1, true);

        for (int i = 2; i <= MAX; i++) {
            if (isPrime[i]) {
                for (int j = i; j <= MAX; j += i) {
                    mobius[j] *= -1;
                    isPrime[j] = false;
                }
                for (int j = i * i; j <= MAX; j += i * i) {
                    mobius[j] = 0;
                }
            }
        }
    }

    int cntCoprime(const vector<int>& arr) {
        computeMobius();

        vector<int> freq(MAX + 1, 0);
        for (int num : arr) {
            freq[num]++;
        }

        vector<int> divisibleCount(MAX + 1, 0);
        for (int d = 1; d <= MAX; d++) {
            for (int j = d; j <= MAX; j += d) {
                divisibleCount[d] += freq[j];
            }
        }

        long long total = 0;
        for (int d = 1; d <= MAX; d++) {
            int count = divisibleCount[d];
            long long pairs = 1LL * count * (count - 1) / 2;
            total += 1LL * mobius[d] * pairs;
        }

        return static_cast<int>(total);
    }
};
