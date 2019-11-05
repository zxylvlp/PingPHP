#PingPHP 
[![Build Status](https://travis-ci.org/zxylvlp/PingPHP.svg?branch=master)](https://travis-ci.org/zxylvlp/PingPHP)
###A PHP code generator which use Python Like grammar



##Introduction

- PingPHP essentially is a PHP code generator, similar to CoffeeScript(CS). However there is a big difference between this code and CS. 
- This library is in order to efficiently write Ping code with Python like grammar, and generate the PHP code which is not different from manual code. So it can improve the production efficiency, and the generated code is easy to maintain. 
- The purpose of the CS is to maintain the CS code, with a lot of syntax sugar, it improved the efficiency of the code but lost the readability of the code. 
- For the most of PHPer, such a large number of syntax sugar is very hard to accept. 
- Moreover, when we work with other developers, maintaining the Ping or CS code directly would impede communication.

- And one of the purposes of writing this library is to help PHPer to improve the work efficiency. Help us to spend more time with our family and friends.

##Installation

To install PingPHP, simply:

`$ sudo pip install pingphp`

or from source:

`$ sudo python setup.py install`

##Getting Started

Generate PingPHP.conf.json file.

```
$ pinginit
```

Then edit the config file with Wildcard.

```
{
    "ignoreFiles": [
        "test1/*"
    ], 
    "transFiles": [
        "test/**/*.ping"
    ], 
    "destDir": "dest"
}
```

Generate files:

```
$ pingrun
```
Generate files and observe their changes:

```
$ pingsee
```

##Grammatical Details
* [Ping Code](https://github.com/zxylvlp/PingPHP/tree/master/test/test)
* [Generated PHP Code](https://github.com/zxylvlp/PingPHP/tree/master/test/dest/test)

##CodeSample

Input file: part of typeHinting.ping

```
''''''
class MyClass:

    public test(otherclass:OtherClass):
        echo otherclass.var
    
    public test_array(input_array:array):
        print_r(input_array)
    
    public test_interface(iterator:Traversable):
        echo get_class(iterator)
    
    public test_callable(callback:callable, data):
        call_user_func(callback, data)
    
myclass = new MyClass()

```

Output file: part of typeHinting.php

```
<?php
class MyClass { 
    
    public function test(OtherClass $otherclass) { 
        echo $otherclass->var; 
    }
    
    public function test_array(array $input_array) { 
        print_r($input_array); 
    }
    
    public function test_interface(Traversable $iterator) { 
        echo get_class($iterator); 
    }
    
    
    public function test_callable(callable $callback, $data) { 
        call_user_func($callback, $data); 
    }
}

$myclass = new MyClass(); 
```

##Related

* Vim Syntax highlighting plugin: [Vim-PingPHP](https://github.com/PingPHP/Vim-PingPHP)
* Sublime Text Syntax highlighting plugin: (Temporarily not supported)

##Author

* [Weibo http://weibo.com/zxylvlp](http://weibo.com/zxylvlp)

* [Mail 937141576@qq.com](mailto:937141576@qq.com)

##License

Copyright (c) 2015 zxylvlp

[MIT](https://github.com/zxylvlp/PingPHP/blob/master/LICENSE)
