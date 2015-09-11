<?php
$arr = array('one', 'two', 'three', 'four', 'stop', 'five'); 
while (list($dummy, $val) = each($arr)) { 
    if ($val == 'stop') { 
        break; // You could also write 'break 1;' here. 
    }
    echo "$val<br />\n"; 
}

/** 使用可选参数 **/

$i = 0; 
while (++$i) { 
    switch ($i) { 
        case 5: 
            echo "At 5<br />\n"; 
            break; 
        case 10: 
            echo "At 10; quitting<br />\n"; 
            break; 
        default: 
            break; 
    }
}
