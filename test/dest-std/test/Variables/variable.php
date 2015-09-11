<?php
$a = 'hello'; 

/****/

$$a = 'world'; 

/****/

echo "$a ${$a}"; 

/****/

echo "$a $hello"; 

/****/

class foo { 
    public $bar = 'I am bar.'; 
    public $arr = array('I am A.', 'I am B.', 'I am C.'); 
    public $r = 'I am r.'; 
}

$foo = new foo(); 
$bar = 'bar'; 
$baz = array('foo', 'bar', 'baz', 'quux'); 
echo $foo->bar . "\n"; 
echo $foo->baz[1] . "\n"; 

$start = 'b'; 
$end = 'ar'; 

echo $foo->{$start . $end} . "\n";

$arr = 'arr'; 
echo $foo->$arr[1] . "\n"; 

echo $foo->{$arr}[1] . "\n";

