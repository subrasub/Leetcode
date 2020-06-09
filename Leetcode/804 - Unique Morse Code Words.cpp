// https://leetcode.com/problems/unique-morse-code-words/
// Tags - String

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
       vector<string> MORSE = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
           unordered_set<string> mcode;
           
    for(auto word:words){
        string code = "";
        for(auto ch:word)
            code+=MORSE[ch-'a'];
        mcode.insert(code); 
        }
        
        return mcode.size();
    }
};