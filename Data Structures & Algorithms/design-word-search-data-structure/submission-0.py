class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]

        while stack:
            node, i = stack.pop()

            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for child in node.children.values():
                        stack.append((child, j + 1))
                    break
                else:
                    if c not in node.children:
                        break
                    node = node.children[c]
            else:
                if node.word:
                    return True

        return False