class Codec:

    def serialize(self, root):
        if not root:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"


    def deserialize(self, data: str):
        if not data:
            return None
        
        def deserialize_list(nums: List[str]):
            val = nums.pop(0)
            if not val:
                return None

            print(val)
            root = TreeNode(val)
            root.left = deserialize_list(nums)
            root.right = deserialize_list(nums)

            return root
    
        return deserialize_list(data.split(","))


   
