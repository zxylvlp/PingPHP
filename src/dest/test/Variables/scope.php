<?php
$a = 1; 
include 'b.inc'; 

/****/

$a = 1; // global scope 

function Test() { 
    echo $a; // reference to local scope variable
}

Test(); 

/****/

$a = 1; 
$b = 2; 

function Sum() { 
    global $a, $b; 
    
    $b = $a + $b; 
}

Sum(); 
echo $b; 

/****/

$a = 1; 
$b = 2; 

function Sum() { 
    $GLOBALS['b'] = $GLOBALS['a'] + $GLOBALS['b']; 
}

Sum(); 
echo $b; 

/****/

function test_global() { 
    // 大多数的预定义变量并不 "super"，它们需要用 'global' 关键字来使它们在函数的本地区域中有效。
    global $HTTP_POST_VARS; 
    
    echo $HTTP_POST_VARS['name']; 
    
    // Superglobals 在任何范围内都有效，它们并不需要 'global' 声明。Superglobals 是在 PHP 4.1.0 引入的。
    echo $_POST['name']; 
}

/****/

function Test() { 
    $a = 0; 
    echo $a; 
    $a++; 
}

/****/

function test() { 
    static $a = 0; 
    echo $a; 
    $a++; 
}

/****/

function test() { 
    static $count = 0; 
    
    $count++; 
    echo $count; 
    if ($count < 10) { 
        test(); 
    }
    $count--; 
}

/****/

function foo() { 
    static $int_ = 0; // correct
    static $int_ = 1 + 2; // wrong  (as it is an expression)
    static $int_ = sqrt(121); // wrong  (as it is an expression too)
    
    $int_++; 
    echo $int_; 
}

/****/

function test_global_ref() { 
    global $obj; 
    $obj = &new stdclass(); 
}

function test_global_noref() { 
    global $obj; 
    $obj = new stdclass(); 
}

test_global_ref(); 
var_dump($obj); 
test_global_noref(); 
var_dump($obj); 

/****/

function &get_instance_ref() { 
    static $obj; 
    
    echo 'Static object: '; 
    var_dump($obj); 
    if (!isset($obj)) { 
        // 将一个引用赋值给静态变量
        $obj = &new stdclass(); 
    }
    $obj->property++; 
    return $obj; 
}

function &get_instance_noref() { 
    static $obj; 
    
    echo 'Static object: '; 
    var_dump($obj); 
    if (!isset($obj)) { 
        // 将一个对象赋值给静态变量
        $obj = new stdclass(); 
    }
    $obj->property++; 
    return $obj; 
}

$obj1 = get_instance_ref(); 
$still_obj1 = get_instance_ref(); 
echo "\n"; 
$obj2 = get_instance_noref(); 
$still_obj2 = get_instance_noref(); 

