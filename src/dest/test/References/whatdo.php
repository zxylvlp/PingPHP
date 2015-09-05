<?php
$a = &$b; 
/****/
function foo(&$var) { 
}

foo($a); // $a is "created" and assigned to null

$b = array(); 
foo($b['b']); 
var_dump(array_key_exists('b', $b)); // bool(true)

$c = new StdClass(); 
foo($c->d); 
var_dump(property_exists($c, 'd')); // bool(true)
/****/
$bar = &new fooclass(); 
$foo = &find_var($bar); 
/****/
$var1 = "Example variable"; 
$var2 = ""; 

function global_references($use_globals) { 
    global $var1, $var2; 
    if (!$use_globals) { 
        $var2 = &$var1; // visible only inside the function
    } else { 
        $GLOBALS["var2"] = &$var1; // visible also in global context
    }
}

global_references(false); 
echo "var2 is set to '$var2'\n"; // var2 is set to ''
global_references(true); 
echo "var2 is set to '$var2'\n"; // var2 is set to 'Example variable'
/****/
$ref = 0; 
$row = &$ref; 
foreach (array(1, 2, 3) as $row) { 
}
echo $ref; // 3 - last element of the iterated array
/****/
function foo(&$var) { 
    $var++; 
}

$a = 5; 
foo($a); 
