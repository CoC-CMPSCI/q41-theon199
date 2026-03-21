#!/bin/sh
g++ -Wall -Wextra --std=c++17 main.cpp -o main
./main < data/data1.txt > result1.txt
./main < data/data2.txt > result2.txt
./main < data/data3.txt > result3.txt
./main < data/data4.txt > result4.txt
