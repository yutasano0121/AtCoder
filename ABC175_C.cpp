using namespace std;
#include <iostream>
#include <algorithm>
#include <vector>

long walk(long x, long k, long d){
    if (x <= d){
        if (k % 2 == 0) return x;
        else return d - x;
    }
    else {
        long res = x / d;
        if (res >= k) return x - d * k;
        else if ((k - res) % 2 == 0) return x % d;
        else return d - (x - d * res);
    }
}

int main(){
    long X, K, D;
    cin >> X;
    cin >> K;
    cin >> D;

    if (X < 0) X = -X;

    cout << walk(X, K, D);

    return 0;
}
