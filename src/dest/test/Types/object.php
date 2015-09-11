<?php
class foo { 
    function do_foo() { 
        echo "Doing foo."; 
    }
}

$bar = new foo(); 
$bar->do_foo(); 

/****/

$obj = (object)'ciao'; 
echo $obj->scalar; // outputs 'ciao'
