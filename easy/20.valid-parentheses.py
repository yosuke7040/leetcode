#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        num_open_word = 0
        num_close_word = 0
        for word in s:
            if word == "(" or word == "[" or word == "{":
                ans.append(word)
                num_open_word += 1
            else:
                num_close_word += 1
                if num_close_word > num_open_word:
                    return False

                open_word = ans.pop()
                print(open_word, word)
                if open_word == "(" and word == ")":
                    num_open_word -= 1
                    num_close_word -= 1
                    continue
                elif open_word == "{" and word == "}":
                    num_open_word -= 1
                    num_close_word -= 1
                    continue
                elif open_word == "[" and word == "]":
                    num_open_word -= 1
                    num_close_word -= 1
                    continue

                return False

        if num_open_word != 0:
            return False
        return True


# @lc code=end
