<?php
$a = 3 * 3 % 5; // (3 * 3) % 5 = 4
$a = true ? 0 : true ? 1 : 2; // (true ? 0 : true) ? 1 : 2 = 2

$a = 1; 
$b = 2; 
$a = $b += 3; // $a = ($b += 3) -> $a = 5, $b = 5

// mixing ++ and + produces undefined behavior
$a = 1; 
echo (++$a + $a++); // may print 4 or 5
