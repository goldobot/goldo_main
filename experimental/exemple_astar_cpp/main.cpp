/*
 *  GoldobotStrat2020
 *
 *  Copyright (c) 2020 Goldorak team
 *
 */
/*
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#ifdef WIN32
#include <windows.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#ifndef WIN32
#include <sys/socket.h>
#include <netinet/in.h>
#endif
#include <unistd.h>

#include <pthread.h>

#include <signal.h>

#include "astar.hpp"
#include "astar_wrapper.hpp"

using namespace goldobot;

int x_start_mm = 1740;
int y_start_mm =  290;
int x_end_mm   = 1850;
int y_end_mm   =-1350;
int xo1_mm     =  400;
int yo1_mm     =-1000;
int xo2_mm     = 1600;
int yo2_mm     = -300;
int xo3_mm     =  200;
int yo3_mm     =  650;

int process_command_line(int argc, const char * argv[]);

int main(int argc, const char * argv[]) 
{
  if (process_command_line(argc, argv)!=0)
  {
    fprintf(stderr, "ERROR : wrong command line arguments.\n");
    return -1;
  }

  if (AstarWrapper::instance().init()!=0)
  {
    fprintf(stderr, "ERROR : cannot init AstarWrapper.\n");
    return -1;
  }

  char dbg_fname[128];
  printf(" ASTAR TEST\n");
  strncpy(dbg_fname,"astar_test.ppm",sizeof(dbg_fname));
  AstarWrapper::instance().dbg_astar_test(x_start_mm, y_start_mm,
                                          x_end_mm  , y_end_mm  ,
                                          xo1_mm    , yo1_mm    ,
                                          xo2_mm    , yo2_mm    ,
                                          xo3_mm    , yo3_mm    ,
                                          dbg_fname);

  return 0;
}

int process_command_line(int argc, const char * argv[]) 
{

  // detect autotest request
  if (argc==1)
  {
    return 0;
  }
  else if (argc==11)
  {
    x_start_mm = atoi(argv[1]);
    y_start_mm = atoi(argv[2]);
    x_end_mm   = atoi(argv[3]);
    y_end_mm   = atoi(argv[4]);
    xo1_mm     = atoi(argv[5]);
    yo1_mm     = atoi(argv[6]);
    xo2_mm     = atoi(argv[7]);
    yo2_mm     = atoi(argv[8]);
    xo3_mm     = atoi(argv[9]);
    yo3_mm     = atoi(argv[10]);
    return 0;
  }

  return -1;
}

