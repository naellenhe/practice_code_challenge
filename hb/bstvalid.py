"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False

        4
     2     6
      3   5 7
       1
    >>> t = Node(4,
    ...       Node(2, None, Node(3, None, Node(1))),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        def as_list(node):
            if (not node.left) and (not node.right):
                lst = [node.data]
                return lst

            left = as_list(node.left) if node.left else []
            right = as_list(node.right) if node.right else []

            lst = left + [node.data] + right
            return lst

        lst = as_list(self)
        return sorted(lst) == lst

    # def __iter__(self):
    #     """Iterate over nodes in BST in proper order.

    #     The __iter__ method is called when you iterate
    #     over an object. It should yield successive
    #     values (for information on yielding, learn about
    #     "generators").

    #     Our BST can be iterated over to get the values
    #     in order. For example, for this tree::

    #             4
    #          2     6
    #         1 3   5 7

    #     We can loop over it::

    #         >>> t = Node(4,
    #         ...       Node(2, Node(1), Node(3)),
    #         ...       Node(6, Node(5), Node(7))
    #         ... )

    #         >>> for n in t:
    #         ...     print n.data,
    #         1 2 3 4 5 6 7

    #     This method of navigating a BST by left-recurse, self,
    #     right-recurse, is often called "in-order traversal".
    #     """

    #     # walk the left descendants recursively:
    #     for n in self.left or []:
    #         yield n

    #     # hand back this node
    #     yield self

    #     # walk the right descendants recursively:
    #     for n in self.right or []:
    #         yield n

    # def is_valid(self):
    #     lst = [n.data for n in self]
    #     return sorted(lst) == lst



if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"
