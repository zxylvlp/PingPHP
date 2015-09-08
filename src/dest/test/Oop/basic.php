<?php
class SimpleClass { 
    // property declaration
    public $var = 'a default value'; 
    
    // method declaration
    public function displayVar() { 
        echo ($this->var); 
    }
}

/****/

class A { 
    public function foo() { 
        if (isset($this)) { 
            echo ('this is defined ('); 
            echo (get_class($this)); 
            echo (")\n"); 
        } else { 
            echo ("\this is not defined.\n"); 
        }
    }
}

class B { 
    public function bar() { 
        // Note: the next line will issue a warning if E_STRICT is enabled.
        A::foo(); 
    }
}

$a = new A(); 
$a->foo(); 

// Note: the next line will issue a warning if E_STRICT is enabled.
A::foo(); 
$b = new B(); 
$b->bar(); 

// Note: the next line will issue a warning if E_STRICT is enabled.
B::bar(); 

/****/

$instance = new SimpleClass(); 

// 也可以这样做：
$className = 'Foo'; 
$instance = new $className(); // Foo()

/****/


$instance = new SimpleClass(); 

$assigned = $instance; 
$reference = &$instance; 

$instance->var = 'assigned will have this value'; 

$instance = null; // instance and $reference become null

var_dump($instance); 
var_dump($reference); 
var_dump($assigned); 

/****/

class Test { 
    public static function getNew() { 
        return new static(); 
    }
}

class Child extends Test { 
}

$obj1 = new Test(); 
$obj2 = new $obj1; 
var_dump($obj1 !== $obj2); 

$obj3 = Test::getNew(); 
var_dump($obj3 instanceof Test); 

$obj4 = Child::getNew(); 
var_dump($obj4 instanceof Child); 

/****/

class ExtendClass extends SimpleClass { 
    // Redefine the parent method
    public function displayVar() { 
        echo ("Extending class\n"); 
        parent::displayVar(); 
    }
}

$extended = new ExtendClass(); 
$extended->displayVar(); 

/****/

namespace NS; 

class ClassName { 
}

echo (ClassName::class); 
