class Solution:
    def maxNumberOfBalloons(self, text):

        dict = {
                'b' : 0,
                'a' : 0,
                'l' : 0,
                'o' : 0,
                'n' : 0
               }

        for i in text:
            if i in dict:
                dict[i] += 1

        dict['l'] = dict['l'] // 2
        dict['o'] = dict['o'] // 2

        return min(dict.values())
