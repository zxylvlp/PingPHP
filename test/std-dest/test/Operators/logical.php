<?php
// --------------------
// foo() 根本没机会被调用，被运算符“短路”了

$c = (false && foo()); 
$d = (true || foo()); 

// --------------------
// "||" 比 "or" 的优先级高

// 表达式 (false || true) 的结果被赋给 $e
// 等同于：($e = (false || true))
$e = false || true; 

// 常量 false 被赋给 $f，true 被忽略
// 等同于：(($f = false) or true)
$f = false || true; 

var_dump($e, $f); 

// --------------------
// "&&" 比 "and" 的优先级高

// 表达式 (true && false) 的结果被赋给 $g
// 等同于：($g = (true && false))
$g = true && false; 

// 常量 true 被赋给 $h，false 被忽略
// 等同于：(($h = true) and false)
$h = true && false; 

var_dump($g, $h); 
