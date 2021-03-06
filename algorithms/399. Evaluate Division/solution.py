class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # @StefanPochmann
        g = collections.defaultdict(dict)
        for (p, q), v in zip(equations, values):
            g[p][p] = g[q][q] = 1.0
            g[p][q] = v
            g[q][p] = 1 / v
        for i, j, k in itertools.permutations(g, 3):
            if k in g[i] and j in g[k]:
                g[i][j] = g[i][k] * g[k][j]
        return [g[p].get(q, -1.0) for p, q in queries]
