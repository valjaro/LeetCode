class Solution:
    def longestPalindrome(self, s):
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
        if len(s) > 0:
            s = list(s)
            main = []
            l = 0
            for i in range(len(s)):
                if s[i] in s[i+1:] and len(s[i+1:]) > l:
                    ss = s[i]
                    for j in range(i+1, len(s)):
                        ss += s[j]
                        if ss == ss[::-1] and len(ss) > l:
                            main.append(ss)
                            l = len(ss)
                if len(main) < 1: main.append(s[i])
            # print(max(r, key=len))
            return main[-1]

if __name__ == "__main__":
    s = Solution()
    i ="tktneonoubkxgfhybavrfnetlxgtkelsoeeuznssntcleenqgiboexflfvlfiapqjbcwyenmfnmxcbcjscucqhwuqfzvvkdxrtxzhjdvsjawcwffoglhkxvyxaninlswyjcfvdwfkqheidwprtjaaqzqgloctafkuasubqqeacdpmtfzokccmnslnklxyvfitbfbdjrlzhkhnturfkimghcnngvdhbehewzzyfsbsactkrfabkhaavryubckkrqbqcbenqpeykyawzkctswaczbjtzeyteftsjklrtchxggsslscypkuilhbitsjwzsvwmqahxkmghigdtuqehjkqswchkrolcloxnkqocyjeorkwjmbevwijmqfhtmolspqcqshafjuxcheckguzxvapfivznkzdkzwnvlquzrbkhvmpdclrettjrxinbbvlwtsyepestvwjfiekjaqphfrhiifrplokslzaxmlwafrrfawlmxazlskolprfiihrfhpqajkeifjwvtsepeystwlvbbnixrjtterlcdpmvhkbrzuqlvnwzkdzknzvifpavxzugkcehcxujfahsqcqpslomthfqmjiwvebmjwkroejycoqknxolclorkhcwsqkjhequtdgihgmkxhaqmwvszwjstibhliukpycslssggxhctrlkjstfetyeztjbzcawstckzwaykyepqnebcqbqrkkcbuyrvaahkbafrktcasbsfyzzwehebhdvgnnchgmikfrutnhkhzlrjdbfbtifvyxlknlsnmcckozftmpdcaeqqbusaukfatcolgqzqaajtrpwdiehqkfwdvfcjywslninaxyvxkhlgoffwcwajsvdjhzxtrxdkvvzfquwhqcucsjcbcxmnfmneywcbjqpaiflvflfxeobigqneelctnssnzueeoslektgxltenfrvabyhfgxkbuonoentkt"
    r = s.longestPalindrome(i)
    print(r)