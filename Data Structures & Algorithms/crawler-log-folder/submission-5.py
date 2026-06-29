class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cwd = []
        
        for i in range(len(logs)):
            if logs[i] == '../':
                if len(cwd):
                    cwd.pop()
            elif logs[i] != './':
                cwd.append(logs[i])
                
        return len(cwd)
        