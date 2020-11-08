import math

class Proportion:

    def proportion(CSValues):

        try:
            ans = []

            total = sum(CSValues)

            for i in CSValues:

                temp = i/total

                ans.append('{:.4f}'.format(temp))

            return ans

        except:
            return 'Pay attion, also I can not divide by zero :('

#if __name__=="__main__":
#    print(Proportion.p roportion([5,9,10,12,6,3,4]))
