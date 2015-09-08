<?php
class classname { 
    function __construct() { 
        echo __METHOD__, "\n"; 
    }
}

function funcname() { 
    echo __FUNCTION__, "\n"; 
}

const CONSTNAME = "global"; 

$a = 'classname'; 
$obj = new $a; // prints classname::__construct
$b = 'funcname'; 
$b(); // prints funcname
echo constant('CONSTNAME'), "\n"; // prints global

/****/

namespace namespacename; 
class classname { 
    function __construct() { 
        echo __METHOD__, "\n"; 
    }
}

function funcname() { 
    echo __FUNCTION__, "\n"; 
}

const CONSTNAME = "namespaced"; 

include 'example1.php'; 

$a = 'classname'; 
$obj = new $a; // prints classname::__construct
$b = 'funcname'; 
$b(); // prints funcname
echo constant('CONSTNAME'), "\n"; // prints global

/** note that if using double quotes, "\\namespacename\\classname" must be used **/
$a = '\namespacename\classname'; 
$obj = new $a; // prints namespacename\classname::__construct
$a = 'namespacename\classname'; 
$obj = new $a; // also prints namespacename\classname::__construct
$b = 'namespacename\funcname'; 
$b(); // prints namespacename\funcname
$b = '\namespacename\funcname'; 
$b(); // also prints namespacename\funcname
echo constant('\namespacename\CONSTNAME'), "\n"; // prints namespaced
echo constant('namespacename\CONSTNAME'), "\n"; // also prints namespaced
