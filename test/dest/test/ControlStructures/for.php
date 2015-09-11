<?php
/**example 1**/
foreach (range(1, 10) as $i) { 
    echo $i; 
}

/**example 2**/
/**example 3**/

$i = 1; 
while (true) { 
    if ($i > 10) { 
        break; 
    }
    echo $i; 
    $i++; 
}

/**example 4**/

$i = 1; 
$j = 0; 
foreach (range(1, 10) as $i) { 
    $j += $i; 
    print $i; 
}

/****/


/**
 * 此数组将在遍历的过程中改变其中某些单元的值
**/
$people = [['name' => 'Kalle', 'salt' => 856412], ['name' => 'Pierre', 'salt' => 215863]]; 


foreach (range(0, count($people) - 1) as $i) { 
    $people[$i]['salt'] = rand(000000, 999999); 
}

