from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
      
        graph = defaultdict(set)

        letters = set()
        for word in words:
            for ch in word:
                letters.add(ch)

        # Compare every pair of words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1 = words[i]
                w2 = words[j]

                k = 0
                while k < min(len(w1), len(w2)) and w1[k] == w2[k]:
                    k += 1

                # Prefix invalidity
                if k == min(len(w1), len(w2)):
                    if len(w1) > len(w2):
                        return ""
                    continue

                graph[w1[k]].add(w2[k])

        # Topological sort with cycle detection
        state = {}  # 0=unvisited, 1=visiting, 2=visited
        res = []

        def dfs(node):
            if node in state:
                return state[node] == 2

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            res.append(node)
            return True

        for ch in letters:
            if ch not in state:
                if not dfs(ch):
                    return ""

        return "".join(res[::-1])