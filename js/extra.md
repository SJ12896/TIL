- 더하기에 피연산자로 문자형 데이터가 한 개라도 포함되어 있으면 다른 피연산자의 데이터는 자동으로 문자형 데이터로 변환되고 문자 결합이 이루어져 하나의 문자형 데이터를 반환한다.
- 증감 연산자 : 변수의 어느 위치에 오는가에 따라 결과값이 달라진다.

```javascript
let num1 = 20;
let result;

result = num1++;
// result = 20, num1 = 21
console.log(result, num1)

result = ++num1;
// result = 22, num1 = 22,
console.log(result, num1)
```

