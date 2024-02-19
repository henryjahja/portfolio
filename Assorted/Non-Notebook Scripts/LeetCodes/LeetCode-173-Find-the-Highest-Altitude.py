#1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        position = 0
        for i in gain:
            position += i
            if highest < position:
                highest = position
        return highest