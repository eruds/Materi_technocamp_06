// First Example 
#include <iostream>
using namespace std; 

int main() { 
    // Conditional Example 1
    int x = 10; 
    int y = 10;
    if( x == y ){ 
        cout << "Var x (" << x << ") Is Equals to var y (" << y << ")" << endl;
    }
    
    // Conditional Example 2 
    int A; 
    cout << "Tahun berapakah yang ingin Anda cek? : " << endl;
    cin >> A; 
    if (A % 4 == 0){ 
        if (A % 100 == 0){ 
            if (A % 400 == 0) {
                cout << "Tahun tersebut merupakan tahun kabisat" << endl;
            } else {
                cout << "Tahun tersebut bukan tahun kabisat" << endl;
            }}
        else {
                cout << "Tahun tersebut merupakan tahun kabisat" << endl;
            }}
    else {
        cout << "Tahun tersebut bukan tahun kabisat" << endl;
    }


    return 0;
}