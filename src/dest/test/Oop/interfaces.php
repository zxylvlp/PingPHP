<?php
// 声明一个'iTemplate'接口
interface iTemplate { 
    public function setVariable($name, $var); 
    public function getHtml($template); 
}


// 实现接口
// 下面的写法是正确的
class Template implements iTemplate { 
    private $vars = array(); 
    
    public function setVariable($name, $var) { 
        $this->vars[$name] = $var; 
    }
    
    public function getHtml($template) { 
        foreach ($this->vars as $name => $value) { 
            $template = str_replace('{' . $name . '}', $value, $template); 
        }
        
        return $template; 
    }
}

// 下面的写法是错误的，会报错，因为没有实现 getHtml()：
// Fatal error: Class BadTemplate contains 1 abstract methods
// and must therefore be declared abstract (iTemplate::getHtml)
class BadTemplate implements iTemplate { 
    private $vars = array(); 
    
    public function setVariable($name, $var) { 
        $this->vars[$name] = $var; 
    }
}

/****/

interface a { 
    public function foo(); 
}

interface b extends a { 
    public function baz(Baz $baz); 
}

// 正确写法
class c implements b { 
    public function foo() { 
    }
    
    public function baz(Baz $baz) { 
    }
}

// 错误写法会导致一个致命错误
class d implements b { 
    public function foo() { 
    }
    
    public function baz(Foo $foo) { 
    }
}

/****/
interface a { 
    public function foo(); 
}

interface b { 
    public function bar(); 
}

interface c extends a, b { 
    public function baz(); 
}

class d implements c { 
    public function foo() { 
    }
    
    public function bar() { 
    }
    
    public function baz() { 
    }
}

/****/
interface a { 
    const B = 'Interface constant'; 
}

// 输出接口常量
echo a::B; 

// 错误写法，因为常量不能被覆盖。接口常量的概念和类常量是一样的。
class b implements a { 
    const B = 'Class constant'; 
}

