"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust==[] and N==1:
            return 1
        people_trust_others=set()
        for pair in trust:
            people_trust_others.add(pair[0])
        leader=[pair[1] for pair in trust]
        for pair in trust:
            if pair[1] not in people_trust_others:
                if leader.count(pair[1])==N-1:
                    return pair[1]
        return -1
