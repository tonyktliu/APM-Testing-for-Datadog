#!/bin/bash
for (( c=1; c<=2; c++ ))
do  
   echo "Running apmtest01.py for $c times..."
   python apmtest.py testing
   echo "The program has been completed."
done
