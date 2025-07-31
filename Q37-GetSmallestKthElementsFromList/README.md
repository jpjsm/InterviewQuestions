# Get the Smallest K Elements from unsorted list of length N

Given a collection of n two dimensional points and a number k, return the k closest points to (0,0) by Euclidean distance.

```txt
    *                         |                              
                              |                            * 
                              |                              
                          *   |                  *           
                              |                              
                              |                              
        *                     |         *                    
                              |                              
                        *     |            *                 
                              |                              
-*----------------------------o------------------------------
                              |                              
              *               |                   *          
                    *         |                              
                              |                         *    
                              |              *               
                        *     |                              
                              |     *                        
                              |                              
                              |             *                
    *                         |                     *        

```

Euclid distance to the origin is: $\sqrt(x^2 + y^2)$

> ***Note***: Assume $n >> k$
