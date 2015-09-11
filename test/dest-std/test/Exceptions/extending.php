<?php
/**
自定义一个异常处理类
**/
class MyException extends Exception { 
    // 重定义构造器使 message 变为必须被指定的属性
    public function __construct($message, $code = 0, $previous = null) { 
        // 自定义的代码
        
        // 确保所有变量都被正确赋值
        parent::__construct($message, $code, $previous); 
    }
    
    // 自定义字符串输出的样式
    public function __toString() { 
        return implode(__CLASS__, "{}: [{$this->code}]: {$this->message}\n"); 
    }
    
    public function customFunction() { 
        echo "A custom function for this type of exception\n"; 
    }
}


/**
创建一个用于测试异常处理机制的类
**/
class TestException { 
    
    public $var; 
    
    const THROW_NONE = 0; 
    const THROW_CUSTOM = 1; 
    const THROW_DEFAULT = 2; 
    
    function __construct($avalue = self::THROW_NONE) { 
        
        switch ($avalue) { 
            case self::THROW_CUSTOM: 
                // 抛出自定义异常
                throw new MyException('1 is an invalid parameter', 5); 
                break; 
            case self::THROW_DEFAULT: 
                // 抛出默认的异常
                throw new Exception('2 is not allowed as a parameter', 6); 
                break; 
            default: 
                // 没有异常的情况下，创建一个对象
                $this->var = $avalue; 
        }
    }
}


// 例子 1
try { 
    $o = new TestException(TestException::THROW_CUSTOM); 
} catch (MyException $e) { // 捕获异常
    echo "Caught my exception\n", $e; 
    $e->customFunction(); 
} catch (Exception $e) { // 被忽略
    echo "Caught Default Exception\n", $e; 
} 

// Continue execution
var_dump($o); // Null
echo ("\n\n"); 


// 例子 2
try { 
    $o = new TestException(TestException::THROW_DEFAULT); 
} catch (MyException $e) { //  不能匹配异常的种类，被忽略
    
    echo "Caught my exception\n", $e; 
    $e->customFunction(); 
} catch (Exception $e) { // 捕获异常
    echo "Caught Default Exception\n", $e; 
} 

// 执行后续代码
var_dump($o); // Null
echo ("\n\n"); 


// 例子 3
try { 
    $o = new TestException(TestException::THROW_CUSTOM); 
} catch (Exception $e) { // 捕获异常
    echo "Default Exception caught\n", $e; 
} 

// 执行后续代码
var_dump($o); // Null
echo ("\n\n"); 


// 例子 4
try { 
    $o = new TestException(); 
} catch (Exception $e) { // 没有异常，被忽略
    echo "Default Exception caught\n", $e; 
} 

// 执行后续代码
var_dump($o); // TestException
echo ("\n\n"); 
