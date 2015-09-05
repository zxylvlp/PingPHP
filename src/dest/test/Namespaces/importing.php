<?php
namespace foo; 
use My\Full\Classname as Another; 

// 下面的例子与 use My\Full\NSname as NSname 相同
use My\Full\NSname; 

// 导入一个全局类
use ArrayObject; 

// importing a function (PHP 5.6+)
use function My\Full\functionName; 

// aliasing a function (PHP 5.6+)
use function My\Full\functionName as func; 

// importing a constant (PHP 5.6+)
use const My\Full\CONSTANT; 

$obj = new namespace\Another(); // 实例化 foo\Another 对象
$obj = new Another(); // 实例化 My\Full\Classname　对象
NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func
$a = new ArrayObject(array(1)); // 实例化 ArrayObject 对象
// 如果不使用 "use \ArrayObject" ，则实例化一个 foo\ArrayObject 对象
func(); // calls function My\Full\functionName
echo CONSTANT; // echoes the value of My\Full\CONSTANT

/****/

use My\Full\Classname as Another, My\Full\NSname; 

$obj = new Another(); // 实例化 My\Full\Classname 对象
NSname\subns\func(); // 调用函数 My\Full\NSname\subns\func

/****/

use My\Full\Classname as Another, My\Full\NSname; 

$obj = new Another(); // 实例化一个 My\Full\Classname 对象
$a = 'Another'; 
$obj = new $a; // 实际化一个 Another 对象

/****/

use My\Full\Classname as Another, My\Full\NSname; 

$obj = new Another(); // instantiates object of class My\Full\Classname
$obj = new \Another(); // instantiates object of class Another
$obj = new Another\thing(); // instantiates object of class My\Full\Classname\thing
$obj = new \Another\thing(); // instantiates object of class Another\thing
