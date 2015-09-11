<?php
function square($num) { 
    return $num * $num; 
}

echo (square(4)); // outputs '16'.

/****/

function small_numbers() { 
    return array(0, 1, 2); 
}

list($zero, $one, $two) = small_numbers(); 

/****/

function &returns_reference() { 
    return $someref; 
}

$newref = &returns_reference(); 


/****/

function sum($a, $b): float { 
    return $a + $b; 
}

// Note that a float will be returned.
var_dump(sum(1, 2)); 

/****/

declare(strict_types = 1); 

function sum($a, $b): int { 
    return $a + $b; 
}

var_dump(sum(1, 2)); 
var_dump(sum(1, 2.5)); 

/****/

class C { 
}

function getC(): C { 
    return new C(); 
}

var_dump(getC()); 

