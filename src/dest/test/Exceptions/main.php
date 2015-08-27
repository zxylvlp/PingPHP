<?php
function inverse($x) {
    if (!$x) {
        throw new Exception('Division by zero.'); 
    }
    return 1 / $x; 
}

try { 
    echo inverse(5), "\n"; 
    echo inverse(0), "\n"; 
} catch (Exception $e) { 
    echo 'Caught exception: ', $e->getMessage(), "\n"; 
} 

try { 
    echo inverse(0), "\n"; 
} catch (Exception $e) { 
    echo 'Caught exception: ', $e->getMessage(), "\n"; 
} finally { 
    echo "Second finally.\n"; 
}

// Continue execution
echo "Hello World\n"; 


class MyException extends Exception {
}

class Test {
    public function testing() {
        try { 
            try { 
                throw new MyException('foo!'); 
            } catch (MyException $e) { 
                // rethrow it
                throw $e; 
            } 
        } catch (Exception $e) { 
            var_dump($e->getMessage()); 
        } 
    }
}

$foo = new Test(); 
$foo->testing(); 

