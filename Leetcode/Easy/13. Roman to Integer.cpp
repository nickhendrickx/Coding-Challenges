class Solution {
public:
    int romanToInt(string s) {
        char curr;
        int sum = 0;
        int currInt = 0;;
        int lastInt = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            curr = s[i];
            currInt = romanCharToInt(curr);
            if(currInt >= lastInt){  
                sum += currInt;
            } else {
                sum -= currInt;
            }
            lastInt = currInt;
        }
        return sum;
    }

    int romanCharToInt(char c){
        switch(c) {
            case 'I':
                return 1;
                break;
            case 'V':
                return 5;
                break;
            case 'X':
                return 10;
                break;
            case 'L':
                return 50;
                break;
            case 'C':
                return 100;
                break;
            case 'D':
                return 500;
                break;
            case 'M':
                return 1000;
                break;
            default:
                return 0;
        }
    }
};