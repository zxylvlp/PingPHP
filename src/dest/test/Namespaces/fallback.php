<?php
namespace A\B\C; 
class Exception extends \Exception { 
}

$a = new Exception('hi'); // $a 是类 A\B\C\Exception 的一个对象
$b = new \Exception('hi'); // $b 是类 Exception 的一个对象

$c = new ArrayObject(); // 致命错误, 找不到 A\B\C\ArrayObject 类

/****/

namespace A\B\C; 

const E_ERROR = 45; 
function strlen($str) { 
    return \strlen($str) - 1; 
}

echo E_ERROR, "\n"; // 输出 "45"
echo INI_ALL, "\n"; // 输出 "7" - 使用全局常量 INI_ALL

echo strlen('hi'), "\n"; // 输出 "1"
if (is_array('hi')) { // 输出 "is not array"
    echo "is array\n"; 
} else { 
    echo "is not array\n"; 
}
