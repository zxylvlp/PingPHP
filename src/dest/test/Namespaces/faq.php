<?php
$a = new \stdClass(); 

/****/

$a = new stdClass(); 

/****/

namespace foo; 
$a = new \stdClass(); 

function test(\ArrayObject $typehintexample = null) { 
}

$a = \DirectoryIterator::CURRENT_AS_FILEINFO; 

// extending an internal or global class
class MyException extends \Exception { 
}

/****/

namespace foo; 

class MyClass { 
}

// using a class from the current namespace as a type hint
function test(MyClass $typehintexample = null) { 
}
// another way to use a class from the current namespace as a type hint
function test(\foo\MyClass $typehintexample = null) { 
}

// extending a class from the current namespace
class Extended extends MyClass { 
}

// accessing a global function
$a = \globalfunc(); 

// accessing a global constant
$b = \INI_ALL; 

/****/

namespace foo; 
$a = new \my\name(); // instantiates "my\name" class
echo (\strlen('hi')); // calls function "strlen"
$a = \INI_ALL; // $a is set to the value of constant "INI_ALL"

/****/

namespace foo; 
use blah\blah as foo; 

$a = new my\name(); // instantiates "foo\my\name" class
foo\bar::name(); // calls static method "name" in class "blah\blah\bar"
my\bar(); // calls function "foo\my\bar"
$a = my\BAR; // sets $a to the value of constant "foo\my\BAR"

/****/

namespace foo; 
use blah\blah as foo; 

$a = new name(); // instantiates "foo\name" class
foo::name(); // calls static method "name" in class "blah\blah"

/****/

namespace foo; 
use blah\blah as foo; 

const FOO = 1; 

function my() { 
}
function foo() { 
}

function sort(&$a) { 
    sort($a); 
    $a = array_flip($a); 
    return $a; 
}

my(); // calls "foo\my"
$a = strlen('hi'); // calls global function "strlen" because "foo\strlen" does not exist
$arr = array(1, 3, 2); 
$b = sort($arr); // calls function "foo\sort"
$c = foo(); // calls function "foo\foo" - import is not applied

$a = FOO; // sets $a to value of constant "foo\FOO" - import is not applied
$b = INI_ALL; // sets $b to value of global constant "INI_ALL"

/****/

namespace my\stuff; 
class MyClass { 
}

/****/

namespace another; 
class thing { 
}

/****/

namespace my\stuff; 
include ('file1.php'); 
include ('another.php'); 

use another\thing as MyClass; 
$a = new MyClass(); // instantiates class "thing" from namespace another

/****/

namespace my\stuff; 
use another\thing as MyClass; 
class MyClass { // fatal error: MyClass conflicts with import statement
}
$a = new MyClass(); 

/****/

namespace my\stuff\nested; 

class foo { 
}

/****/

namespace mine; 
use ultra\long\ns\name; 

$a = name\CONSTANT; 
name\func(); 

/****/

$a = new "dangerous\name"; // \n is a newline inside double quoted strings!
$obj = new $a; 

$a = new 'not\at\all\dangerous'; // no problems here.
$obj = new $a; 

/****/

namespace bar; 
$a = FOO; // produces notice - undefined constants "FOO" assumed "FOO";
$a = \FOO; // fatal error, undefined namespace constant FOO
$a = Bar\FOO; // fatal error, undefined namespace constant bar\Bar\FOO
$a = \Bar\FOO; // fatal error, undefined namespace constant Bar\FOO

/****/

namespace bar; 
// const NULL = 0 # fatal error;
// const true = 'stupid' # also fatal error;
// etc.
