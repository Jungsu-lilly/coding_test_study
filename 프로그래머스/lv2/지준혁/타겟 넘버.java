class Solution {
    
    public int solution(int[] numbers, int target) {
        
        return dfs(0, numbers, 0, target);
    }
    
    int dfs(int depth, int[] numbers, int sum, int target) {
        if (depth == numbers.length) {
            
            return sum == target ? 1 : 0;
        }
        
        int add = dfs(depth + 1, numbers, sum + numbers[depth], target);
        int substract = dfs(depth + 1, numbers, sum - numbers[depth], target);
        
        return add + substract;
    }
}
