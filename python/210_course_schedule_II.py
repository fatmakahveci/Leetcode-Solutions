class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { course: [] for course in range(numCourses) }
        
        for (course, pre) in prerequisites:
            pre_map[course].append(pre)
        
        output = []
        visited, cycle = set(), set()

        def dfs(course):

            if course in visited:
                return True
            
            if course in cycle:
                return False
            
            cycle.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)

            visited.add(course)
            output.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output
