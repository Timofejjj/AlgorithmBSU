#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>

using namespace std;
using ll = long long;

struct Stage {
    int machine;
    ll duration;
};

struct State {
    ll current_time;
    vector<int> current_stage;
    vector<ll> remaining_duration;
    ll priority; 
};

struct CompareStates {
    bool operator()(const State& a, const State& b) {
        return a.priority > b.priority; 
    }
};

int n;
vector<vector<Stage>> jobs;
ll minTime = numeric_limits<ll>::max();

void backtrack() {
    priority_queue<State, vector<State>, CompareStates> pq;
    vector<int> initialStage(2, 0);
    vector<ll> initialDuration(2, 0);
    for (int i = 0; i < 2; ++i) {
        if (!jobs[i].empty()) {
            initialDuration[i] = jobs[i][0].duration;
        }
    }
    ll initialPriority = 0; 
    pq.push({0, initialStage, initialDuration, initialPriority});

    while (!pq.empty()) {
        State s = pq.top(); pq.pop();
        ll t = s.current_time;
        vector<int> stage = s.current_stage;
        vector<ll> rem = s.remaining_duration;


        if (stage[0] >= jobs[0].size() && stage[1] >= jobs[1].size()) {
            minTime = min(minTime, t);
            continue;
        }


        if (t >= minTime) {
            continue;
        }


        ll lb = t;
        for (int i = 0; i < 2; ++i) {
            if (stage[i] < jobs[i].size()) {
                ll remSum = rem[i];
                for (size_t j = stage[i] + 1; j < jobs[i].size(); ++j) {
                    remSum += jobs[i][j].duration;
                }
                lb = max(lb, t + remSum);
            }
        }
        if (lb >= minTime) {
            continue;
        }


        vector<bool> canRun(2, false);
        vector<int> machine(2, -1);
        for (int i = 0; i < 2; ++i) {
            if (stage[i] < jobs[i].size()) {
                canRun[i] = true;
                machine[i] = jobs[i][stage[i]].machine;
            }
        }


        vector<State> nextStates;
        for (int mask = 1; mask < (1 << 2); ++mask) {
            vector<int> nextStage = stage;
            vector<ll> nextRem = rem;
            bool valid = true;
            vector<bool> machineUsed(n + 1, false);


            for (int i = 0; i < 2; ++i) {
                if (mask & (1 << i)) {
                    if (!canRun[i]) {
                        valid = false;
                        break;
                    }
                    if (machineUsed[machine[i]]) {
                        valid = false;
                        break;
                    }
                    machineUsed[machine[i]] = true;
                }
            }
            if (!valid) continue;


            ll timeToRun = numeric_limits<ll>::max();
            for (int i = 0; i < 2; ++i) {
                if (mask & (1 << i)) {
                    timeToRun = min(timeToRun, nextRem[i]);
                }
            }


            for (int i = 0; i < 2; ++i) {
                if (mask & (1 << i)) {
                    nextRem[i] -= timeToRun;
                    if (nextRem[i] == 0) {
                        nextStage[i]++;
                        if (nextStage[i] < jobs[i].size()) {
                            nextRem[i] = jobs[i][nextStage[i]].duration;
                        }
                    }
                }
            }


            ll heuristic = t + timeToRun;
            for (int i = 0; i < 2; ++i) {
                if (nextStage[i] < jobs[i].size()) {
                    ll remSum = nextRem[i];
                    for (size_t j = nextStage[i] + 1; j < jobs[i].size(); ++j) {
                        remSum += jobs[i][j].duration;
                    }
                    heuristic = max(heuristic, t + timeToRun + remSum);
                }
            }
            nextStates.push_back({t + timeToRun, nextStage, nextRem, heuristic});
        }


        for (const auto& state : nextStates) {
            pq.push(state);
        }
    }
}

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> n;
    jobs.resize(2);
    for (int i = 0; i < 2; ++i) {
        int s;
        fin >> s;
        jobs[i].resize(s);
        for (int j = 0; j < s; ++j) {
            fin >> jobs[i][j].machine >> jobs[i][j].duration;
        }
    }

    backtrack();
    fout << minTime << endl;

    fin.close();
    fout.close();
    return 0;
}