<?php
setcookie("MyCookie[foo]", 'Testing 1', time() + 3600); 
setcookie("MyCookie[bar]", 'Testing 2', time() + 3600); 

/****/

if (isset($_COOKIE['count'])) { 
    $count = $_COOKIE['count'] + 1; 
} else { 
    $count = 1; 
}

setcookie('count', $count, time() + 3600); 
setcookie("Cart[$count]", $item, time() + 3600); 
