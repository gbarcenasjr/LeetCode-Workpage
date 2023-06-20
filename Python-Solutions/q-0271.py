"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/description/

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).



Example:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
"""


class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


if __name__ == '__main__':
    codec = Codec()
    example = ["The", "Class", "Works!", "#number1"]
    print(codec.decode(codec.encode(example)))
