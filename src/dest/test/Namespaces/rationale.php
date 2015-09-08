<?php
namespace my\name; // 参考 "定义命名空间" 小节

class MyClass { 
}

function myfunction() { 
}

const MYCONST = 1; 

$a = new MyClass(); 
$c = new \my\name\MyClass(); // 参考 "全局空间" 小节

$a = strlen('hi'); // 参考 "使用命名空间：后备全局函数/常量" 小节

$d = namespace\MYCONST; // 参考 "namespace操作符和__NAMESPACE__常量” 小节

$m = a\B; 
$d = join('', [__NAMESPACE__, '\MYCONST']); 
echo (constant($d)); // 参考 "命名空间和动态语言特征" 小节
