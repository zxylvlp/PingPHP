<?php
// Pre PHP 7 code
class Logger { 
    public function log($msg) { 
        echo $msg; 
    }
}

$util->setLogger(new Logger()); 

// PHP 7+ code
$util->setLogger(new class () { 
    public function log($msg) { 
        echo $msg; 
    }
}); 

/****/

class SomeClass { 
}
interface SomeInterface { 
}
trait SomeTrait { 
}

var_dump(new class (10) extends SomeClass implements SomeInterface { 
    private $num; 
    public function __construct($num) { 
        $this->num = $num; 
    }
    use SomeTrait; 
}); 

/****/

class Outer { 
    private $prop = 1; 
    protected $prop2 = 2; 
    
    protected function func1() { 
        return 3; 
    }
    
    public function func2() { 
        return (new class ($this->prop) extends Outer { 
            private $prop3; 
            
            public function __construct($prop) { 
                $this->prop3 = $prop; 
            }
            
            public function func3() { 
                return $this->prop2 + $this->prop3 + $this->func1(); 
            }
        }); 
    }
}

echo (new Outer())->func2()->func3(); 
