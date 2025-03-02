#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<long long>> arr(N, vector<long long>(M));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    long long max_sum = 0;

    for (int top = 0; top < N; top++) {
        vector<long long> temp(M, 0);
    
        for (int bottom = top; bottom < N; bottom++) {

            for (int j = 0; j < M; j++) {
                temp[j] += arr[bottom][j];
            }

            long long current = 0, current_max = 0;
            for (int x : temp) {
                current = max(0LL, current + x);
                current_max = max(current_max, current);
            }

            max_sum = max(max_sum, current_max);
        }
    }

    cout << max_sum << endl;
    return 0;
}
