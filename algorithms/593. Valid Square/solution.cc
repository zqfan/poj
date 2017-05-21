class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        set<int> s({d(p1,p2), d(p1,p3), d(p1,p4), d(p2,p3), d(p2,p4), d(p3,p4)});
        return s.size() == 2 and s.count(0) == 0;
    }

    int d(vector<int> & p, vector<int> & q) {
        return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]);
    }
};
