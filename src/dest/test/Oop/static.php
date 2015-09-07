<?php
class Foo { 
    public static $my_static = 'foo'; 
    
    public function staticValue() { 
        return self::$my_static; 
    }
}

class Bar extends Foo { 
    public function fooStatic() { 
        return parent::$my_static; 
    }
}

print join('', [Foo::$my_static, "\n"]); 

$foo = new Foo(); 
print join('', [$foo->staticValue(), "\n"]); 
print join('', [$foo->my_static, "\n"]); // Undefined "Property" my_static 

print join('', [foo::$my_static, "\n"]); 
$classname = 'Foo'; 
print join('', [$classname::$my_static, "\n"]); // As of PHP 5.3.0

print join('', [Bar::$my_static, "\n"]); 
$bar = new Bar(); 
print join('', [$bar->fooStatic(), "\n"]); 

/****/

class Foo { 
    public static function aStaticMethod() { 
        // ...
    }
}

Foo::aStaticMethod(); 
$classname = 'Foo'; 
$classname::aStaticMethod(); // 自 PHP 5.3.0 起
