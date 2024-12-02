#include <iostream>
#include <vector>
#include <sstream>

std::vector<std::vector<int>> reports;

void loader() {
    std::string line;
    while (std::getline(std::cin, line)) {
        std::vector<int> levels;
        std::istringstream iss(line);
        int n;

        while (iss >> n) {
            levels.push_back(n);
        }

        reports.push_back(levels);
    }
}

void partI() {
    int safe = 0;
    for (std::vector<int>& report : reports) {
        bool desc = report[0] > report[1];
        bool passed = true;
        for (int i = 0; i != report.size()-1; i++) {
            if (abs(report[i] - report[i+1]) > 3 || (desc && report[i] <= report[i+1]) || (!desc && report[i] >= report[i+1])) {
                passed = false;
                break;
            }
        }

        if (passed) {
            safe++;
        }
    }

    std::cout << safe << std::endl;
}

int partII() {
    int safe = 0;
    for (std::vector<int>& report : reports) {
        bool desc = report[0] > report[1];
        bool passed = true;

        for (int j = 0; j < report.size(); j++) {
            std::vector<int> temp = report;
            temp.erase(temp.begin() + j);
            
            int tempPassed = true;
            desc = temp[0] > temp[1];
            for (int i = 0; i != temp.size() - 1; i++) {
                if (abs(temp[i] - temp[i + 1]) > 3 || 
                    (desc && temp[i] <= temp[i + 1]) || 
                    (!desc && temp[i] >= temp[i + 1])) {
                    tempPassed = false;
                    break;
                }
            }

            if (tempPassed) {
                safe++;
                break;
            }
        }
    }

    std::cout << safe << std::endl;
    return safe;
}


int main () {
    loader();
    partI();
    partII();
}