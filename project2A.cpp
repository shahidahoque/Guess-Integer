/*
Name: Shahida Hoque 
Task 2A:Computer generates a random integer and user guesses. 
*/

#include <iostream>
#include <cstdlib> 
using namspace std;

int main(){
    int range;
    int random;
    int left;
    int right;
    int guess;
    
    cout << "Enter the left end of range: " << endl;
    cin >> left;
    cout << "Enter the right end of range: " << endl;
    cin >> right;
    
    range = (right - left) + 1;
    random = left + rand() % range;

    cout << "enter your guess: " << endl;
    cin >> guess;

    while(guess != random){
        if (guess > random){
            cout << "guess is too big" << endl;
        }
        else if (guess < random){
            cout << "guess is too small" << endl;
        }
    }
    if (guess == random){
        cout << "Congratulations!" << endl;
    }
    return 0;
}
