AddTimer (TimeoutValue,  ApplicationModuleId, Param1, Param2….)
{
   Allocate a timer block and fill in the fields with
      the  task id, and parameters;
   Determine the granularity of the timer from the timeout value
   specified and access the array entry corresponding to the
   granularity (1 ms, 10 ms, 1 sec and 10 secs);
   Add the timer block to the list in the array entry
     using the differential timeout approach;
}

ProcessTick ( )
{
    Decrement the counts in all the array entries;
    If count reaches zero, decrement the count field in the
       first timer block of the list for the array entry;
    If  the decremented timer count reaches zero {
         Delete the block(s) from the timer list and
           indicate the timeout with the parameters
           from the timer block to the task which started the timer;
          Return the timer block to the timer block free list;
    }
}