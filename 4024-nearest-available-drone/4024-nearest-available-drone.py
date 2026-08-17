class Solution:
    def nearestDrone(self, drones: List[List[int]], target: List[int]) -> int:
        l = []

        for index, i in enumerate(drones):
            distance = abs(i[0] - target[0]) + abs(i[1] - target[1])

            if distance <= i[2]:
                l.append((distance, index))

        return min(l)[1] if l else -1