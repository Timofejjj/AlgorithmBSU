#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

std::vector<int> parent;
std::vector<int> rank;
int connectivity_components;

int find(int el) {
    if (parent[el] != el) {
        parent[el] = find(parent[el]);
    }
    return parent[el];
}

void Union(int el_1, int el_2) {
    int el_1_root = find(el_1);
    int el_2_root = find(el_2);

    if (el_1_root == el_2_root) {
        return;
    }
    if (rank[el_1_root] < rank[el_2_root]) {
        parent[el_1_root] = el_2_root;
    } else if (rank[el_1_root] > rank[el_2_root]) {
        parent[el_2_root] = el_1_root;
    } else {
        parent[el_2_root] = el_1_root;
        rank[el_1_root] += 1;
    }
    connectivity_components -= 1;
}

int main() {
    std::ifstream file("input.txt");
    if (!file.is_open()) {
        std::cerr << "Не удалось открыть input.txt" << std::endl;
        return 1;
    }

    std::vector<int> nums;
    int num;
    while (file >> num) {
        nums.push_back(num);
    }
    file.close();

    int towns_num = nums[0];
    int roads = nums[1];
    int earthquake = nums[2];

    parent.resize(towns_num);
    for (int i = 0; i < towns_num; i++) {
        parent[i] = i;
    }
    rank.resize(towns_num, 0);
    connectivity_components = towns_num;

    std::vector<std::pair<int, int>> conected_towns;
    std::vector<int> indexes_destroided_roads;

    int i = 3;
    for (int _ = 0; _ < roads; _++) {
        int t_1 = nums[i] - 1;
        int t_2 = nums[i + 1] - 1;
        conected_towns.push_back({t_1, t_2});
        i += 2;
    }

    for (int _ = 0; _ < earthquake; _++) {
        indexes_destroided_roads.push_back(nums[i] - 1);
        i += 1;
    }

    std::vector<bool> delited(roads, false);
    for (int idx : indexes_destroided_roads) {
        delited[idx] = true;
    }

    for (int i = 0; i < roads; i++) {
        if (!delited[i]) {
            int t_1 = conected_towns[i].first;
            int t_2 = conected_towns[i].second;
            Union(t_1, t_2);
        }
    }

    std::vector<char> res(earthquake, ' ');
    for (int j = earthquake - 1; j >= 0; j--) {
        if (connectivity_components == 1) {
            res[j] = '1';
        } else {
            res[j] = '0';
        }
        int idx = indexes_destroided_roads[j];
        int u = conected_towns[idx].first;
        int v = conected_towns[idx].second;
        Union(u, v);
    }

    std::ofstream output("output.txt");
    if (!output.is_open()) {
        std::cerr << "Не удалось открыть output.txt" << std::endl;
        return 1;
    }
    for (int i = 0; i < res.size(); i++) {
        output << res[i];
    }
    output.close();

    return 0;
}