#PingPHP 
[![Build Status](https://travis-ci.org/zxylvlp/PingPHP.svg?branch=master)](https://travis-ci.org/zxylvlp/PingPHP)
###A PHP code generator which use Python Like grammar



##简介

这本质上是一个PHP代码生成器，类似于CoffeeScript。而本代码库和它之间有一个很重要区别。这个库是为了高效的编写类似Python语法的代码，并且生成的PHP与手工写的代码并无差异，可以提高生产效率，并且生成的代码易于维护。而CoffeeScript的目的完全就是维护CoffeeScript,增加了很多语法糖，提升了效率却失去了生成后代码的可读性。对于广大PHPer这样多的语法糖恐怕是很难接受的，而且为了工作需要，配合其他的开发人员，直接维护Ping代码会影响沟通。

这个Ping是我老婆的名字，写这个库的目的之一也是为了提升工作效率帮助大家可以多陪陪自己的家人和朋友。

这个库选了Python这个语言来写，主要是为了快速开发，以前没有用过，用了很多quick and dirty的方式做出一个小样来。

目前它还在最初阶段的开发中，very buggy。每天可能会抽出一个小时左右的时间来写，时间不是很充裕，但是我会坚持下来。

##使用方法

自己按照需求定义配置文件PingPHP.conf.json，里面的参数应该大家都懂，linux查文件的通配符表示。下面的例子中输出的文件是dest/test/\*\*/\*.ping

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

然后再shell中运行

```
python main.py
```

##结果示例

输入文件asdf.ping

```
class MyClass extends MyBaseClass implements MyIterfaceA, MyIterfaceB:#line1

	a#line2
	b#line2
	
	'''
	我的多行注释
	'''

	#我的单行注释

	<?php
	public $c = 1;
	?>
	public static myMethod():#line2

		a = 2#line2

		this.a = 1#line2
	
		return a#line2

interface MyIterfaceA extends MyIterfaceB:#line2

	public static myMethod()
```

输出文件asdf.php

```
<?php
class MyClass extends MyBaseClass implements MyIterfaceA, MyIterfaceB {//line1
        
        public $a;//line2
        public $b;//line2
        
        /**
		我的多行注释
		**/
        
        //我的单行注释
        
        public $c = 1;
	
        public static function myMethod() {//line2
                
                $a = 2;//line2
                
                $this->a = 1;//line2
                
                return;//line2
        }
}

interface MyIterfaceA extends MyIterfaceB {//line2
        
        public static function myMethod();
}

```
