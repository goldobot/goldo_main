# distutils: language = c++
# cython: language_level=3

from libcpp.list cimport list
from libcpp.pair cimport pair
from libcpp cimport bool

from AStar cimport AStar, AStarPathType

cdef (float, float) Point

cdef class AStarWrapper:
    cdef AStar* c_astar
    
    def __cinit__(self):
        self.c_astar = new AStar()
        self.c_astar[0].setMatrix(200,300)
        
    def setSquare(self, p, r):
        cdef int x0 = p[0] * 100 - r
        cdef int y0 = p[1] * 100 + 149 - r
        cdef int x1 = p[0] * 100 + r
        cdef int y1 = p[1] * 100 + 149 + r
        if x0 < 0:
            x0 = 0
        if x1 < 0:
            x1 = 0
        if x0 > 199:
            x0 = 199
        if x1 > 199:
            x1 = 199
        if y0 < 0:
            y0 = 0
        if y1 < 0:
            y1 = 0
        if y0 > 299:
            y0 = 299
        if y1 > 299:
            y1 = 299
        for i in range(x0, y0):
            for j in range(y0, y1):
                self.c_astar[0].setWall(i, j)
        
    def unsetSquare(self, x, y, r):
        pass
        
    def setWall(self, x, y):
        self.c_astar[0].setWall(x, y)
       
    def resetCosts(self):
        for x in range(200):
            for y in range(300):
                self.c_astar[0].setWay(x, y, 1)
        for i in range(200):
            for j in range(15):
                self.setWall(i,j)
                self.setWall(i,299 - j)
            
        for i in range(300):
            for j in range(15):
                self.setWall(j,i)
                self.setWall(199 - j,i)
                
        #recifs
        for i in range(30):
            for j in range(15):
                self.setWall(199 - i, 150 - 60 - j)
                self.setWall(199 - i, 150 - 60 + j)
                self.setWall(199 - i, 150 + 60 - j)
                self.setWall(199 - i, 150 + 60 + j)
        for i in range(45):
            for j in range(15):
                self.setWall(199 - i, 150 - j)
                self.setWall(199 - i, 150 + j)
        
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
        
            
        path = self.c_astar[0].getPathOnlyIfNeed(True, &is_new_path, path_type)
        ret = []
        for p in path:
            ret.append((p.first * 0.01, (<int>(p.second) - 149) * 0.01))
        return ret
        
    