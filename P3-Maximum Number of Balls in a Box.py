class Solution:
    def countBalls(self, lowLimit, highLimit):
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(num))
            boxes[s] = boxes.get(s, 0) + 1

        return max(boxes.values())