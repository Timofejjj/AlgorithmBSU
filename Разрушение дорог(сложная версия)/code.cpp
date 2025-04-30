#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

std::vector<int> parent;
std::vector<int> rank;
int connectivity_components;

inline int find(int el) {
    // Итеративная версия с компрессией пути
    while (parent[el] != el) {
        parent[el] = parent[parent[el]];  // Компрессия пути
        el = parent[el];
    }
    return el;
}

inline void Union(int el_1, int el_2) {
    int el_1_root = find(el_1);
    int el_2_root = find(el_2);

    if (el_1_root == el_2_root) {
        return;
    }
    
    if (rank[el_1_root] < rank[el_2_root]) {
        parent[el_1_root] = el_2_root;
    } else {
        parent[el_2_root] = el_1_root;
        if (rank[el_1_root] == rank[el_2_root]) {
            rank[el_1_root]++;
        }
    }
    
    connectivity_components--;
}

int main() {
    std::ios_base::sync_with_stdio(false);  // Ускорение ввода-вывода
    std::ifstream file("input.txt");
    if (!file.is_open()) {
        std::cerr << "Не удалось открыть input.txt" << std::endl;
        return 1;
    }

    int towns_num, roads, earthquake;
    file >> towns_num >> roads >> earthquake;
    
    parent.resize(towns_num);
    for (int i = 0; i < towns_num; i++) {
        parent[i] = i;
    }
    rank.resize(towns_num, 0);
    connectivity_components = towns_num;

    std::vector<std::pair<int, int>> conected_towns(roads);
    for (int i = 0; i < roads; i++) {
        int t_1, t_2;
        file >> t_1 >> t_2;
        conected_towns[i] = {t_1 - 1, t_2 - 1};
    }

    std::vector<int> indexes_destroided_roads(earthquake);
    for (int i = 0; i < earthquake; i++) {
        file >> indexes_destroided_roads[i];
        indexes_destroided_roads[i]--;
    }
    file.close();

    std::vector<bool> delited(roads, false);
    for (int idx : indexes_destroided_roads) {
        delited[idx] = true;
    }

    for (int i = 0; i < roads; i++) {
        if (!delited[i]) {
            Union(conected_towns[i].first, conected_towns[i].second);
        }
    }

    std::string res(earthquake, ' ');
    for (int j = earthquake - 1; j >= 0; j--) {
        res[j] = (connectivity_components == 1) ? '1' : '0';
        int idx = indexes_destroided_roads[j];
        Union(conected_towns[idx].first, conected_towns[idx].second);
    }

    std::ofstream output("output.txt");
    if (!output.is_open()) {
        std::cerr << "Не удалось открыть output.txt" << std::endl;
        return 1;
    }
    output << res;
    output.close();

    return 0;
}
    return 0;
}
