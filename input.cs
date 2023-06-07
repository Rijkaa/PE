using System;
class MyClass {
    int myInt;
    bool myBool;
    string myString;
    void myFunction(int myParam) {
        if (myBool) {
            for (int i = 0; i < myParam; i++) {
                myInt += i;
            }
        } else {
            while (myInt < myParam) {
                myInt++;
            }
        }
    }
}