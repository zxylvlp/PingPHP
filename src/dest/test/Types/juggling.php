<?php
$foo = "0"; // $foo 是字符串 (ASCII 48)
$foo += 2; // $foo 现在是一个整数 (2)
$foo = $foo + 1.3; // $foo 现在是一个浮点数 (3.3)
$foo = 5 + "10 Little Piggies"; // $foo 是整数 (15)
$foo = 5 + "10 Small Pigs"; // $foo 是整数 (15)

/****/

$a = 'car'; // $a is a string
$a[0] = 'b'; // $a is still a string
echo $a; // bar

/****/

$foo = 10; // $foo is an integer
$bar = (bool)$foo; // $bar is a boolean

/****/

$foo = (int)$bar; 
$foo = (int)$bar; 

/****/

$binary = (binary)$string; 
$binary = b"binary string"; 

/****/

$foo = 10; // $foo 是一个整数
$str = "$foo"; // $str 是一个字符串
$fst = (string)$foo; // $fst 也是一个字符串

// 输出 "they are the same"
if ($fst === $str) { 
    echo "they are the same"; 
}
