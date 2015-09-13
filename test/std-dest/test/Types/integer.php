<?php
$a = 1234; // 十进制数
$a = -123; // 负数
$a = 0123; // 八进制数 (等于十进制 83)
$a = 0x1A; // 十六进制数 (等于十进制 26)

/****/

var_dump(01070); // 八进制 010 = 十进制 8

/****/

$large_number = 2147483647; 
var_dump($large_number); // int(2147483647)

$large_number = 2147483648; 
var_dump($large_number); // float(2147483648)

$million = 1000000; 
$large_number = 50000 * $million; 
var_dump($large_number); // float(50000000000)

/****/

$large_number = 9223372036854775807; 
var_dump($large_number); // int(9223372036854775807)

$large_number = 9223372036854775808; 
var_dump($large_number); // float(9.2233720368548E+18)

$million = 1000000; 
$large_number = 50000000000000 * $million; 
var_dump($large_number); // float(5.0E+19)

/****/

var_dump(25 / 7); // float(3.5714285714286) 
var_dump((int)(25 / 7)); // int(3)
var_dump(round(25 / 7)); // float(4) 

/****/

echo (int)((0.1 + 0.7) * 10); // 显示 7!

