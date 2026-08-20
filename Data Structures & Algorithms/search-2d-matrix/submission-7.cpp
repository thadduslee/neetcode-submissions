class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int columns = matrix[0].size();
        int left = 0;
        int right = rows*columns -1;
        while(left<=right){
            int mid = (right-left)/2 + left;
            int row = mid/columns;
            int column = mid%columns;
            if(matrix[row][column] == target){
                return true;
            }
            else if(matrix[row][column] < target){
                left = mid +1;
            }
            else if (matrix[row][column] > target){
                right = mid -1;
            }
        }
        return false;
    }
};
