<?php
trait ezcReflectionReturnInfo { 
    function getReturnType() { 
        //1
    }
    function getReturnDescription() { 
        //2 
    }
}


class ezcReflectionMethod extends ReflectionMethod { 
    use ezcReflectionReturnInfo; 
}

class ezcReflectionFunction extends ReflectionFunction { 
    use ezcReflectionReturnInfo; 
}

/****/

class Base { 
    public function sayHello() { 
        echo 'Hello '; 
    }
}



trait SayWorld { 
    public function sayHello() { 
        parent::sayHello(); 
        echo 'World!'; 
    }
}



class MyHelloWorld extends Base { 
    use SayWorld; 
}


$o = new MyHelloWorld(); 
$o->sayHello(); 

/****/

trait HelloWorld { 
    public function sayHello() { 
        echo 'Hello World!'; 
    }
}



class TheWorldIsNotEnough { 
    use HelloWorld; 
    public function sayHello() { 
        echo 'Hello Universe!'; 
    }
}



$o = new TheWorldIsNotEnough(); 
$o->sayHello(); 

/****/

trait Hello { 
    public function sayHello() { 
        echo 'Hello '; 
    }
}



trait World { 
    public function sayWorld() { 
        echo 'World'; 
    }
}



class MyHelloWorld { 
    use Hello, World; 
    public function sayExclamationMark() { 
        echo '!'; 
    }
}



$o = new MyHelloWorld(); 
$o->sayHello(); 
$o->sayWorld(); 
$o->sayExclamationMark(); 

/****/

trait A { 
    public function smallTalk() { 
        echo 'a'; 
    }
    
    public function bigTalk() { 
        echo 'A'; 
    }
}



trait B { 
    public function smallTalk() { 
        echo 'b'; 
    }
    
    public function bigTalk() { 
        echo 'B'; 
    }
}



class Talker { 
    use A, B { 
        B::smallTalk insteadof A; 
        A::bigTalk insteadof B; 
    }
}



class Aliased_Talker { 
    use A, B { 
        B::smallTalk insteadof A; 
        A::bigTalk insteadof B; 
        B::bigTalk as talk; 
    }
}



/****/

trait HelloWorld { 
    public function sayHello() { 
        echo 'Hello World!'; 
    }
}



// 修改 sayHello 的访问控制
class MyClass1 { 
    use HelloWorld { 
        sayHello as protected; 
    }
}


// 给方法一个改变了访问控制的别名
// 原版 sayHello 的访问控制则没有发生变化
class MyClass2 { 
    use HelloWorld { 
        sayHello as private myPrivateHello; 
    }
}


/****/

trait Hello { 
    public function sayHello() { 
        echo 'Hello '; 
    }
}



trait World { 
    public function sayWorld() { 
        echo 'World!'; 
    }
}



trait HelloWorld { 
    use Hello, World; 
}


class MyHelloWorld { 
    use HelloWorld; 
}


$o = new MyHelloWorld(); 
$o->sayHello(); 
$o->sayWorld(); 

/****/

trait Hello { 
    public function sayHelloWorld() { 
        echo 'Hello' . $this->getWorld(); 
    }
    
    abstract public function getWorld(); 
}


class MyHelloWorld { 
    private $world; 
    use Hello; 
    public function getWorld() { 
        return $this->world; 
    }
    
    public function setWorld($val) { 
        $this->world = $val; 
    }
}



/****/

trait Counter { 
    public function inc() { 
        static $c = 0; 
        $c = $c + 1; 
        echo "$c\n"; 
    }
}



class C1 { 
    use Counter; 
}


class C2 { 
    use Counter; 
}


$o = new C1(); 
$o->inc(); // echo 1
$p = new C2(); 
$p->inc(); // echo 1

/****/

trait StaticExample { 
    public static function doSomething() { 
        return 'Doing something'; 
    }
}



class Example { 
    use StaticExample; 
}


Example::doSomething(); 

/****/

trait PropertiesTrait { 
    public $x = 1; 
}


class PropertiesExample { 
    use PropertiesTrait; 
}


$example = new PropertiesExample(); 
$example->x; 

/****/

trait PropertiesTrait { 
    public $same = true; 
    public $different = false; 
}


class PropertiesExample { 
    use PropertiesTrait; 
    public $same = true; // Strict Standards
    public $different = true; // 致命错误
}

