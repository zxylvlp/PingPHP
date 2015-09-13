<?php
/**
 * Ignore the top section,
 * it is just formatting to make output clearer.
**/

$format = '(%1$2d = %1$04b) = (%2$2d = %2$04b)' . ' %3$s (%4$2d = %4$04b)' . "\n"; 

echo <<<EOH
 ---------     ---------  -- ---------
 result        value      op test
 ---------     ---------  -- ---------
EOH;


/**
 * Here are the examples.
**/

$values = array(0, 1, 2, 4, 8); 
$test = 1 + 4; 

echo "\n Bitwise AND \n"; 
foreach ($values as $value) { 
    $result = $value & $test; 
    printf($format, $result, $value, '&', $test); 
}

echo "\n Bitwise Inclusive OR \n"; 

foreach ($values as $value) { 
    $result = $value | $test; 
    printf($format, $result, $value, '|', $test); 
}

echo "\n Bitwise Exclusive OR (XOR) \n"; 

foreach ($values as $value) { 
    $result = $value ^ $test; 
    printf($format, $result, $value, '^', $test); 
}

/****/

echo 12 ^ 9; // Outputs '5'

echo "12" ^ "9"; // Outputs the Backspace character (ascii 8)
// ('1' (ascii 49)) ^ ('9' (ascii 57)) = #8

echo "hallo" ^ "hello"; // Outputs the ascii values #0 #4 #0 #0 #0
// 'a' ^ 'e' = #4

echo 2 ^ "3"; // Outputs 1
// 2 ^ ((int)"3") == 1

echo "2" ^ 3; // Outputs 1
// ((int)"2") ^ 3 == 1

/****/
/**
 * Here are the examples.
**/

echo "\n--- BIT SHIFT RIGHT ON POSITIVE INTEGERS ---\n"; 

$val = 4; 
$places = 1; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'copy of sign bit shifted into left side'); 

$val = 4; 
$places = 2; 
$res = $val >> $places; 
p($res, $val, '>>', $places); 

$val = 4; 
$places = 3; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'bits shift out right side'); 

$val = 4; 
$places = 4; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'same result as above; can not shift beyond 0'); 


echo "\n--- BIT SHIFT RIGHT ON NEGATIVE INTEGERS ---\n"; 

$val = -4; 
$places = 1; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'copy of sign bit shifted into left side'); 

$val = -4; 
$places = 2; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'bits shift out right side'); 

$val = -4; 
$places = 3; 
$res = $val >> $places; 
p($res, $val, '>>', $places, 'same result as above; can not shift beyond -1'); 


echo "\n--- BIT SHIFT LEFT ON POSITIVE INTEGERS ---\n"; 

$val = 4; 
$places = 1; 
$res = $val << $places; 
p($res, $val, '<<', $places, 'zeros fill in right side'); 

$val = 4; 
$places = (PHP_INT_SIZE * 8) - 4; 
$res = $val << $places; 
p($$res, $val, '<<', $places); 

$val = 4; 
$places = (PHP_INT_SIZE * 8) - 3; 
$res = $val << $places; 
p($res, $val, '<<', $places, 'sign bits get shifted out'); 

$val = 4; 
$places = (PHP_INT_SIZE * 8) - 2; 
$res = $val << $places; 
p($res, $val, '<<', $places, 'bits shift out left side'); 


echo "\n--- BIT SHIFT LEFT ON NEGATIVE INTEGERS ---\n"; 

$val = -4; 
$places = 1; 
$res = $val << $places; 
p($res, $val, '<<', $places, 'zeros fill in right side'); 

$val = -4; 
$places = (PHP_INT_SIZE * 8) - 3; 
$res = $val << $places; 
p($res, $val, '<<', $places); 

$val = -4; 
$places = (PHP_INT_SIZE * 8) - 2; 
$res = $val << $places; 
p($res, $val, '<<', $places, 'bits shift out left side, including sign bit'); 


/**
 * Ignore this bottom section,
 * it is just formatting to make output clearer.
**/

function p($res, $val, $op, $places, $note = '') { 
    $format = '%0' . (PHP_INT_SIZE * 8) . "b\n"; 
    
    printf("Expression: %d = %d %s %d\n", $res, $val, $op, $places); 
    
    echo " Decimal:\n"; 
    printf("  val=%d\n", $val); 
    printf("  res=%d\n", $res); 
    
    echo " Binary:\n"; 
    printf('  val=' . $format, $val); 
    printf('  res=' . $format, $res); 
    
    if ($note) { 
        echo " NOTE: $note\n"; 
    }
    
    echo "\n"; 
}
