"""
Input : “12abc345def67ghi”
Output : “12cba345fed67ihg”
"""

import re


class Solution:
    def reverse_alpha_segments(self, s: str) -> str:
        if not s:
            return s

        segments = []
        current_segment = s[0]  # Start with the first character
        for i in range(1, len(s)):
            # Check if the current character and the previous character are of the same type (both digits or both alphabetic)
            if (s[i].isdigit() and s[i - 1].isdigit()) or (
                s[i].isalpha() and s[i - 1].isalpha()
            ):
                current_segment += s[i]
                # print("19=", current_segment)
            else:
                # If the type changes, add the current segment to the list and start a new segment
                segments.append(current_segment)
                current_segment = s[i]
                # print("24=", current_segment)
        # Add the last segment
        segments.append(current_segment)
        # print(segments)
        # Reverse alphabetic segments
        for i in range(len(segments)):
            if segments[i].isalpha():
                segments[i] = segments[i][::-1]

        # Join the segments back into a single string
        return "".join(segments)

    def reverse_alpha_segments_re(self, s: str) -> str:
        # Split the string into segments of digits and non-digits
        segments = re.split(r"(\d+)", s)  # Use capturing group to keep delimiters

        # Reverse each alphabetic segment
        for i in range(len(segments)):
            if not segments[i].isdigit():  # Check if the segment is alphabetic
                segments[i] = segments[i][::-1]  # Reverse the segment

        # Join the segments back into a single string
        return "".join(segments)


# Test the function
input_str = "12abc345def67ghi"
s = Solution()
output_str = s.reverse_alpha_segments(input_str)
output_str_re = s.reverse_alpha_segments_re(input_str)
print(output_str)  # Output: "12cba345fed67ihg"
print(output_str_re)  # Output: "12cba345fed67ihg"
