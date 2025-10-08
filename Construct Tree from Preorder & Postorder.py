class Solution:
    def constructTree(self, pre, post):
        post_index = {val: idx for idx, val in enumerate(post)}
        self.preIndex = 0
      
        def build(postStart, postEnd):
            if self.preIndex >= len(pre) or postStart > postEnd:
                return None

            root = Node(pre[self.preIndex])
            self.preIndex += 1

            if postStart == postEnd or self.preIndex >= len(pre):
                return root

            next_val = pre[self.preIndex]
            leftRootIndex = post_index[next_val]
            root.left = build(postStart, leftRootIndex)
            root.right = build(leftRootIndex + 1, postEnd - 1)
            return root
          
        return build(0, len(post) - 1)
