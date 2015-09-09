<?php
echo (preg_replace_callback('~-([a-z])~', function ($match) { 
    return strtoupper($match[1]); 
}, 'hello-world')); 
// 输出 helloWorld

$greet = (function ($name) { 
    printf("Hello %s\r\n", $name); 
}); 

$greet('World'); 
$greet('PHP'); 
/****/

$message = 'hello'; 

// 没有 "use"
$example = (function () { 
    var_dump($message); 
}); 

echo ($example()); 

// 继承 $message
$example = (function () use ($message){ 
    var_dump($message); 
}); 

echo ($example()); 

// Inherited variable's value is from when the function
// is defined, not when called
$message = 'world'; 
echo ($example()); 

// Reset message
$message = 'hello'; 

// Inherit by-reference
$example = (function () use (&$message){ 
    var_dump($message); 
}); 

echo ($example()); 

// The changed value in the parent scope
// is reflected inside the function call
$message = 'world'; 
echo ($example()); 

// Closures can also accept regular arguments
$example = (function ($arg) use ($message){ 
    var_dump("{$arg} {$message}"); 
}); 

$example("hello"); 

/****/
// 一个基本的购物车，包括一些已经添加的商品和每种商品的数量。
// 其中有一个方法用来计算购物车中所有商品的总价格，该方法使
// 用了一个 closure 作为回调函数。
class Cart { 
    const PRICE_BUTTER = 1.00; 
    const PRICE_MILK = 3.00; 
    const PRICE_EGGS = 6.95; 
    
    protected $products = array(); 
    
    public function add($product, $quantity) { 
        $this->products[$product] = $quantity; 
    }
    
    public function getQuantity($product) { 
        return isset($this->products[$product]) ? $this->products[$product] : false; 
    }
    
    public function getTotal($tax) { 
        $total = 0.00; 
        $callback = (function ($quantity, $product) use ($tax, &$total){ 
            $pricePerItem = constant(__CLASS__ . "::PRICE_" . strtoupper($product)); 
            $total += ($pricePerItem * $quantity) * ($tax + 1.0); 
        }); 
        array_walk($this->products, $callback); 
        return round($total, 2); 
    }
}

$my_cart = new Cart(); 

// 往购物车里添加条目
$my_cart->add('butter', 1); 
$my_cart->add('milk', 3); 
$my_cart->add('eggs', 6); 

// 打出出总价格，其中有 5% 的销售税.
print $my_cart->getTotal(0.05) . "\n"; 
// 最后结果是 54.29
