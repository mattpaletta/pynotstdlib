import pickle
from typing import List


class Trie(object):
    # Based on: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of
    # -code-a877ea23c1a1
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children: [Trie] = []
        # Is it the last character of the word.`
        self.word_finished = False

    def merge(self, trie):
        vals1 = trie.get_all()
        vals2 = self.get_all()
        self.add_multiple(words = [x for x in vals1 if not x in vals2])

    def intersection(self, trie):
        vals1 = trie.get_all()
        vals2 = self.get_all()
        new_trie = Trie(char = "")
        new_trie.add_multiple(words = [x for x in vals1 if x in vals2])
        return new_trie

    def add_multiple(self, words: List[str]):
        for word in words:
            self.add(word)

    def save(self, trie_file: str):
        pickle.dump(obj = self.get_all(), file = trie_file)

    def load(self, trie_file: str):
        self.add_multiple(words = pickle.load(trie_file))

    def add(self, word: str):
        root = self

        def _add():
            """
            Adding a word in the trie structure
            """
            node = root
            for char in word:
                found_in_child = False
                # Search for the character in the children of the present `node`
                for child in node.children:
                    if child.char == char:
                        # We found it, increase the counter by 1 to keep track that another
                        # word has it as well
                        # And point the node to the child that contains this char
                        node = child
                        found_in_child = True
                        break
                # We did not find it so add a new chlid
                if not found_in_child:
                    new_node = Trie(char)
                    node.children.append(new_node)
                    # And then point node to the new child
                    node = new_node
            # Everything finished. Mark it as the end of a word.
            node.word_finished = True
        return _add()

    def get_all(self) -> [str]:
        root = self

        def __get_all(node, path: [str], acc: [str]):
            path.append(node.char)

            if root.word_finished:
                acc.append("".join(path))
            for c in root.children:
                child: Trie = c
                for i in __get_all(child, path, acc):
                    acc.append(i)
            return acc

        return __get_all(root, path = [], acc = [])

    def contains(self, prefix: str) -> bool:
        root = self

        def _contains():
            """
            Check and return
              1. If the prefix exsists in any of the words we added so far
              2. If yes then how may words actually have the prefix
            """
            node = root
            # If the root node has no children, then return False.
            # Because it means we are trying to search in an empty trie
            if not root.children:
                return False
            for char in prefix:
                char_not_found = True
                # Search through all the children of the present `node`
                for child in node.children:
                    if child.char == char:
                        # We found the char existing in the child.
                        char_not_found = False
                        # Assign node as the child containing the char and break
                        node = child
                        break
                # Return False anyway when we did not find a char.
                if char_not_found:
                    return False
            # Well, we are here means we have found the prefix. Return true to indicate that
            # And also the counter of the last node. This indicates how many words have this
            # prefix
            return True
        return _contains()
