using namespace std;
#include <iostream>
#include <string>

int main(){
  string weather;
  cin >> weather;
  int max = 0;
  int count = 0;

  for (int i = 0; i < weather.length(); i++){
    if (i == 0){
      if (weather[i] == 'R'){
        count = 1;
        max = 1;
      }
    }
    else {
      if (weather[i] == 'R'){
        count += 1;
        if (max < count) max = count;
      }
      else count = 0;
    }
  }

  cout << max;
  return 0;
}
