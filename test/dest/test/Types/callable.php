<?php
// An example callback function
function my_callback_function() { 
    echo 'hello world!'; 
}

// An example callback method
class MyClass { 
    static function myCallbackMethod() { 
        echo 'Hello World!'; 
    }
}

// Type 1: Simple callback
call_user_func('my_callback_function'); 

// Type 2: Static class method call
call_user_func(array('MyClass', 'myCallbackMethod')); 

// Type 3: Object method call
$obj = new MyClass(); 
call_user_func(array($obj, 'myCallbackMethod')); 

// Type 4: Static class method call (As of PHP 5.2.3)
call_user_func('MyClass::myCallbackMethod'); 

// Type 5: Relative static class method call (As of PHP 5.3.0)
class A { 
    public static function who() { 
        echo "A\n"; 
    }
}

class B extends A { 
    public static function who() { 
        echo "B\n"; 
    }
}

call_user_func(array('B', 'parent::who')); // A

/****/

// Our closure
$double = (function ($a) { 
    return $a * 2; 
}); 

// This is our range of numbers
$numbers = range(1, 5); 

// Use the closure as a callback here to 
// double the size of each element in our 
// range
$new_numbers = array_map($double, $numbers); 

print implode(' ', $new_numbers); 
