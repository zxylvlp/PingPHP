<?php
function foo($arg_1, $arg_2, $arg_n) { 
    echo "Example function.\n"; 
    return $retval; 
}

/****/

$makefoo = true; 

/**不能在此处调用foo()函数，
   因为它还不存在，但可以调用bar()函数.**/

bar(); 

if ($makefoo) { 
    function foo() { 
        echo "I don't exist until program execution reaches me.\n"; 
    }
}

/**现在可以安全调用函数 foo()了，
   因为 $makefoo 值为真**/

if ($makefoo) { 
    foo(); 
}

function bar() { 
    echo "I exist immediately upon program start.\n"; 
}

/****/

function foo() { 
    function bar() { 
        echo "I don't exist until foo() is called.\n"; 
    }
}

/** 现在还不能调用bar()函数，因为它还不存在 **/

foo(); 

/** 现在可以调用bar()函数了，因为foo()函数
    的执行使得bar()函数变为已定义的函数 **/

bar(); 

/****/

function recursion($a) { 
    if ($a < 20) { 
        echo "$a\n"; 
        recursion($a + 1); 
    }
}
