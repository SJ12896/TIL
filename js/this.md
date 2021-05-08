## this

- 함수 호출 맥락을 의미.

1. 함수의 호출

- 함수 안에서 this는 window. func앞에 window가 생략되어있는 것과 같다.(window.func() { ~ })

```javascript
function func() {
    if (window === this ){
        console.log("window === this")
    }
}
```

2. 메소드의 호출

- o에 속해 있을 때는 this가 o를 가리킨다.

```javascript
var o = {
    func : function () {
        if (o === this) {
            console.log("o === this")
        }
    }
}
```

---

- [What's the difference between a method and a function?](https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function)
- 함수 : 이름으로 호출할 수 있는 코드조각. 조작하기 위해 data를 보낼 수 있다.(파라미터) 그리고 선택적으로 data를 return한다. 
- 메소드 : 이름으로 호출되는 코드조각인데 객체와 연관되어 있다. 함수와 거의 비슷하지만 두 가지면에서 다르다. 메소드는 객체가 호출되면 암묵적으로 전달된다(?). 메소드는 클래스 안에 포함된 data를 조작할 수 있다.  

---

3. 생성자와 this

```javascript
var funcThis = null;

function Func() {
    funcThis = this;
}

var o1 = Func();
if (funcThis === window) {
    console.log('window')
}

var o2 = new Func();
if (funcThis === o2) {
    console.log('o2')
}
```

