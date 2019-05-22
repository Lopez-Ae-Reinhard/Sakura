### TCP传输
    三次握手和四次挥手

### 套接字编程

#### 流式套接字

`socket --> bind -->listen --> accept --> recv/send --> close`
    
`socket --> connect --> send/recv --> close`
    
#### 数据报套接字

`socket --> bind --> recvfrom/sendto --> close`
    
`socket --> sendto/recvfrom --> close`
    
### 套接字属性 
`getpeername() fileno() setsockopt()`