<?php
function takes_array($input) { 
    echo "$input[0] + $input[1] = " . $input[0] + $input[1]; 
}

/****/

function add_some_extra(&$string) { 
    $string = join('', [$string, 'and something extra.']); 
}

$str = 'This is a string, '; 
add_some_extra($str); 
echo ($str); // outputs 'This is a string, and something extra.'

/****/

function makecoffee($type = "cappuccino") { 
    return "Making a cup of $type.\n"; 
}

echo (makecoffee()); 
echo (makecoffee(null)); 
echo (makecoffee("espresso")); 

/****/

function makecoffee($types = array("cappuccino"), $coffeeMaker = NULL) { 
    $device = is_null($coffeeMaker) ? "hands" : $coffeeMaker; 
    return join("", ["Making a cup of ", join(", ", $types), " with $device.\n"]); 
}

echo (makecoffee()); 
echo (makecoffee(array("cappuccino", "lavazza"), "teapot")); 

/****/

function makeyogurt($type = "acidophilus", $flavour) { 
    return "Making a bowl of $type $flavour.\n"; 
}

echo (makeyogurt("raspberry")); // won't work as expected

/****/

function makeyogurt($flavour, $type = "acidophilus") { 
    return "Making a bowl of $type $flavour.\n"; 
}

echo (makeyogurt("raspberry")); // works as expected

/****/

class C { 
}
class D extends C { 
}

// This doesn't extend C.
class E { 
}

function f(C $c) { 
    echo (join("", [get_class($c), "\n"])); 
}

f(new C()); 
f(new D()); 
f(new E()); 

/****/

interface I { 
    public function f(); 
}

class C implements I { 
    public function f() { 
    }
}

// This doesn't implement I.
class E { 
}

function f(I $i) { 
    echo (join("", [get_class($i), "\n"])); 
}

f(new C()); 
f(new E()); 

/****/

class C { 
}

function f(C $c = null) { 
    var_dump($c); 
}

f(new C()); 
f(null); 

/****/

declare(strict_types = 1); 

function sum(int $a, int $b) { 
    return $a + $b; 
}

var_dump(sum(1, 2)); 
var_dump(sum(1.5, 2.5)); 

/****/

function sum(int $a, int $b) { 
    return $a + $b; 
}

var_dump(sum(1, 2)); 

// These will be coerced to integers: note the output below!
var_dump(sum(1.5, 2.5)); 

/****/

declare(strict_types = 1); 

function sum(int $a, int $b) { 
    return $a + $b; 
}

try { 
    var_dump(sum(1, 2)); 
    var_dump(sum(1.5, 2.5)); 
} catch (TypeError $e) { 
    echo (join("", ['Error: ', $e->getMessage()])); 
} 

/****/

function sum(...$numbers) { 
    $acc = 0; 
    foreach ($numbers as $n) { 
        $acc += $n; 
    }
    return $acc; 
}

echo (sum(1, 2, 3, 4)); 

/****/

function add($a, $b) { 
    return $a + $b; 
}

echo add(...[1, 2]), "\n"; 

$a = [1, 2]; 
echo (add(...$a)); 

/****/

function total_intervals($unit, DateInterval ...$intervals) { 
    $time = 0; 
    foreach ($intervals as $interval) { 
        $time += $interval->unit; 
    }
    return $time; 
}

$a = new DateInterval('P1D'); 
$b = new DateInterval('P2D'); 
echo total_intervals('d', $a, $b), ' days'; 

// This will fail, since null isn't a DateInterval object.
echo (total_intervals('d', null)); 

/****/

function sum() { 
    $acc = 0; 
    foreach (func_get_args() as $n) { 
        $acc += $n; 
    }
    return $acc; 
}

echo (sum(1, 2, 3, 4)); 
