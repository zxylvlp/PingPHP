<?php

class MyClass { 
    
    public $var1 = 'value 1'; 
    public $var2 = 'value 2'; 
    public $var3 = 'value 3'; 
    
    protected $protected_ = 'protected var'; 
    private $private_ = 'private var'; 
    
    function iterateVisible() { 
        echo "MyClass::iterateVisible:\n"; 
        foreach ($this as $key => $value) { 
            print "$key => $value\n"; 
        }
    }
}




$class_ = new MyClass(); 

foreach ($class_ as $key => $value) { 
    print "$key => $value\n"; 
}

echo "\n"; 


$class_->iterateVisible(); 



/****/


class MyIterator implements Iterator { 
    
    private $var = array(); 
    
    public function __construct($array_) { 
        
        if ((is_array($array_))) { 
            $this->var = $array_; 
        }
    }
    
    
    public function rewind() { 
        echo "rewinding\n"; 
        reset($this->var); 
    }
    
    
    public function current() { 
        $var = current($this->var); 
        echo "current: $var\n"; 
        return $var; 
    }
    
    
    public function key() { 
        $var = key($this->var); 
        echo "key: $var\n"; 
        return $var; 
    }
    
    
    public function next() { 
        $var = next($this->var); 
        echo "next: $var\n"; 
        return $var; 
    }
    
    
    public function valid() { 
        $var = $this->current() !== false; 
        echo "valid: $var\n"; 
        return $var; 
    }
}



$values = array(1, 2, 3); 
$it = new MyIterator($values); 

foreach ($it as $a => $b) { 
    print "$a: $b\n"; 
}



/****/


class MyCollection implements IteratorAggregate { 
    
    private $items = array(); 
    private $count = 0; 
    
    // Required definition of interface IteratorAggregate
    public function getIterator() { 
        return new MyIterator($this->items); 
    }
    
    
    public function add($value) { 
        $this->items[$this->count++] = $value; 
    }
}



$coll = new MyCollection(); 
$coll->add('value 1'); 
$coll->add('value 2'); 
$coll->add('value 3'); 

foreach ($coll as $key => $val) { 
    echo "key/value: [$key -> $val]\n\n"; 
}



/****/


