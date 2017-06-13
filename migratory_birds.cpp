#include <bits/stdc++.h>
#include <map>
#include <vector>

using namespace std;

typedef map<int, int> LouisMapping;

bool is_key_exist(LouisMapping *mapping, int *key){
    auto m = mapping->find(*key);
    return m != mapping->end();
}

void key_add_one(LouisMapping *mapping, int *key){
    if (is_key_exist(mapping, key)){
        auto m = mapping->find(*key);
        m->second = m->second + 1;
    }
    else{
        mapping->insert(mapping->begin(), make_pair(*key, 1));
    }
}

int get_great_value_key(LouisMapping *mapping){
    int key = 0, value = 0;
    bool is_assigned = false;
    for(auto it = mapping->begin(); it != mapping->end(); ++it) {
        if (!is_assigned){
            key = it->first;
            value = it->second;
            is_assigned = true;
        } else if ( is_assigned && (it->second > value) ){
            key = it->first;
            value = it->second;
        }
    }
    return key;
}

int migratoryBirds(int *n, vector <int> *ar) {
    // Complete this function
    LouisMapping bird_type_map;
    for (int i=0; i<*n; i++){
        key_add_one(&bird_type_map, &ar->at(i));
    }
    return get_great_value_key(&bird_type_map);
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = migratoryBirds(&n, &ar);
    cout << result << endl;
    return 0;
}
