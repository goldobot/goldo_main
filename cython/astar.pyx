# distutils: language = c++
# cython: language_level=3

from libcpp.list cimport list
from libcpp.pair cimport pair
from libcpp cimport bool
from cpython.bytes cimport PyBytes_FromStringAndSize



from AStar cimport AStar, AStarPathType

cdef (float, float) Point

cdef class AStarWrapper:
    cdef AStar* c_astar
    cdef char c_arr[200 * 300]
    
    def __cinit__(self):
        self.c_astar = new AStar()
        self.c_astar[0].setMatrix(200,300)
        
    def setSquare(self, p, r):
        cdef float xf = 100.0*p[0]
        cdef float yf = 100.0*p[1]
        cdef int x0 = xf - r
        cdef int y0 = yf + 149 - r
        cdef int x1 = xf + r
        cdef int y1 = yf + 149 + r
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
        for x in range(x0, x1):
            for y in range(y0, y1):
                self.setWall(x, y)
        
    def setDisk(self, p, r):
        cdef float xf = 100.0*p[0]
        cdef float yf = 100.0*p[1]
        cdef int x0 = xf - r
        cdef int y0 = yf + 149 - r
        cdef int x1 = xf + r
        cdef int y1 = yf + 149 + r
        cdef int wtf = 0
        cdef int xC = x0 + r
        cdef int yC = y0 + r
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
        for x in range(x0, x1):
            for y in range(y0, y1):
                dx = x-xC
                dy = y-yC
                if ((dx*dx+dy*dy)<r*r):
                    self.setWall(x, y)


    def fillRect(self, int x1, int y1, int x2, int y2):
        cdef int x, y
        if x1 < 0:
            x1 = 0
        if x2 > 199:
            x2 = 199
        if y1 < 0:
            y1 = 0
        if y2 > 299:
            y2 = 299
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.setWall(x, y)
                
    def clearRect(self, int x1, int y1, int x2, int y2):
        cdef int x, y
        if x1 < 0:
            x1 = 0
        if x2 > 199:
            x2 = 199
        if y1 < 0:
            y1 = 0
        if y2 > 299:
            y2 = 299
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.setWay(x, y)
        
    def getArr(self):
        return PyBytes_FromStringAndSize(self.c_arr, 200 * 300)
        
    cdef setWall(self, unsigned x, unsigned y):
        self.c_astar[0].setWall(x, y)
        self.c_arr[y + x * 300] = 128
        
    cdef setWay(self, unsigned x, unsigned y):
        self.c_astar[0].setWay(x, y, 1)
        self.c_arr[y + x * 300] = 255
        
        
    def resetCosts(self):
        cdef int x, y
        cdef int i, j
        
        for x in range(200):
            for y in range(300):
                self.setWay(x, y)
                
        for x in range(200):
            for j in range(15):
                self.setWall(x,j)
                self.setWall(x,299 - j)
                
        for y in range(300):
            for i in range(15):
                self.setWall(i,y)
                self.setWall(199 - i,y)
                
        # rochers
        for i in range(25):
            for j in range(15):
                self.setWall(i, 150 - j)
                self.setWall(i, 150 + j)
        
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
        
    