$ErrorActionPreference = 'Stop'

g++ -Wall -Wextra --std=c++17 main.cpp -o main.exe

Get-Content data/data1.txt | .\main.exe > result1.txt
Get-Content data/data2.txt | .\main.exe > result2.txt
Get-Content data/data3.txt | .\main.exe > result3.txt
Get-Content data/data4.txt | .\main.exe > result4.txt
