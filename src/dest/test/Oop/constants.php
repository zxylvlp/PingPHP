<?php
class MyClass { 
    const CONSTANT = 'constant value'; 
    
    public function showConstant() { 
        echo self::CONSTANT, "\n"; 
    }
}

echo MyClass::CONSTANT, "\n"; 

$classname = "MyClass"; 
echo $classname::CONSTANT, "\n"; // 自 5.3.0 起

$class_ = new MyClass(); 
$class_->showConstant(); 

echo $class::CONSTANT, "\n"; // 自 PHP 5.3.0 起

/****/

class foo { 
    // 自 PHP 5.3.0 起
    const bar = <<<'EOT'
bar
EOT;
}
