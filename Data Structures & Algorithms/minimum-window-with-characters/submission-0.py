from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Speaking cue: If t is empty or longer than s, no useful window exists.
        if not s or not t or len(t) > len(s):
            return ""

        # Speaking cue: Store the required frequency for every character in t.
        need = Counter(t)

        # Speaking cue: 'have' tracks frequencies inside the current window.
        have = {}

        # Speaking cue: 'formed' counts how many distinct requirements are satisfied.
        formed = 0
        required = len(need)

        # Speaking cue: These variables store the best window seen so far.
        best_length = float("inf")
        best_left = 0
        best_right = 0

        # Speaking cue: Expand the window by moving the right pointer across s.
        left = 0
        for right, char in enumerate(s):
            # Speaking cue: Add the new character to the current window count.
            have[char] = have.get(char, 0) + 1

            # Speaking cue: A requirement becomes satisfied exactly when its count matches.
            if char in need and have[char] == need[char]:
                formed += 1

            # Speaking cue: While valid, shrink from the left to minimize the window.
            while formed == required:
                window_length = right - left + 1

                # Speaking cue: Record this window if it is shorter than the best one.
                if window_length < best_length:
                    best_length = window_length
                    best_left = left
                    best_right = right

                # Speaking cue: Remove the leftmost character before moving left forward.
                left_char = s[left]
                have[left_char] -= 1

                # Speaking cue: The window becomes invalid if a required count drops below need.
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        # Speaking cue: Return the best substring, or an empty string if none was valid.
        if best_length == float("inf"):
            return ""
        return s[best_left:best_right + 1]
