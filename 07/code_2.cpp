#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>

using namespace std;

int main() {
    size_t N, M;
    cin >> N >> M;

    vector<vector<int64_t>> arr(N, vector<int64_t>(M));
    
    for (size_t i = 0; i < N; i++) {
        for (size_t j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    int64_t max_sum = 0;

    for (size_t top = 0; top < N; top++) {
        vector<int64_t> temp(M, 0);
    
        for (size_t bottom = top; bottom < N; bottom++) {

            for (size_t j = 0; j < M; j++) {
                temp[j] += arr[bottom][j];
            }

            int64_t current = 0, current_max = 0;
            for (auto&& x : temp) {
                current = max(0LL, current + x);
                current_max = max(current_max, current);
            }

            max_sum = max(max_sum, current_max);
        }
    }

    cout << max_sum << endl;
    return 0;
}
