<?php
while (list($key, $value) = each($arr)) { 
    if (!($key % 2)) { // skip odd members
        continue; 
    }
    do_something_odd($value); 
}

$i = 0; 
while ($i++ < 5) { 
    echo "Outer<br />\n"; 
    while (1) { 
        echo "Middle<br />\n"; 
        while (1) { 
            echo "Inner<br />\n"; 
            continue 3; 
        }
        echo "This never gets output.<br />\n"; 
    }
    echo "Neither does this.<br />\n"; 
}

