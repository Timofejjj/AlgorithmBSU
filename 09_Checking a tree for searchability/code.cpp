#include <vector>
#include <fstream>
#include <limits>

const long long MIN_BOUND = -3000000000; // Adjust bounds as needed
const long long MAX_BOUND = 3000000000;

int main() {
    std::ifstream inputFile("bst.in");
    std::ofstream outputFile("bst.out");

    if (!inputFile || !outputFile) {
        outputFile << "NO";
        return 0;
    }

    long long numberOfNodes;
    inputFile >> numberOfNodes;

    if (numberOfNodes == 0) {
        outputFile << "NO";
        return 0;
    }

    std::vector<long long> nodeValues(numberOfNodes);
    std::vector<long long> minBounds(numberOfNodes, MIN_BOUND);
    std::vector<long long> maxBounds(numberOfNodes, MAX_BOUND);

    inputFile >> nodeValues[0]; // Read root node

    for (long long i = 1; i < numberOfNodes; ++i) {
        long long currentValue, parentIndex;
        char childType;

        if (!(inputFile >> currentValue >> parentIndex >> childType)) {
            outputFile << "NO";
            return 0; // Invalid input
        }

        nodeValues[i] = currentValue;

        // Adjust bounds for left and right children
        if (childType == 'L') {
            minBounds[i] = minBounds[parentIndex - 1];
            maxBounds[i] = nodeValues[parentIndex - 1];
        } else if (childType == 'R') {
            minBounds[i] = nodeValues[parentIndex - 1];
            maxBounds[i] = maxBounds[parentIndex - 1];
        }

        // Check if currentValue violates BST properties
        if (nodeValues[i] < minBounds[i] || nodeValues[i] >= maxBounds[i]) {
            outputFile << "NO";
            return 0;
        }
    }

    // If all nodes satisfy BST properties
    outputFile << "YES";
    return 0;
}
