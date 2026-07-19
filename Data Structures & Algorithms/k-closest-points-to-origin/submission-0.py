class Solution:

    def d_sqrt(self, point):
        x, y = point
        d_sqrt = x * x + y * y
        return d_sqrt

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        distance = [self.d_sqrt(point) for point in points]
        distance = dict(zip(range(len(points)), distance))
        distance = sorted(distance.items(), key=lambda x: x[1], reverse=False)
        indices = [d[0] for d in distance]
        indices = indices[:k]
        for ix in indices:
            output.append(points[ix])
        return output 