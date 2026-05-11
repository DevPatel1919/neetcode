class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap <Character, Integer> gram = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }
        for (char c : s.toCharArray()) {
            if (!gram.containsKey(c)) {
                gram.put(c, 0);
            }
            gram.put(c, gram.get(c) + 1);
        }
        for (char c : t.toCharArray()) {
            if (!gram.containsKey(c)) {
                return false;
            }
            gram.put(c, gram.get(c) - 1);
        }
        for (int value: gram.values()) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }   
}
