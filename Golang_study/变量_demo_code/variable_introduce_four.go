/*
匿名变量
我们在使用传统的强类型语言编程时，经常会出现这种情况，即在调用函数时为了获取一个 值，
却因为该函数返回多个值而不得不定义一堆没用的变量。
在Go中这种情况可以通过结合使 用多重返回和匿名变量来避免这种丑陋的写法，让代码看起来更加优雅。
 */


 //假设GetName()函数的定义如下，它返回3个值，分别为firstName、lastName和 nickName：
package main

import "fmt"

func GetName()(firstName, lastName, nickName string) {
	return "May", "Chan", "Chibi Maruko"}

func main(){
	_,name,liyanliang:=GetName()
	//运行结果 Chibi Maruko
	fmt.Println(liyanliang,name)
}


