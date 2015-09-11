<?php
class AbstractClass { 
    // 强制要求子类定义这些方法
    abstract protected function getValue(); 
    abstract protected function prefixValue($prefix); 
    
    // 普通方法（非抽象方法）
    public function printOut() { 
        print (join('', [$this->getValue(), "\n"])); 
    }
}

class ConcreteClass1 extends AbstractClass { 
    protected function getValue() { 
        return "ConcreteClass1"; 
    }
    
    public function prefixValue($prefix) { 
        return "{$prefix}ConcreteClass1"; 
    }
}

class ConcreteClass2 extends AbstractClass { 
    public function getValue() { 
        return "ConcreteClass2"; 
    }
    
    public function prefixValue($prefix) { 
        return "{$prefix}ConcreteClass2"; 
    }
}

$class1 = new ConcreteClass1(); 
$class1->printOut(); 
echo $class1->prefixValue('FOO_'), "\n"; 

$class2 = new ConcreteClass2(); 
$class2->printOut(); 
echo $class2->prefixValue('FOO_'), "\n"; 

/****/

class AbstractClass { 
    // 我们的抽象方法仅需要定义需要的参数
    abstract protected function prefixName($name); 
}


class ConcreteClass extends AbstractClass { 
    
    // 我们的子类可以定义父类签名中不存在的可选参数
    public function prefixName($name, $separator = ".") { 
        if ($name == "Pacman") { 
            $prefix = "Mr"; 
        } else if ($name == "Pacwoman") { 
            $prefix = "Mrs"; 
        } else { 
            $prefix = ""; 
        }
        return "{$prefix}{$separator} {$name}"; 
    }
}

$class_ = new ConcreteClass(); 
echo $class_->prefixName("Pacman"), "\n"; 
echo $class_->prefixName("Pacwoman"), "\n"; 
