<?php
$arr = array(1, 2, 3, 4); 
foreach ($arr as $value) { 
    $value = $value * 2; 
}

// $arr is now array(2, 4, 6, 8)
unset($value); // 最后取消掉引用

/****/

foreach (array(1, 2, 3, 4) as &$value) { 
    $value = $value * 2; 
}

/****/

$arr = array("one", "two", "three"); 
reset($arr); 
while (list($dummy, $value) = each($arr)) { 
    echo "Value: $value<br>\n"; 
}

foreach ($arr as $value) { 
    echo "Value: $value<br />\n"; 
}

/****/

$arr = array("one", "two", "three"); 
reset($arr); 
while (list($key, $value) = each($arr)) { 
    echo "Key: $key Value: $value<br />\n"; 
}

foreach ($arr as $key => $value) { 
    echo "Key: $key Value: $value<br />\n"; 
}

/****/

/** foreach example 1: value only **/

$a = array(1, 2, 3, 17); 

foreach ($a as $v) { 
    echo "Current value of \$a: $v.\n"; 
}

/** foreach example 2: value (with its manual access notation printed for illustration) **/

$a = array(1, 2, 3, 17); 

$i = 0; // for illustrative purposes only

foreach ($a as $v) { 
    echo "\$a[$i] => $v.\n"; 
    $i++; 
}

/** foreach example 3: key and value **/

$a = ["one" => 1, "two" => 2, "three" => 3, "seventeen" => 17]; 

foreach ($a as $k => $v) { 
    echo "\$a[$k] => $v.\n"; 
}

/** foreach example 4: multi-dimensional arrays **/
$a = array(); 
$a[0][0] = "a"; 
$a[0][1] = "b"; 
$a[1][0] = "y"; 
$a[1][1] = "z"; 

foreach ($a as $v1) { 
    foreach ($v1 as $v2) { 
        echo "$v2\n"; 
    }
}

/** foreach example 5: dynamic arrays **/

foreach (array(1, 2, 3, 4, 5) as $v) { 
    echo "$v\n"; 
}


/****/

$array = [[1, 2], [3, 4]]; 

foreach ($array as list($a, $b)) { 
    // $a contains the first element of the nested array,
    // and $b contains the second element.
    echo "A: $a B: $b\n"; 
}

/****/

$array = [[1, 2], [3, 4]]; 

foreach ($array as list($a)) { 
    // Note that there is no $b here.
    echo "$a\n"; 
}

/****/

$array = [[1, 2], [3, 4]]; 

foreach ($array as list($a, $b, $c)) { 
    echo "A: $a B: $b C: $c\n"; 
}
