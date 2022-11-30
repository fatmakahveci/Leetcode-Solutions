class FileSystem:

    from collections import defaultdict # avoiding key error

    def __init__(self):
        self.paths = defaultdict(list) # { "/a/b": [files, dirs] }
        self.files = defaultdict(str) # { file_name : content }

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split('/')[-1]]
        return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split('/')
        for i in range(1, len(directories)): # avoids the first ""
            curr_dir = "/".join(directories[:i]) or "/"

            if curr_dir not in self.paths or directories[i] not in self.paths[curr_dir]:
                bisect.insort(self.paths[curr_dir], directories[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
