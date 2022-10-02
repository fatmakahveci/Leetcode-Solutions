class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        hardest_job_remaining = [0] * len(jobDifficulty)
        hardest_job = 0
        for i in range(len(jobDifficulty) - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return hardest_job_remaining[i]

            best = float("inf")
            hardest = 0
            for j in range(i, len(jobDifficulty) - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1))
            return best

        return dp(0, 1)
