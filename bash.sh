#!/usr/bin/env bash

read -p "Please input your grade" gd
if [ $gd -ge 90 ] && [ $gd -le 100 ];
then
    echo "Great"
elif [ $gd -ge 70 ] && [ $gd -lt 90 ];
then
    echo "Simple"
else
    echo "Failed"
fi