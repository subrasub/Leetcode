class Solution {
public:
    bool isValid(string s) {
        if(s.size()==0)
            return true;
        if(s.size()%2 != 0)
            return false;
        
        stack <char> res;
        
        map<char,char> par;
        par[')'] = '(';
        par[']'] = '[';
        par['}'] = '{';
        
        for(int i=0; i<s.size(); i++){
            if(s[i] == '{' || s[i] == '(' || s[i] == '[')
                res.push(s[i]);
            if(s[i] == '}' || s[i] == ')' || s[i] == ']'){
                if(res.empty() || res.top() != par[s[i]])
                    return false;
                else
                    res.pop();
            }
        }
        return res.empty()? true: false;
    }
};