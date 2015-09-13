<?php
namespace A\B\C; 

/** 这个函数是 A\B\C\fopen **/
function fopen() { 
    /**...**/
    $f = \fopen(''); // 调用全局的fopen函数
    return $f; 
}
