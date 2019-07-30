#!/bin/bash
for (( c=1; c<=5; c++ ))
do  
   echo "Running apmtest01.py for $c times..."
   python apmtest01.py testing
   echo "The program has been completed."
done