class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> count1;
        for(auto c:s1){
            count1[c] += 1;
        }
        int need = count1.size();
        for(int i = 0; i < s2.size();i+=1){
            std::unordered_map<char,int> count2;
            int cur = 0;
            for(int j = i; j < s2.size(); j+=1){
                count2[s2[j]] +=1;

                if(count1[s2[j]] < count2[s2[j]]){
                    break;
                }
                if(count1[s2[j]] == count2[s2[j]]){
                    cur +=1;
                }
                if(cur == need){
                    return true;
                }
        }
        }
        return false;
    }
};
