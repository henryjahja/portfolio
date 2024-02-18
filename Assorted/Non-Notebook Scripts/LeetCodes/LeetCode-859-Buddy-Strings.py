# Incomplete
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #First Attempt
        if len(s) == 1 or len(s) != len(goal):
            return False
        else:
            #First Attempt
            # temp_s = ''
            # for i in range(len(s)):
            #     for j in range(len(s)):
            #         if i == j:
            #             continue
            #         else:
            #             temp_s = list(s)
            #             temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            #             if temp_s == list(goal):
            #                 return True
            # return False


            
            #Second Attempt
            s_ = {}
            for i in range(len(s)):
                s_[i] = s[i]
            goal_ = {}
            for i in range(len(goal)):
                goal_[i] = goal[i]
            
        
def runner(a,b):
    print(f'{a} with {b}\nResult: {sol.buddyStrings(None,a,b)}\n')
sol = Solution
runner('ab','ab')
runner('aa','aa')
runner('abcaa','abcbb')
runner('thequickbrownfoxjumpsoverthelazydog','thejuickbrownfoxqumpsoverthelazydog')
