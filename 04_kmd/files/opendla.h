#ifndef __OPENDLA_H_
    #define __OPENDLA_H_
    #define DLA_2_CONFIG

    #ifdef DLA_2_CONFIG
        #include <opendla_small.h>
    #else
        #include <opendla_initial.h>
    #endif

#endif

#ifndef DLA_SMALL_CONFIG
    #define DLA_SMALL_CONFIG  
#endif