//
// Created by Gerardo Barcenas on 8/5/23.
//

#include "q0412.h"

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> array;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                array.push_back("FizzBuzz");
            }
            else if (i % 3 == 0) {
                array.push_back("Fizz");
            }
            else if (i % 5 == 0) {
                array.push_back("Buzz");
            }
            else {
                array.push_back(to_string(i));
            }
        }

        return array;
    }
};