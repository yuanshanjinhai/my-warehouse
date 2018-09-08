# my-warehouse
这是我原创的框架，分享给大家(This is my original framework. I want to share it with you. )

Chinese:

my_data_driver_1：

这是一个数据驱动的UI框架，用于操作126邮箱，数据写在Excel里。

guolin_hybrid_driver_1：

这是一个混合驱动的UI框架，用于操作126邮箱，关键字和数据都写在Excel里，用户可通过用例的随意组合来操作126邮箱的任何功能，执行结果会写入到用例Excel里以及日志里。
当然，他也可以用来操作其他市面上主流的邮箱系统，如搜狐闪邮、QQ邮箱等。
我在里面写了一个中文的详细说明文档。

my interface_1：

这是一个混合驱动的接口框架，他的用例文档是一个Excel，我们可以把传给服务器的json串里的值依次写到用例里，程序会根据这些值拼出json串，所以，这个框架就只适合与json串比较规整的接口，如果你的json串里有嵌套，则不适用于它。
同时，测试结果也会写到用例Excel里以及日志里。

my interface_2(more process)：

这同样是一个混合驱动的接口框架，也是这个几个里面最复杂的一个，它的用例仍然是Excel，用户需要在用例里写好传给服务器的json串，程序会的服务器的返回json串进行各种判断，并把结果写到用例Excel以及各种日志里。
我在这个套代码里写了详细的中文注释。

希望我的分享可以帮到大家



English:

My_data_driver_1:

This is a data driven UI framework for manipulating 126 mailboxes and data written in Excel.

Guolin_hybrid_driver_1: 

This is a hybrid driver UI framework for manipulating 126 mailboxes. The keywords and data are written in Excel. Users can manipulate any function of 126 mailboxes by arbitrary combination of use cases. The execution results are written in Excel and log.
Of course, he can also be used to operate other mainstream mailbox systems on the market, such as Sohu flash mail, QQ mailbox, etc.
I wrote a detailed description of Chinese in it. 

My interface_1:

This is a hybrid driver interface framework. Its use case document is an Excel. We can write the values in the JSON string passed to the server into the use case in turn. The program will spell out the JSON string according to these values. So this framework is only suitable for the interface that is more regular with the JSON string. If your JSON string is nested, it is not Apply to it.            At the same time, the test results will be written in use case Excel and log.

My interface_2 (more process):

This is also a hybrid driver interface framework, but also one of the most complex of these, its use case is still Excel, users need to write a good use case to the server's JSON string, the program will return the server's JSON string for various judgments, and write the results to the use case Excel and various logs. I wrote detailed Chinese annotations in this set of code. 

I hope my sharing can help you. 
