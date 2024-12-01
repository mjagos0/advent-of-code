#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> listA;
std::vector<int> listB;

void loader() {
    int a, b;
    while (std::cin >> a >> b) {
        listA.push_back(a);
        listB.push_back(b);
    }
}

void partI() {
    int acum = 0;

    std::sort(listA.begin(), listA.end());
    std::sort(listB.begin(), listB.end());
    for (int i = 0; i != listA.size(); i++) {
        acum += std::abs(listA[i] - listB[i]);
    }

    std::cout << acum << std::endl;
}

void partII() {
    std::sort(listA.begin(), listA.end());
    std::sort(listB.begin(), listB.end());

    int simil = 0;
    int curA = 0, curB = 0;
    while (curA != listA.size() && curB != listB.size()) {
        if (listB[curB] > listA[curA]) {
            curA++;
        } else if (listB[curB] < listA[curA]) {
            curB++;
        } else {
            simil += listA[curA];
            curB++;
        }
    }

    std::cout << simil << std::endl;
}

int main() {
    loader();
    partI();
    partII();

    return 0;
}