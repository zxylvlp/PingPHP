<?php
class A { 
    public $foo = 1; 
}

$a = new A(); 
$b = $a; // $a ,$b都是同一个标识符的拷贝
// ($a) = ($b) = <id>
$b->foo = 2; 
echo $a->foo . "\n"; 


$c = new A(); 
$d = &$c; // $c ,$d是引用
// ($c,$d) = <id>

$d->foo = 2; 
echo $c->foo . "\n"; 


$e = new A(); 

function foo($obj) { 
    // ($obj) = ($e) = <id>
    $obj->foo = 2; 
}

foo($e); 
echo $e->foo . "\n"; 

