<?php
function foo() {
    echo "In foo()<br />\n"; 
}

function bar($arg = '') {
    echo "In bar(); argument was '$arg'.<br />\n"; 
}

// 使用 echo 的包装函数
function echoit($string_) {
    echo $string_; 
}

$func = 'foo'; 
$func(); // This calls foo()

$func = 'bar'; 
$func('test'); // This calls bar()

$func = 'echoit'; 
$func('test'); // This calls echoit()

/****/

class Foo {
    public function Variable() {
        $name = 'Bar'; 
        $this->$name(); // This calls the Bar() method
    }
    
    public function Bar() {
        echo "This is Bar"; 
    }
}

$foo = new Foo(); 
$funcname = "Variable"; 
$foo->$funcname(); // This calls $foo->Variable()

/****/

class Foo {
    public static $variable = 'static property'; 
    public static function Variable() {
        echo 'Method Variable called'; 
    }
}

echo Foo::$variable; // This prints 'static property'. It does need a $variable in this scope.
$variable = "Variable"; 
Foo::$variable(); // This calls $foo->Variable() reading $variable in this scope.

