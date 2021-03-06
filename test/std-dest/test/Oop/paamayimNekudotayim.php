<?php
class MyClass { 
    const CONST_VALUE = 'A constant value'; 
}

$classname = 'MyClass'; 
echo ($classname::CONST_VALUE); // 自 PHP 5.3.0 起

echo (MyClass::CONST_VALUE); 

/****/

class OtherClass extends MyClass { 
    public static $my_static = 'static var'; 
    
    public static function doubleColon() { 
        echo parent::CONST_VALUE, "\n"; 
        echo self::$my_static, "\n"; 
    }
}

$classname = 'OtherClass'; 
echo ($classname::doubleColon()); // 自 PHP 5.3.0 起

OtherClass::doubleColon(); 

/****/

class MyClass { 
    protected function myFunc() { 
        echo ("MyClass::myFunc()\n"); 
    }
}

class OtherClass extends MyClass { 
    // 覆盖了父类的定义
    public function myFunc() { 
        // 但还是可以调用父类中被覆盖的方法
        parent::myFunc(); 
        echo ("OtherClass::myFunc()\n"); 
    }
}

$class_ = new OtherClass(); 
$class_->myFunc(); 
