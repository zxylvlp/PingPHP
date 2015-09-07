<?php
class BaseClass { 
    public function __construct() { 
        print "In BaseClass constructor\n"; 
    }
}

class SubClass extends BaseClass { 
    public function __construct() { 
        parent::__construct(); 
        print "In SubClass constructor\n"; 
    }
}

class OtherSubClass extends BaseClass { 
    // inherits BaseClass's constructor
}

// In BaseClass constructor
$obj = new BaseClass(); 

// In BaseClass constructor
// In SubClass constructor
$obj = new SubClass(); 

// In BaseClass constructor
$obj = new OtherSubClass(); 

/****/

namespace Foo; 
class Bar { 
    public function Bar() { 
        // treated as constructor in PHP 5.3.0-5.3.2
        // treated as regular method as of PHP 5.3.3
    }
}

/****/

class MyDestructableClass { 
    public function __construct() { 
        print "In constructor\n"; 
        $this->name = "MyDestructableClass"; 
    }
    
    public function __destruct() { 
        print join("", ["Destroying ", $this->name, "\n"]); 
    }
}

$obj = new MyDestructableClass(); 


