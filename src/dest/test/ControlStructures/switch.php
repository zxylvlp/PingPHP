<?php
if ($i == 0) { 
    echo "i equals 0"; 
} else if ($i == 1) { 
    echo "i equals 1"; 
} else if ($i == 2) { 
    echo "i equals 2"; 
}

switch ($i) { 
    case 0: 
        echo "i equals 0"; 
        break; 
    case 1: 
        echo "i equals 1"; 
        break; 
    case 2: 
        echo "i equals 2"; 
        break; 
}

/****/

switch ($i) { 
    case "apple": 
        echo "i is apple"; 
        break; 
    case "bar": 
        echo "i is bar"; 
        break; 
    case "cake": 
        echo "i is cake"; 
        break; 
}

/****/

switch ($i) { 
    case 0: 
        echo "i equals 0"; 
        break; 
    case 1: 
        echo "i equals 1"; 
        break; 
    case 2: 
        echo "i equals 2"; 
        break; 
}

/****/

switch ($i) { 
    case 0: 
    case 1: 
    case 2: 
        echo "i is less than 3 but not negative"; 
        break; 
    case 3: 
        echo "i is 3"; 
        break; 
}
/****/

switch ($i) { 
    case 0: 
        echo "i equals 0"; 
        break; 
    case 1: 
        echo "i equals 1"; 
        break; 
    case 2: 
        echo "i equals 2"; 
        break; 
    default: 
        echo "i is not equal to 0, 1 or 2"; 
}

/****/

switch ($i) { 
    case 0: 
        echo "i equals 0"; 
        break; 
    case 1: 
        echo "i equals 1"; 
        break; 
    case 2: 
        echo "i equals 2"; 
        break; 
    default: 
        echo "i is not equal to 0, 1 or 2"; 
}

/****/

switch ($beer) { 
    case 'tuborg': 
    case 'carlsberg': 
    case 'heineken': 
        echo 'Good choice'; 
        break; 
    default: 
        echo 'Please make a new selection...'; 
}
