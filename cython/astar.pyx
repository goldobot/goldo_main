# distutils: language = c++
from libcpp.list cimport list
from libcpp.pair cimport pair
from libcpp cimport bool

from AStar cimport AStar, AStarPathType

cdef class AStarWrapper:
    cdef AStar* c_astar
    
    def __cinit__(self):
        self.c_astar = new AStar()
        self.c_astar[0].setMatrix(200,300)
        
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
        
    