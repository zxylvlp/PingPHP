<?php
// Pre PHP 7 code
class Logger { 
    public function log($msg) { 
        echo $msg; 
    }
}

$util->setLogger(new Logger()); 

// PHP 7+ code
$util->setLogger(); 

/****/

class SomeClass { 
}
interface SomeInterface { 
}
trait SomeTrait { 
}

var_dump(); 

/****/

class Outer { 
    private $prop = 1; 
    protected $prop2 = 2; 
    
    protected function func1() { 
        return 3; 
    }
    
    public function func2() { 
        return (); 
    }
}

echo (new Outer())->func2()->func3(); 
