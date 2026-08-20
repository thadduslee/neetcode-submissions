class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!= t.length()){
            return false;
        }
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i+=1){
            count[s.charAt(i) - 'a'] +=1;
            count[t.charAt(i)- 'a'] -=1;
        }
        for(int value:count){
            if(value != 0){
                return false;
            }
        }
        return true;
    }
}
