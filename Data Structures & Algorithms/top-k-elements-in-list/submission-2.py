class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for number in nums:
            if number in hash_map:
                hash_map[number] += 1
            else:
                hash_map[number] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in hash_map.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        