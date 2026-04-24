class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # L: 2
        # R: 2
        # _: 3
        # res = max(L, R) - min(L, R) + _
        d = {'L': 0, 'R': 0, '_': 0}
        for el in moves:
            d[el] += 1

        return max(d['L'], d['R']) - min(d['L'], d['R']) + d['_']
