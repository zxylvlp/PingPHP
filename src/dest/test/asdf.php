<?php
class MyClass extends MyBaseClass implements MyIterfaceA, MyIterfaceB {//line1
        
        public $a;//line2
        public $b;//line2
        
        /**
	我的多行注释
	**/
        
        //我的单行注释
        
        
	public $c = 1;
	
        public static function myMethod() {//line2
        }
}

interface MyIterfaceA extends MyIterfaceB {//line2
        
        public static function myMethod();
}

