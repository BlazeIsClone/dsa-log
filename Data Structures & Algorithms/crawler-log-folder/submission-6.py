class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cwd = []
        
        for log in logs:
            if log == '../':
                if len(cwd):
                    cwd.pop()
            elif log != './':
                cwd.append(log)
                
        return len(cwd)
        