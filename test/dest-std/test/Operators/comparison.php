<?php
var_dump(0 == "a"); // 0 == 0 -> true
var_dump("1" == "01"); // 1 == 1 -> true
var_dump("10" == "1e1"); // 10 == 10 -> true
var_dump(100 == "1e2"); // 100 == 100 -> true

switch ("a") { 
    case 0: 
        echo "0"; 
        break; 
    case "a": // never reached because "a" is already matched with 0
        echo "a"; 
        break; 
}

/****/
// 数组是用标准比较运算符这样比较的
function standard_array_compare($op1, $op2) { 
    if (count($op1) < count($op2)) { 
        return -1; // $op1 < $op2
    } else if (count($op1) > count($op2)) { 
        return 1; // $op1 > $op2
    }
    foreach ($op1 as $key => $val) { 
        if (!array_key_exists($key, $op2)) { 
            return null; // uncomparable
        } else if ($val < $op2[$key]) { 
            return -1; 
        } else if ($val > $op2[$key]) { 
            return 1; 
        }
    }
    return 0; // $op1 == $op2
}

/****/

// Example usage for: Ternary Operator
$action = (empty($_POST['action'])) ? 'default' : $_POST['action']; 

// The above is identical to this if/else statement
if (empty($_POST['action'])) { 
    $action = 'default'; 
} else { 
    $action = $_POST['action']; 
}

/****/

// 乍看起来下面的输出是 'true'
echo (true ? 'true' : 'false' ? 't' : 'f'); 
// 然而，上面语句的实际输出是't'，因为三元运算符是从左往右计算的

// 下面是与上面等价的语句，但更清晰
echo ((true ? 'true' : 'false') ? 't' : 'f'); 

// here, you can see that the first expression is evaluated to 'true', which
// in turn evaluates to (bool)true, thus returning the true branch of the
// second ternary expression.
