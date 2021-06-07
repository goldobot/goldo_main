# distutils: language = c++
# cython: language_level=3

from libcpp.list cimport list
from libcpp.pair cimport pair
from libcpp cimport bool

from AStar cimport AStar, AStarPathType

cdef (float, float) Point

cdef bool _is_right_side((float, float) p, (float, float) strt, (float, float) end):
    """Determine if a point (p) is `inside` a line segment (strt-->end).
    See : line_crosses, in_out_crosses in npg_helpers.
    position = sign((Bx - Ax) * (Y - Ay) - (By - Ay) * (X - Ax))
    negative for right of clockwise line, positive for left. So in essence,
    the reverse of _is_left_side with the outcomes reversed ;)
    """
    cdef float x = p[0]
    cdef float y = p[1]
    cdef float x0 = strt[0]
    cdef float y0 = strt[1]
    cdef float x1 = end[0]
    cdef float y1 = end[1]
    return (x1 - x0) * (y - y0) - (y1 - y0) * (x - x0)

cdef class AStarWrapper:
    cdef AStar* c_astar
    
    def __cinit__(self):
        self.c_astar = new AStar()
        self.c_astar[0].setMatrix(200,300)
        
    def resetCosts(self):
        for x in range(200):
            for y in range(300):
                self.c_astar[0].setWay(x, y, 1)
        
    def computePath(self, p0, p1):
        cdef unsigned x0 = p0[0] * 100
        cdef unsigned y0 = p0[1] * 100 + 149
        cdef unsigned x1 = p1[0] * 100
        cdef unsigned y1 = p1[1] * 100 + 149
        
        self.c_astar[0].setStart(x0,y0)
        self.c_astar[0].setEnd(x1,y1)
        
        cdef list[pair[unsigned,unsigned]] path
        cdef bool is_new_path
        cdef AStarPathType path_type = AStarPathType.smooth 
        
        for i in range(200):
            self.c_astar[0].setWall(i,0)
            self.c_astar[0].setWall(i,299)
            
        for i in range(200):
            self.c_astar[0].setWall(0,i)
            self.c_astar[0].setWall(199,i)
            
        for i in range(100):
            self.c_astar[0].setWall(i,150)
            
        path = self.c_astar[0].getPathOnlyIfNeed(True, &is_new_path, path_type)
        ret = []
        for p in path:
            ret.append((p.first * 0.01, (<int>(p.second) - 149) * 0.01))
        return ret
        
    