<?php
declare(ticks = 1); 

// A function called on each tick event
function tick_handler() { 
    echo "tick_handler() called\n"; 
}

register_tick_function('tick_handler'); 

$a = 1; 

if ($a > 0) { 
    $a += 2; 
    print $a; 
}

/****/

function tick_handler() { 
    echo "tick_handler() called\n"; 
}

$a = 1; 
tick_handler(); 

if ($a > 0) { 
    $a += 2; 
    tick_handler(); 
    print $a; 
    tick_handler(); 
}

tick_handler(); 

/****/

declare(encoding = 'ISO-8859-1'); 
// code here
