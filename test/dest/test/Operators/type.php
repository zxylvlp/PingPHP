<?php
class MyClass { 
}

class NotMyClass { 
}

$a = new MyClass(); 

var_dump($a instanceof MyClass); 
var_dump($a instanceof NotMyClass); 

/****/

class ParentClass { 
}

class MyClass extends ParentClass { 
}

$a = new MyClass(); 

var_dump($a instanceof MyClass); 
var_dump($a instanceof ParentClass); 

/****/

class MyClass { 
}

$a = new MyClass(); 
var_dump(!($a instanceof stdClass)); 

/****/

interface MyInterface { 
}

class MyClass implements MyInterface { 
}

$a = new MyClass(); 

var_dump($a instanceof MyClass); 
var_dump($a instanceof MyInterface); 

/****/

interface MyInterface { 
}

class MyClass implements MyInterface { 
}

$a = new MyClass(); 
$b = new MyClass(); 
$c = 'MyClass'; 
$d = 'NotMyClass'; 

var_dump($a instanceof $b); // $b is an object of class MyClass
var_dump($a instanceof $c); // $c is a string 'MyClass'
var_dump($a instanceof $d); // $d is a string 'NotMyClass'

/****/

$a = 1; 
$b = NULL; 
$c = imagecreate(5, 5); 
var_dump($a instanceof stdClass); // $a is an integer
var_dump($b instanceof stdClass); // $b is NULL
var_dump($c instanceof stdClass); // $c is a resource
var_dump(false instanceof stdClass); 

/****/

$d = 'NotMyClass'; 
var_dump($a instanceof $d); // no fatal error here

