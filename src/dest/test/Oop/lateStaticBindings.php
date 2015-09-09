<?php
class A { 
    public static function who() { 
        echo __CLASS__; 
    }
    
    public static function test() { 
        self::who(); 
    }
}


class B extends A { 
    public static function who() { 
        echo __CLASS__; 
    }
}



B::test(); 

/****/

class A { 
    public static function who() { 
        echo __CLASS__; 
    }
    
    public static function test() { 
        static::who(); // 后期静态绑定从这里开始
    }
}



class B extends A { 
    public static function who() { 
        echo __CLASS__; 
    }
}


B::test(); 


/****/


class A { 
    private function foo() { 
        echo "success!\n"; 
    }
    
    public function test() { 
        $this->foo(); 
        static::foo(); 
    }
}



class B extends A { 
    /**foo() will be copied to B, hence its scope will still be A and
    * the call be successful **/
}


class C extends A { 
    private function foo() { 
        /** original method is replaced the scope of the new one is C **/
    }
}



$b = new B(); 
$b->test(); 
$c = new C(); 
$c->test(); //fails



/****/



class A { 
    public static function foo() { 
        static::who(); 
    }
    
    
    public static function who() { 
        echo __CLASS__ . "\n"; 
    }
}



class B extends A { 
    public static function test() { 
        A::foo(); 
        parent::foo(); 
        self::foo(); 
    }
    
    
    public static function who() { 
        echo __CLASS__ . "\n"; 
    }
}


class C extends B { 
    public static function who() { 
        echo __CLASS__ . "\n"; 
    }
}



C::test(); 


