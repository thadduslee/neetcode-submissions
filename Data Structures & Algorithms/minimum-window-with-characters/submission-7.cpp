class Solution {
public:
    string minWindow(string s, string t) {
        if(t.size()> s.size()){
            return "";
        }
        std::unordered_map<char, int> countT;
        for(auto c:t){
            countT[c]+=1;
        }
        int have = 0;
        int need = countT.size();
        int left = 0;
        int longest = INT_MAX;
        pair<int,int> answer = {0,0};
        std::unordered_map<char, int> count;
        for(int right = 0; right < s.size(); right +=1){
            char c = s[right];
            count[c] +=1;
            if(countT.count(c) and count[c] == countT[c]){
                have +=1;
            }
            while(have == need){
                count[s[left]] -=1;
                if(right-left+1 < longest){
                    longest = right-left+1;
                    answer = {left,right};
                }
                if(countT.count(s[left]) && count[s[left]] < countT[s[left]]){
                    have -=1;
                }
                left +=1;
            }
        }
        return longest == INT_MAX ? "": s.substr(answer.first,longest);
    }
};
