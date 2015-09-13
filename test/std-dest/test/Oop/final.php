<?php
class BaseClass { 
    public function test() { 
        echo "BaseClass::test() called\n"; 
    }
    
    
    final public function moreTesting() { 
        echo "BaseClass::moreTesting() called\n"; 
    }
}



class ChildClass extends BaseClass { 
    public function moreTesting() { 
        echo "ChildClass::moreTesting() called\n"; 
    }
}


// Results in Fatal error: Cannot override final method BaseClass::moreTesting()

/****/

final class BaseClass { 
    public function test() { 
        echo "BaseClass::test() called\n"; 
    }
    
    
    // 这里无论你是否将方法声明为final，都没有关系
    final public function moreTesting() { 
        echo "BaseClass::moreTesting() called\n"; 
    }
}



class ChildClass extends BaseClass { 
}

// 产生 Fatal error: Class ChildClass may not inherit from final class (BaseClass)

