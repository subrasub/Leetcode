class Solution {
public:
    bool isValid(string s) {
        int para = 0;
        // int p_right = 0;
        int sq = 0;
        // int s_right = 0;
        int curl = 0;
        // int c_right = 0;
        
        for(int i=0; i< s.size(); i++){
            if(s[i]=='(')
                para = para + 1;
            else 
            if(s[i] == ')')
                para = para - 1;
            else
            if(s[i] == '{')
                curl = curl + 1;
            else
            if(s[i] == '}')
                curl = curl - 1;
            else
            if(s[i] == '[')
                sq = sq + 1;
            else
            if(s[i] == ']')
                sq = sq - 1;
            
            cout<<s[i];
            cout<<"\npara: "<<para<<endl;
            cout<<"curl: "<<curl<<endl;
            cout<<"sq: "<<sq<<endl;
        }
        
        if(para == 0 && curl == 0 && sq == 0)
            return true;
        return false;
    }
};