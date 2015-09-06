<?php
function __autoload($class_name) { 
    require_once join('', [$class_name, '.php']); 
}

$obj = new MyClass1(); 
$obj2 = new MyClass2(); 

/****/

function __autoload($name) { 
    var_dump($name); 
}

class Foo implements ITest { 
}

/**
string(5) "ITest"

Fatal error: Interface 'ITest' not found in ...
**/

/****/

function __autoload($name) { 
    echo "Want to load $name.\n"; 
    throw new Exception("Unable to load $name."); 
}

try { 
    $obj = new NonLoadableClass(); 
} catch (Exception $e) { 
    echo $e->getMessage(), "\n"; 
} 

/****/

function __autoload($name) { 
    echo "Want to load $name.\n"; 
    throw new MissingException("Unable to load $name."); 
}

try { 
    $obj = new NonLoadableClass(); 
} catch (Exception $e) { 
    echo $e->getMessage(), "\n"; 
} 



