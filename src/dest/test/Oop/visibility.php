<?php
/**
 * Define MyClass
**/
class MyClass { 
    public $public_ = 'Public'; 
    protected $protected_ = 'Protected'; 
    private $private_ = 'Private'; 
    
    public function printHello() { 
        echo ($this->public_); 
        echo ($this->protected_); 
        echo ($this->private_); 
    }
}

$obj = new MyClass(); 
echo ($obj->public_); // 这行能被正常执行
echo ($obj->protected_); // 这行会产生一个致命错误
echo ($obj->private_); // 这行也会产生一个致命错误
$obj->printHello(); // 输出 Public、Protected 和 Private


/**
 * Define MyClass2
**/
class MyClass2 extends MyClass { 
    // 可以对 public 和 protected 进行重定义，但 private 而不能
    protected $protected_ = 'Protected2'; 
    
    public function printHello() { 
        echo ($this->public_); 
        echo ($this->protected_); 
        echo ($this->private_); 
    }
}

$obj2 = new MyClass2(); 
echo ($obj2->public_); // 这行能被正常执行
echo ($obj2->private_); // 未定义 private
echo ($obj2->protected_); // 这行会产生一个致命错误
$obj2->printHello(); // 输出 Public、Protected2 和 Undefined

/****/

/**
 * Define MyClass
**/
class MyClass { 
    // 声明一个公有的构造函数
    public function __construct() { 
    }
    
    // 声明一个公有的方法
    public function MyPublic() { 
    }
    
    // 声明一个受保护的方法
    protected function MyProtected() { 
    }
    
    // 声明一个私有的方法
    private function MyPrivate() { 
    }
    
    // 此方法为公有
    public function Foo() { 
        $this->MyPublic(); 
        $this->MyProtected(); 
        $this->MyPrivate(); 
    }
}

$myclass = new MyClass(); 
$myclass->MyPublic(); // 这行能被正常执行
$myclass->MyProtected(); // 这行会产生一个致命错误
$myclass->MyPrivate(); // 这行会产生一个致命错误
$myclass->Foo(); // 公有，受保护，私有都可以执行


/**
 * Define MyClass2
**/
class MyClass2 extends MyClass { 
    // 此方法为公有
    public function Foo2() { 
        $this->MyPublic(); 
        $this->MyProtected(); 
        $this->MyPrivate(); // 这行会产生一个致命错误
    }
}

$myclass2 = new MyClass2(); 
$myclass2->MyPublic(); // 这行能被正常执行
$myclass2->Foo2(); // 公有的和受保护的都可执行，但私有的不行

class Bar { 
    public function test() { 
        $this->testPrivate(); 
        $this->testPublic(); 
    }
    
    public function testPublic() { 
        echo ("Bar::testPublic\n"); 
    }
    
    private function testPrivate() { 
        echo ("Bar::testPrivate\n"); 
    }
}

class Foo extends Bar { 
    public function testPublic() { 
        echo ("Foo::testPublic\n"); 
    }
    
    private function testPrivate() { 
        echo ("Foo::testPrivate\n"); 
    }
}

$myFoo = new foo(); 
$myFoo->test(); // Bar::testPrivate 
// Foo::testPublic

/****/

class Test { 
    private $foo; 
    
    public function __construct($foo) { 
        $this->foo = $foo; 
    }
    
    private function bar() { 
        echo ('Accessed the private method.'); 
    }
    
    public function baz(Test $other) { 
        // We can change the private property:
        $other->foo = 'hello'; 
        var_dump($other->foo); 
        
        // We can also call the private method:
        $other->bar(); 
    }
}

$test = new Test('test'); 

$test->baz(new Test('other')); 
