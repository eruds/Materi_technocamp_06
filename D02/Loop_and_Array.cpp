#include <iostream>
using namespace std; 


int main(int argc, char const *argv[])
{
    // Print 3 Hello Worlds
    for (int i = 0; i < 3; i++)
    {
        printf("Hello World!\n"); 
    }
    
    // Using the i Variable 
    for (int i = 0; i < 3; i++)
    {
        cout << i << endl; 
    }
    
    // Using Steps 
    for (int i = 0; i < 10; i += 2 )
    {
        printf("%i",i); 
    }
    
    // Negative Steps
    for (int i = 10; i > 0; i--)
    {
        cout << i << endl; 
    }
    
    int i = 0; 
    while ( i < 4 )
    {
        cout << i << endl; 
        i++;
    }

    // List of Food 
    string food[] = { 
        "A Food", "Another Food", "A Whole Chicken", "A Pizza", 
    };


    // Doesn't work 
    cout << food << endl; 

    // How You can Print an Array
    // Find the length of an array 
    int foodLength = sizeof(food)/sizeof(food[0]);
    // cout << sizeof(food) << endl;
    // cout << sizeof(food[0]) << endl;
    // Print the Array 
    for (int i = 0; i < foodLength; i++)
    {
        cout << food[i] << endl;
    }

    // Merging Lists 
    string notFood[] = { "Car", "Bicycles", "Trucks"};
    int notFoodLength = sizeof(notFood)/sizeof(notFood[0]);
    printf("%i", notFoodLength);
    string merged[foodLength+notFoodLength]; 
    // Merging two arrays 
    for (int i = 0; i < foodLength+notFoodLength; i++)
    {
        if( i < foodLength ){ 
            merged[i] = food[i];
        } else { 
            merged[i] = notFood[i-foodLength];
        }
        cout << merged[i] << endl;
    }
    // Printing 


    // List with range 
    int intList[5]; 
    int intListLength = sizeof(intList)/sizeof(intList[0]);
    for (int i = 0; i < intListLength; i++)
    {
        intList[i] = i;
    };
    
    for (int i = 0; i < intListLength; i++)
    {
        cout << intList[i] << endl;
    };



    // Palindrome 

    return 0;
}
