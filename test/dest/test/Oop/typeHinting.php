<?php
/****/
//如下面的类
class MyClass { 
    
    /**
     * 测试函数
     * 第一个参数必须为 OtherClass 类的一个对象
    **/
    public function test(OtherClass $otherclass) { 
        echo $otherclass->var; 
    }
    
    
    
    /**
     * 另一个测试函数
     * 第一个参数必须为数组 
    **/
    public function test_array(array $input_array) { 
        print_r($input_array); 
    }
    
    
    
    /**
     * 第一个参数必须为递归类型
    **/
    public function test_interface(Traversable $iterator) { 
        echo get_class($iterator); 
    }
    
    
    /**
     * 第一个参数必须为回调类型
    **/
    public function test_callable(callable $callback, $data) { 
        call_user_func($callback, $data); 
    }
}



// OtherClass 类定义
class OtherClass { 
    public $var = 'Hello World'; 
}



/****/

// 两个类的对象
$myclass = new MyClass(); 
$otherclass = new OtherClass(); 

// 致命错误：第一个参数必须是 OtherClass 类的一个对象
$myclass->test('hello'); 

// 致命错误：第一个参数必须为 OtherClass 类的一个实例
$foo = new stdClass(); 
$myclass->test($foo); 

// 致命错误：第一个参数不能为 null
$myclass->test(null); 

// 正确：输出 Hello World 
$myclass->test($otherclass); 

// 致命错误：第一个参数必须为数组
$myclass->test_array('a string'); 

// 正确：输出数组
$myclass->test_array(array('a', 'b', 'c')); 

// 正确：输出 ArrayObject
$myclass->test_interface(new ArrayObject(array())); 

// 正确：输出 int(1)
$myclass->test_callable('var_dump', 1); 

/****/
// 如下面的类
class MyClass { 
    public $var = 'Hello World'; 
}


/**
 * 测试函数
 * 第一个参数必须是 MyClass 类的一个对象
**/
function MyFunction(MyClass $foo) { 
    echo $foo->var; 
}


// 正确
$myclass = new MyClass(); 
MyFunction($myclass); 

/****/

/** 接受 NULL 值 **/
function test(stdClass $obj = null) { 
}



test(null); 
test(new stdClass()); 


