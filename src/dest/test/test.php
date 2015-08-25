<?php
    
    const A = 100;
    
    const B = "PingPHP";
    
    
    function func($a, $b = 1) {
        
        if ($a == 1) {
            $b = 11;
        } else if ($a == 2) {
            $b = 22;
        } else {
            $b = 33;
        }
        
        return;
    }
    
    class MyClass extends BaseClass implements AInterface, BInterface {
        
        
    }
    
    
