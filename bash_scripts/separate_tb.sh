#!/bin/bash

counter=1
for f in event*
do
    mkdir tb_$counter
    mv $f tb_$counter
    ((counter++))
done