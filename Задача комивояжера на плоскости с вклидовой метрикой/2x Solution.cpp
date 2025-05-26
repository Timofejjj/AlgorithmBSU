#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <climits>
#include <stack>

using namespace std;

struct Point {
    long long x, y;
};


long long manhattanDistance(const Point& a, const Point& b) {
    return abs(a.x - b.x) + abs(a.y - b.y);
}


vector<int> primMST(int n, const vector<Point>& coords) {
    vector<bool> inMST(n, false);
    vector<long long> distance(n, LLONG_MAX);
    vector<int> parent(n, -1);
    
    distance[0] = 0;
    
    for (int count = 0; count < n; count++) {
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (!inMST[i] && (u == -1 || distance[i] < distance[u])) {
                u = i;
            }
        }
        
        inMST[u] = true;
        
        for (int v = 0; v < n; v++) {
            if (!inMST[v]) {
                long long d = manhattanDistance(coords[u], coords[v]);
                if (d < distance[v]) {
                    distance[v] = d;
                    parent[v] = u;
                }
            }
        }
    }
    
    return parent;
}


vector<int> findEulerianPath(const vector<vector<int>>& adj, int start) {
    vector<int> path;
    stack<int> st;
    st.push(start);
    
    vector<vector<int>> tempAdj = adj; 
    
    while (!st.empty()) {
        int u = st.top();
        if (!tempAdj[u].empty()) {
            int v = tempAdj[u].back();
            tempAdj[u].pop_back();
            
            for (size_t i = 0; i < tempAdj[v].size(); i++) {
                if (tempAdj[v][i] == u) {
                    tempAdj[v][i] = tempAdj[v].back();
                    tempAdj[v].pop_back();
                    break;
                }
            }
            st.push(v);
        } else {
            path.push_back(u);
            st.pop();
        }
    }
    
    reverse(path.begin(), path.end());
    return path;
}


vector<int> shortcutToHamilton(const vector<int>& path, int n) {
    vector<int> tour;
    vector<bool> visited(n, false);
    
    for (int v : path) {
        if (!visited[v]) {
            tour.push_back(v);
            visited[v] = true;
        }
    }
    
    return tour;
}


pair<vector<int>, long long> solution(int cities, const vector<Point>& coordinates) {

    vector<int> parent = primMST(cities, coordinates);
    

    vector<vector<int>> adj(cities);
    for (int i = 1; i < cities; i++) {
        if (parent[i] != -1) {
            adj[parent[i]].push_back(i);
            adj[i].push_back(parent[i]);
        }
    }
    

    vector<int> eulerianPath = findEulerianPath(adj, 0);
    

    vector<int> tspTour = shortcutToHamilton(eulerianPath, cities);
    tspTour.push_back(tspTour[0]); // Закрываем цикл
    

    long long totalLength = 0;
    for (int i = 0; i < tspTour.size() - 1; i++) {
        int u = tspTour[i];
        int v = tspTour[i + 1];
        totalLength += manhattanDistance(coordinates[u], coordinates[v]);
    }
    
    return make_pair(tspTour, totalLength);
}

int main() {
    ifstream input("input.txt");
    ofstream output("output.txt");
    
    int n;
    input >> n;
    
    vector<Point> coordinates(n);
    for (int i = 0; i < n; i++) {
        input >> coordinates[i].x >> coordinates[i].y;
    }
    
    pair<vector<int>, long long> result = solution(n, coordinates);
    vector<int> tspTour = result.first;
    long long totalLength = result.second;
    

    for (int i = 0; i < tspTour.size(); i++) {
        if (i > 0) output << " ";
        output << (tspTour[i] + 1);
    }
    output << "\n";
    output << totalLength << "\n";
    
    input.close();
    output.close();
    
    return 0;
}