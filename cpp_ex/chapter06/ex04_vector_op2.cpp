#include <vector>
#include <iostream>
using namespace std;
int main() {
    vector<int> v;
    for(int i=0; i<10; i++) {
        v.push_back(i);
    }

    for(auto& e: v) {
        cout << e << ' ';
    }

    cout << endl;

    cout << "����" << endl;

    while(v.empty() != true) {
        cout << v.back() << " ";
        v.pop_back();
    }
    return 0;
}