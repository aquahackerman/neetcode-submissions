from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        q = deque([beginWord])
        visit = {beginWord}
        steps = 1

        def oneDiff(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff == 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                for nxt in wordList:
                    if nxt not in visit and oneDiff(word, nxt):
                        visit.add(nxt)
                        q.append(nxt)

            steps += 1

        return 0