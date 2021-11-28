//Name: Shahida Hoque
//Task 2B: User picks an integer in a range and computer guesses using approach
//similar to binary-search.

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){
    srand(time(0))
    int left;
    cout << "Enter left end in range: " << endl;
    cin >> left;
    int right;
    cout << "Enter right end in range: " << endl;
    cin >> right;
    cout << "User has an int in ["left", "right"].Computer will guess."<< endl

    int max = right;
    int min = left;
    int guess = (min+max)/2
    guess = (rand()%(max-min+1))+min;
    int correct;
    correct = (max == min)
    if (guess == correct){
        cout << "The answer must be " << guess << endl;
        break;
    }
    
    cout << guess << endl;
    cout << "How is my guess?" << endl;
    int a;
    cout << "1.too big 2.too small 3.just right" << endl;
    cout << "Enter only 1, 2, or 3: " << endl;
    cin >> a;

    while (guess != correct){
        if (a == 1){
            max = guess - 1;
        }
        else if (a == 2){
            min = guess + 1;
        }
        else if (a == 3){
            cout << "The answer must be " << guess << endl;
            break;
        }
    }
            
            
}
