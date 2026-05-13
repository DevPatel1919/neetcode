class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet <Integer> duplicate = new HashSet<>();

        for (int dup : nums) {
            if (duplicate.contains(dup)) {
                return true;
            }
            duplicate.add(dup);
        }
        return false;
    }
}