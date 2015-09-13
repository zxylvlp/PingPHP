<?php
$a = 1.234; 
$b = 1.2e3; 
$c = 7E-10; 

/****/

$a = 1.23456789; 
$b = 1.23456780; 
$epsilon = 0.00001; 

if (abs($a - $b) < $epsilon) { 
    echo "true"; 
}
