<?php
function foo(&$var) {
    $var++; 
}

$a = 5; 
foo($a); 
// $a is 6 here

function &bar() {
    $a = 5; 
    return $a; 
}

foo(bar()); 

function bar() {// Note the missing &
    $a = 5; 
    return $a; 
}

foo(bar()); // 自 PHP 5.0.5 起导致致命错误，自 PHP 5.1.1 起导致严格模式错误
//  自 PHP 7.0 起导致 notice 信息
foo($a = 5); // 表达式，不是变量
foo(5); // 导致致命错误

