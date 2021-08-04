## 모던 자바스크립트 핵심 가이드

### 0. 변수

- 값을 재할당해야 하는 상황이 아니라면 항상 const를 쓰자. 나중에 코드를 디버그하지 않고 실수로 재할당하려 할 때 오류가 발생하므로 잘못된 변수를 참조했다는 사실을 알 수 있다.
- 원시 자료형 : 객체가 아닌 자료형, 메서드 가지지 않는다 / string, number, boolean, null, undefined, symbol(고유하고 변경할 수 없는 값?)

---

#### 0-1. 객체

- 객체 : 여러 속성의 모음 저장. 함수도 저장 가능.

```javascript
const car = {
    drive: function() {
        console.log("wroom wroom");
    }
};
```

- 변수에 저장된 키를 통해 객체 속성에 접근하려면 대괄호 표기법 사용

```javascript
const cars = {
    ferrari: "california",
};

const key = "ferrari";
console.log(cars[key]) // cars.key는 undefined가 나온다.
```

- 객체의 복사본 만들기 : Object.assign() 사용. 이렇게 하면 car를 업데이트해도 secondCar는 변화하지 않는다. 첫 인수는 복사본에 해당하는 객체, 두 번째 인수는 원본에 해당

```javascript
const secondCar = Object.assign({}, car);
```

---

- 배열 : unshift() - 배열 시작에 새 값 추가 / shift() - 배열 시작에 한 값 제거
- typeof로 객체, 배열, null을 확인하면 전부 object라고 나온다. null은 원시 자료형이라고 했지만,,,

- 원시 자료형이 함수에 전달될 때 참조가 아닌 값의 형태로 전달된다. 값 변경 사항이 전역적으로 반영되지 않는다. 원시 자료형이 아닌 객체나 배열을 함수에 전달할 때는 참조로 전달된다. 값 변경 사항이 원래 객체에 반영된다.

---

#### 0-2. this 키워드

```javascript
const myCar = {
    color: 'red',
    logColor: function() {
        console.log(this.color);
    },
};

function logThis() {
    console.log(this);
}

const unboundGetColor = myCar.logColor; // undefined
const boundGetColor = unboundGetColor.bind(myCar); // red
```

- 위의 예에서는 this 키워드가 myCar 개체를 참조한다. 
- 아래 예에서는 전역 범위에서 호출했으므로 this값은 window 객체를 참조한다.
- `스트릭트 모드`로 설정하면 실수로 window 객체를 참조하는 것을 방지할 수 있다. 자바스크립트 파일 시작 부분에 `use strict;`를 삽입하면 된다. 엄격한 규칙에서 전역 객체 값을 window 대신 undefined로 설정하는 규칙이 있다.
- this 값을 수동으로 설정하고자 할 때는 `.bind()`를 사용할 수 있다. 3번 예에서 첫번재는 winodw를 참조하기 때문에 undefined지만 .bind()를 사용했을 때는 this 키워드가 괄호 안의 객체, myCar를 참조했다.
- this키워드 값을 설정하는 다른 방법은 `.call()`과 `.apply()`가 있다. 두 메서드 모두 주어진 this로 함수를 호출하지만 받아들이는 인수가 다르다. call은 인수 목록, apply는 하나의 인수 배열을 받는다. 필요한 인수의 수를 모르거나 알 필요 없을 때 apply를 주로 사용한다. call은 인수를 개별적으로 전달해야 해서 사용할 수 없다.

```javascript
function Car(maker, color) {
    this.carMaker = maker;
    this.carColor = color;
}

// .call()
function MyCar(maker, color) {
    Car.call(this, maker, color); // MyCar 객체를 전달.
    this.age = 5;
}

const myNewCar = new MyCar('bmw', 'red');
console.log(myNewCar.carMaker); // bmw
console.log(myNewCar.carColor); // red

// .apply()
function MyCar(maker, color) {
    Car.apply(this, [maker, color]); // 
    this.age = 5;
}

const myNewCar = new MyCar('bmw', 'red');
console.log(myNewCar.carMaker); // bmw
console.log(myNewCar.carColor); // red

// 전달하는 인수 수 관계없을 때 .apply()
const ourFunction = function(item, method, args) {
    method.apply(args);
}
ourFunction(item, method, ['argument1', 'argument2']);
ourFunction(item, method, ['argument1', 'argument2', 'argument3']);
```

---

### 1. var, let, const

- var, let, const의 차이
  - var : 함수 스코프에 종속된다. for 루프 내에서 선언하면 밖에서도 사용 가능. if 문안에서 값 변경하면 바깥에서도 값이 변경된다.
  - let : 블록 스코프로 종속된다. 
  - const: 블록 스코프로 종속된다. 재할당을 통해 값이 변경될 수 없고 다시 선언될 수도 없다. 객체가 담긴 상황이라면 변수 전체를 재할당하는 것이 아니라 그 속성 중 하나만 재할당하는 것이므로 문제 없다. 다만 `Object.freeze(객체명);` 을 사용하면 객체를 고정할 수 있지만 값을 변경하려고 시도해도 에러가 발생하지는 않는다.
- TDZ (temporal dead zone) : 일시적 비활성 구역. var는 정의되기 전에 접근할 수 있지만 값에는 접근할 수 없다. let과 const는 정의되기 전에 접근할 수 없다. var, let, const 모두 호이스팅hoisting의 대상이 된다. 코드가 실행되기 전에 처리되고 해당 스코프 상단으로 올라간다. var는 정의되기 전에 접근할 수 있고 undefined값을 가진다. let은 변수가 선언될 때 까지 일시적으로 비활성 구역, TDZ에 있게 된다. 초기화 전 변수에 접근하면 오류가 발생한다. 오류가 발생하는 편이 디버깅이 쉽다.

---

### 2. 화살표 함수

```javascript
// 일반적 함수 선언
const greeting = function(name) {
    return "hello" + name;
};

// 화살표 함수 문법
var greeting = (name) => {
    return `hello ${name}`;
};

// 매개변수가 하나만 있으면 괄호를 생략할 수 있다.
var greeting = name => {
    return `hello ${name}`;
};

// 매개변수가 없으면 빈 괄호를 쓴다.
var greeting = () => {
    return "hello";
};

// 명시적 반환을 생략하고 암시적 반환을 할 수 있다.
const greeting = name => `hello ${name}`;
```



- 객체 리터럴 암시적 반환
- runner는 배열의 현재 원소, i는 배열의 인덱스. 배열 각 원소에 대해 name, race, place 속성을 포함하는 객체를 results에 추가한다. 

```javascript
const race = "100m dash";
const runners = ["Usain Bolt", "Justin Gatlin", "Asafa Powell"];

const results = 
      runners.map((runner, i) => ({name: runner, race, place: i + 1}));

console.log(results);
// [{name: "Usain Bolt", race: "100m dash", place: 1}]
```



- 화살표 함수에서 this키워드는 일반 함수와 다르게 동작한다. 상위 스코프에서 상속된다.
- 이 코드에서 첫 this는 box에 할당되었지만 setTimeout내부의 두 번째 this는 Window객체로 설정되어 오류가 발생한다.

```javascript
const box = document.querySelector(".box");
box.addEventListener("click", function() {
    this.classList.toggle("opening");
    setTimeout(function() {
        this.classList.toggle("opening")l
    }, 500);
});
```

- 화살표 함수가 부모 스코프에서 this값을 상속하는 것을 인지하면 여기서 this는 const box로 설정된다.

```javascript
setTimeout(() => {
    this.classList.toggle("opening");
}, 500);
```



- 그러나 화살표 함수 사용하면 문제가 될 수 있는 상황도 있다. 여기서 this는 Window를 가리킨다.

```javascript
const button = document.querySelector("btn");
button.addEventListener("click", () => {
    this.classList.toggle("on");
})

const person2 = {
    age: 10,
    grow: () => {
        this.age++;
        console.log(this.age);
    },
};
```



- 화살표함수와 일반 함수 또 다른 차이점은 arguments 객체 접근 방식이다. arguments는 함수 내부에서 접근할 수 있는 배열 객체로 해당 함수에 전달된 인수 값을 담고 있다. this와 비슷하게 화살표 함수에서 arguments 객체는 부모 스코프 값을 상속한다. arguments는 변수 이름이 아니라 키워드다. 

```javascript
function example() {
    console.log(arguments[0]);
}

example(1, 2, 3); // 1

const showWinner = () => {
    const winner = arguments[0];
    console.log(`${winner} was the winner`);
};

showWinner("Usain Bolt", "Justin Galtin", "Asafa Powell"); 
// arguments is not defined

// 화살표 함수로 arguments에 접근하는 예
const showWinner = (...args) => {
    const winner = args[0];
    console.log(`${winner} was the winner`);
}
```

---

### 3. 함수 기본값 인수

- ES6에서 달라졌다. 기존엔 첫 번째 인수를 기본값으로 바꾸기 위해서 인수로 undefined 값을 전달해야 했다. 

```javascript
// ES6
function calculatePrice(total, tax = 0.1, tip = 0.05) {
    return total + (total * tax) + (total * tip);
}
```

- 매개변수를 아예 전달하지 않으려면 undefined를 써야했지만 디스트럭처링을 통해 코드를 다음과 같이 바꿔 쓸 수 있다. 함수 인수를 객체로 만들어 호출하면 매개변수가 주어진 키에 맞춰 입력되어 순서를 걱정할 필요 없다. 인수 객체를 빈 객체로 기본 설정하지 않고 선언하면 오류가 발생한다. {}를 추가해야 인수를 기본적으로 객체로 설정한다. 인수로 무엇을 전달했는지에 상관없이 세 기본 속성을 가진 객체로 기본 설정된다.

```javascript
function calculatePrice({total = 0, tax = 0.1, tip = 0.05,} = {}) {
    return total + (total * tax) + (total * tip);
}

const bill = calculatePrice({tip: 0.15, total: 150});
calculatePrice({}); // 0
calculatePrice(); // 0
calculatePrice(undefined); // 0
```

---

### 4. 템플릿 리터럴

- HTML 프래그먼트 등에 사용할 여러 줄로 이뤄진 문자열은 전체를 백틱으로 감싸면 된다.

```javascript
const content = `hello,
my name is Alberto
how are you?`;
```

- 중첩 템플릿

```javascript
const artist = {
    name: 'sj',
    age: 20,
};

const text = `
	<div>
		<p> ${artist.name} is ${artist.age} years old ${artist.song ? `and wrote the song ${artist.song}` : ''} 
		</p>
	</div> 
`;

console.log(text); // <div> <p> sj is 20 years old  </p> </div> 
```

- 템플릿 리터럴에 함수를 전달할 수도 있다.
- 함수를 태그tag하여 템플릿 리터럴을 실행하면 템플릿 내부에 있는 모든 항목이 태그된 함수의 인수로 제공된다. 함수 이름을 가져다 실행할 템플릿 앞에 쓰기만 하면 된다. strings는 let sentence문의 전체 문자열 중 템플릿 리터럴 변수를 제외한 문자열들이 담긴 배열로 설정되고, 템플릿 리터럴 변수들이 나머지 인수가 된다. strings 배열 각 원소는 템플릿 리터럴에 포함된 변수들을 구분자로 삼아 문자열을 나눈 결과다. 

```javascript
let person = 'alberto';
let age = 25;

function myTag(strings, personName, personAge) {
    // strings: ["That", " is a ", "!"]
    let str = strings[1]; 
    let ageStr;
    
    personAge > 50 ? ageStr = "grandpa" : ageStr = "youngster";
    
    return personName + Str + ageStr;
}

let sentence = myTag`That ${person} is a ${age}!`;
console.log(sentence) // alberto is a youngster
```

---

### 5. 문자열 메서드

- indexOf() : 문자열에서 매개변수 값이 처음 나타나는 위치 반환
- slice(start, end) : 문자열 지정된 부분을 새 문자열로 반환
- toUpperCase() : 문자열 내 모든 문자를 대문자로 바꾼다. / toLowerCase()
-  ES6에서 도입된 4가지 새로운 문자열 메서드
  - startsWith() :  매개변수로 받은 값으로 문자열이 시작하는지 확인 (대소문자 구별), 매개변수 숫자를 추가로 전달하면 검사 시작점을 지정할 수 있다.
  - endsWith() : 추가 매개변수로 문자열의 얼마만큼만을 확인할지 길이를 전달할 수 있다.
  - includes()
  - repeat() : 문자열을 반복하며 횟수를 인수로 받는다.

---

### 6. 디스트럭처링

- 디스트럭처링 할당 문법은 배열의 값 또는 객체 속성을 풀어서 별개의 변수로 쓸 수 있게 해주는 자바스크립트 표현식
- 객체 디스트럭처링 : person이 가진 속성에 접근함과 동시에 해당 속성 이름으로 변수 선언 가능

```javascript
// 과거
var person = {
    first: "alberto",
    last: "montalesi",
}

var first = person.first;
var second = person.last;

// ES6
const {first, last} = person;
// 변수 이름을 바꿀 수도 있다.
const {first: fs} = person;
console.log(fs) // alberto
```



- 배열 디스트럭처링 : 생성하려는 변수 수가 배열 원소보다 적다면 앞에서부터 순서대로 할당된다. 나머지 모든 값을 얻고 싶다면 `레스트 연산자(...)`를 사용하면 된다.

```javascript
const person = ["alberto", "monalesi", 25];
const [name, surname, age] = person;

const person = ["alberto", "monalesi", "pizza", "ice cream", "cheese cake"];
const [name, surname, ...food] = person;
console.log(food); // ["pizza", "ice cream", "cheese cake"]
```



- 디스트럭처링을 이용하여 변수 교체하기

```javascript
let hungry  = "yes";
let full = "no";

[hungry, full] = [full, hungry];
cosnole.log(hungry, full); // no, yes
```

---

### 7. 루프

```javascript
var fruits = ['mango', 'kiwi', 'watermelon'];

// 일반 반복문
for (var i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// for of (값 목록(원소 목록) 반환)
for (var fruit of fruits) {
    console.log(fruit);
}

// for in : 순서 없이 객체의 모든 열거 가능한 속성 반복 (key 목록(속성 목록) 반환)
const car = {
    maker: "BMW",
    color: "red",
    year: "2010",
};

for (const prop in car) {
    console.log(prop, car[prop]);
}
```

- 객체 반복은 Object.keys()로 모든 키를 가져오거나 ES6의 새로운 함수인 Object.entries()를 사용해 모든 키/값 쌍을 가져와 반복할 수 있다.

---

### 8. 배열 메서드

- Array.from() : 배열처럼 보이지만 배열이 아닌 객체를 받아 실제 배열로 변환

```html
<div class="fruits">
    <p> Apple </p>
    <p> Banana </p>
    <p> Orange </p>
</div>

<script>
    const fruits = document.querySelectorAll(".fruits p");
    const fruitArray = Array.from(fruits);
    console.log(fruitArray); // 세 가지 p객체가 array로 반환된다.
    const fruitNames = fruitArray.map(fruit => fruit.textContent); // p의 textContent 속성만 가져온다.
    console.log(fruitNames);
    
    // 더 간단하게
    const fruitArray = Array.from(fruits, fruit => {
        return fruit.textContent;
    });
</script>
```



- Array.of() : 전달받은 모든 인수로 배열 생성

```javascript
const digits = Array.of(1, 2, 3, 4, 5);
console.log(digits); // [1, 2, 3, 4, 5]
```



- Array.find() : 제공된 테스트 함수를 충족하는 배열의 첫 원소 반환. 없으면 undefined

```javascript
const array = [1, 2, 3, 4, 5];

let found = array.find(e => e > 3);
console.log(found); // 4
```



- Array.findIndex() : 조건과 일치하는 첫 번째 원소의 인덱스 반환
- Array.some(), Array.every() : 조건과 일치하는 원소 있는지 검색하고 첫 번째 일치하는 원소 찾으면 바로 중지 / 모든 원소가 주어진 조건과 일치하는지 여부 확인 / true, false 반환

---

### 9. 스프레드 연산자와 레스트 매개변수

- 스프레드 문법 : 0개 이상의 인수(함수 호출용) 또는 원소(배열 리터럴용)가 예상되는 위치에서 배열 표현식 또는 문자열과 같은 이터러블 항목을 확장하거나 0개 이상의 키/값 쌍(객체 리터럴용)이 예상되는 위치에서 객체 표현식 확장
- 배열 결합 뿐 아니라 배열 복사에 유용

```javascript
// 이전 버전
const veggie = ["tomato", "cucumber", "beans"];
const newVeggie = [].concat(veggie);

// 스프레드 문법
const newVeggie = [...veggie];
```



- 함수와 스프레드 연산자

```javascript
// 기존 방식
function doStuff(x, y, z) {
    console.log(x + y + z);
}
var args = [0, 1, 2];

doStuff.apply(null, args);

// 스프레드 문법
doStuff(...args);
```



- 객체에도 스프레드 연산자가 적용된다.

---

### 10. 객체 리터럴의 업그레이드

```javascript
const name = "alberto";
const surname = "montalesi";
const age = 25;
const nationality = "italian";

// 변수들의 이름이 코드 내 속성과 동일하므로 두 번 표기하지 않아도 된다.
const person = {
    name,
    surname,
    age,
    nationality,
}

// 객체에 함수 추가. function 키워드가 없어도 된다. + 화살표 함수
const person = {
    name: "alberto",
    greet() {
        console.log("hello");
    }
    greet2: () => console.log("Hello2");
};

// 객체 속성 동적으로 정의
const name = "myname";
const person = {
    [name]: "alberto",
};
console.log(person.myname); // alberto
```

---

### 11. 심벌

- ES6에서 추가된 원시 자료형
- 심벌은 항상 고유하며 객체 속성 식별자로 사용할 수 있다.

```javascript
const me = Symbol("alberto");
console.log(me); // Symbol(alberto)

// 속성이 겹칠 때 
const office = {
    "Tom" : "CEO",
    "Mark" : "CTO",
    "Mark" : "CIO",
};

for (person in office) {
    console.log(person);
}

// 심벌을 사용하면 열거 가능하지 않아 for in 으로 반복 시 undefined가 나온다. 대신 객체 속성 배열을 얻기 위해서는 Object.getOwnPropertySymbols()를 사용
const office = {
   [Symbol("Tom")]: "CEO",
   [Symbol("Mark")]: "CTO",
   [Symbol("Mark")]: "CIO",
};

const symbols = Object.getOwnPropertySymbols(office);
console.log(symbols); // 0: Symbol(Tom), ..., length: 3
const value = symbols.map(symbol => office[symbol]);
console.log(value); // 0: "CEO", ..., length: 3

```

- 같은 값으로 심벌을 생성해도 각 심벌은 항상 고유하므로 다른 심벌과 겹치치 않는다.

---

### 12. 클래스

- 클래스 : 일차적으로 자바스크립트 기존 프로토타입 기반 상속에 대한 문법적 설탕syntatic sugar이다. 클래스 문법이 자바스크립트에 새로운 객체 지향 상속 모델을 도입하는 것은 아니다. 
- Person의 프로토타입에 새 메서드를 추가해 Person 객체 인스턴스들이 접근할 수 있게 만들었다. 

```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    console.log("Hello, my name is" + this.name);
}

const alberto = new Person("alberto", 26);
alberto.greet(); // Hello, my name is alberto
```



- 클래스를 만드는 방법 두 가지 : 클래스 선언, 클래스 표현식 / 호이스팅 되지 않아 접근하기 전 선언하지 않으면 ReferenceError발생

```javascript
// 클래스 선언
class Person {
    
}

// 클래스 표현식
const person = class Person {
    
};


// 생성자 메서드를 제외하면 프로토타입 방식과 비슷하다. 생성자는 하나만 추가해야 한다.
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        cosnole.log(`Hi, my name is ${this.name} and I'm ${this.age} years old`);
    }
    farewell() {
        console.log("goodbye friend");
    }
}

const alberto = new Person("Alberto", 26);
alberto.greet(); 
alberto.farewell();
```



- greet(), farewell() 메서드는 Person 클래스의 모든 인스턴스에서 접근 가능하지만 클래스의 인스턴스가 아닌 클래스 자체에서 접근할 수 있는 정적 메서드는 다음과 같다.

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    static info() {
        console.log("Hi");
    }
 
const alberto = new Person("Alberto", 26);
alberto.info(); // TypeError
Person.info(); // Hi
```



- set과 get

```javascript
const Person{
    constructor(name, surname) {
        this.name = name;
        this.surname = surname;
        this.nickname = "";
    }
    set nicknames(value) {
        this.nickname = value;
    }
    get nicknames() {
        console.log(this.nickname);
    }
}

const alberto = new Person("Alberto", 26);
alberto.nicknames = "albi"; // 세터 호출
alberto.nicknames; // 게터 호출
```



- 클래스 상속 : extends 키워드 사용. 다만 새로운 클래스에서 this를 사용하기 전에 super()를 호출해야 한다. 

```javascript
class Adult extends Person {
    constructor(name, age, work) {
        super(name, age); // Person을 다시 선언하고 초기화할 필요 없다.
        this.work = work;
    }
}
```



- 배열 확장하기. 첫 값은 교실 이름, 나머지는 학생 이름과 학생 점수를 나타내는 Classroom이라는 클래스

```javascript
class Classroom extends Array {
    // 레스트 연산자를 사용해 가변 인수로 입력받은 학생들 정보를 배열 형태로 students에 저장한다. 
    constructor(name, ...students) {
        // 스프레드 연산자를 사용해 배열 원소를 풀어헤쳐 생성자를 호출한다. 스프레드 연산자로 풀어헤치지 않으면 학생들 정보가 있는 배열 자체를 원소로 가지게 된다.
        super(...students);
        this.name = name;
    }
    add(student) {
        this.push(student);
    }
}

const myClass = new Classroom('1A',
      {name: "Tim", mark: 6},
      {name: "Tom", mark: 3},
      {name: "Jim", mark: 8},)

myClass.add({name: "Timmy", mark: 7});
myClass[3]; // {name: "Timmy", ~ }

for (const student of myClass) {
    console.log(student);
}
// {name: "Tim", ~ }, ...
```

---

### 13. 프로미스

- 자바스크립트는 동기적으로 작동한다. 즉, 각 코드 블록이 이전 코드 블록 이후에 실행된다.
- fetch를 사용해서 어떤 url에서 데이터를 가져온다고 가정할 때 동기 코드라면 fetch작업 완료 후 다음 행이 호출될거라고 생각하지만 실제로는 fetch 직후 다음 행의 두 console.log가 실행되므로 data를 undefined가 출력된다. 
- fetch는 비동기적으로 수행되기 때문이다. fetch가 완료될 때까지 코드 실행을 중지하는 게 아니라 계속해서 다음 행을 실행한다. 이 문제를 해결하기 위해 콜백 또는 프로미스를 사용하면 fetch가 무언가를 반환하는 시점까지 기다리게 할 수 있다.

```javascript
const data = fetch('your-api-url-goes-here');
cosole.log('Finished');
console.log(data);
```



- 콜백 지옥 : 비동기 코드를 동기식으로 작동하는 것처럼 하기 위해 콜백으로 여러 코드 블록을 차례로 연결해 작성할 때 발생하는 상황을 콜백 지옥 이라고 한다.
- 프로미스 : 비동기 작업의 최종 성공 또는 실패를 나타내는 객체

```javascript
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
    	resolve("The value we get from the promise");
    }, 2000);
});

myPromise
   	.then(data => {
        console.log(data);
    })
	.catch(err => {
    console.error(err);
});
```



- 프로미스 체이닝 : 성공, 실패 여부와 무관하게 이전 프로미스에서 반환된 것을 후속 프로미스 기반으로 사용하여 게속 체이닝할 수 있다.
- Promise.resolve()와 Promise.reject()는 자동으로(즉시) 성공하거나 실패하는 프로미스를 생성한다. 
- Promise.all()은 모든 프로미스가 성공할 경우에만 성공하는 하나의 프로미스를 반환. 프로미스 중 하나가 실패하면 다른 프로미스가 성공해도 해당 실패에서 발생한 오류가 반환

```javascript
const promise1 = new Promise((resolve, reject) => {
    setTimeout(resolve, 500, 'first value');
});
const promise2 = new Promise((resolve, reject) => {
    setTimeout(resolve, 1000, 'second value');
});

Promise
	.all([promise1, promise2])
	.then(data => {
    	const [promise1data, promise2data] = data;
    	console.log(promise1data, promise2data)
});
// 1000ms 후 first value second value
```

- Promise.race()는 이터러블에 포함된 프로미스들 중 가장 먼저 성공이나 실패한 결과를 반환한다. 비어있는 이터러블을 전달하면 영원히 보류된 상태로 남아 있는다.

---

### 14. 제너레이터

- 원하는 만큼 코드 실행을 시작하거나 중지할 수 있는 함수. 중지된 제너레이터 함수를 다시 시작할 때 데이터를 추가로 전달하면서 재시작할 수 있다. 

```javascript
function* fruitList() {
    yield 'Banana';
    yield 'Apple';
    yield 'Orange';
}

const fruits = fruitList();
fruits.next();
// {value: "Banana", done: false}
// next로 마지막까지 출력했다면 그 다음 next에서는
// {value: undefined, done: true}
```



- for of 루프를 사용하면 제너레이터에 대해 반복하고 각 루프에서 콘텐츠를 반환(yield)할 수 있다.

```javascript
const fruitList = ['Banana', 'Apple', 'Orange', 'Melon', 'Cherry', 'Mango'];

function* loop(arr) {
    for (const item of arr) {
        yield `I like to eat ${item}s`;
    }
}

const fruitGenerator = loop(fruitList);
fruitGenerator.next();
// {value: "I ~ Bananas", done: false}
fruitGenerator.next().value;
// "I ~ Apples"
```



- .return() : 주어진 값을 반환하고 제너레이터 종료
- . throw()로 오류 잡기 : .thorw를 호출했을 대 오류를 반환했고 실행할 yield가 남아있는데도 종료되었다.

- 제너레이터를 프로미스와 함께 사용하면 마치 동기 코드처럼 느껴지게 비동기 코드를 작성할 수 있다. 프로미스가 완료될 때까지 기다렸다가 완료될 때 반환된 값을 .next() 호출 시점에 제너레이터로 다시 전달한다.

```javascript
const myPromise = () => new Promise((resolve) => {
    resolve("our value is...");
})

function* gen() {
    let result = "";
    yield myPromise().then(data => {result = data});
    yield result + '2';
}

const asyncFunc = gen();
const val1 = asyncFunc.next();
console.log(val1);
// {value: Promise, done: false}
// 프로미스 완료되길 기다린 후 .next()호출
va1l.value.then(() => {
    console.log(asyncFunc.next());
});
// {value: "our value is... 2", done: false}
```

---

### 15. 프록시

- 프록시Proxy 객체는 기본 작업에 대해 사용자 지정 동작을 추가로 정의하는데 사용한다.

- 프록시 생성

  - var x = new Proxy(target, handler);

  - target은 객체, 함수, 다른 프록시 등 무엇이든 가능
  - handler는 작업이 수행될 때 프록시 동작을 정의하는 객체

```javascript
const dog = {breed: "German Shephard", age: 5};
const dogProxy = new Proxy(dog, {
    get(target, breed) {
        return target[breed].toUpperCase();
    },
    set(target, breed, value) {
        console.log("changing breed to...");
        target[breed] = value;
    },
});

console.log(dogProxy.breed); // GERMAN SHEPHARD
console.log(dogProxy.breed = "Labrador");
// changing breed to...
// "Larbrador"
console.log(dogProxy.breed);
// "LARBRADOR"
```



- 프록시 활용 : user객체의 age 속성을 설정할 때 마다 validateAge함수가 실행된다. 

```javascript
const validateAge = {
    set: function(object, property, value) {
        if (property === 'age') {
            if (value < 10) {
                throw new Error('you are too young!');
            }
        else {
            object[property] = value;
            return true;
        }
        }
    }
};

const user = new Proxy({}, validateAge);
user.age = 17; // you are too young!
```



- 프록시는 동일한 내용의 게터와 세터를 많은 속성에 적용해야 할 때 매우 유용하다. 프록시를 사용하면 하나의 게터와 하나의 세터만 정의하면 된다. 먼저 프록시를 사용하지 않는 예시다. 여기서 _name, _age의 _기호는 프라이빗 속성을 정의하는데 사용된다. 문법적으로 강제하지는 않지만 개발자가 프라이빗 속성을 빠르게 식별할 수 있다. 

```javascript
const dog = {
    _name: 'pup',
    _age: 7,
}

get name() {
    console.log(this._name);
}
get age() {
    console.log(this._age);
}
set name(newName) {
    this._name = newName;
    cosole.log(this._name);
}
set age(newAge) {
    this._age = newAge;
    console.log(this._age);
}

dog.name; // pup
dog.breed; // 존재하지 않는 속성에 접근 시 undefined
dog.name = "Max";

// 이런 형태로 함수가 작성됐다면 this.name은 세터를 다시 호출하므로 무한 루프가 발생한다. _를 사용해 방지할 수 있다. 물론 set name이 아닌 rename등으로 변경해도 된다.
// set name(newName) {
//  	this.name = newName;
//		}
```

- 프록시를 사용한 코드 : 하나의 게터와 세터로 모든 속성을 처리하는 handler를 만들었다. 게터는 해당 속성이 존재하면 출력하고 아니면 지정한 메세지를 출력한다. 

```javascript
const dog = {
    name: 'pup',
    age: 7,
};
const handler = {
    get: (target, property) => {
        property in target ? console.log(target[property]) : console.log('property not found');
    },
    set: (target, property, value) => {
        target[property] = value;
        console.log(target[property]);
    },
};

const dogProxy = new Proxy(dog, handler);

dogProxy.name = 'Max';
dogProxy.breed; // property not found
```

---

### 16. 세트, 위크셋, 맵, 위크맵

- 세트 : 어떠한 자료형 값이든 각 원소 고유하게 저장하는 객체
- keys(), entries(), values() : 키가 없기 때문에 셋 다 동일한 결과가 나온다.
- .next()나 for of 사용해서 반복

```javascript
const family = new Set();
family.add("Dad");
family.add("Dad"); // 한 번 더 추가되지 않고 동일하게 유지됨
family.size();
family.delete("Dad");
family.clear();

const iterator = family.values();
iterator.next();

for (const person of family) {
    console.log(person);
}

const myArray = ["dat", "mom", "mom", "daughter"]

// 배열 set으로 바꿔서 중복 제거
const set = new Set(myArray);

// set을 배열로 변환
const uniqueArray = Array.from(set);
```



- 위크셋weakset : 세트와 유사하지만 객체만 포함할 수 있음. 위크셋은 이터러블이 아니기 때문에 for of 루프를 사용할 수 없다. / weakset이 포함하는 객체가 가비지 컬렉터에 의해 삭제되면 해당 객체는 weakset에서도 자동으로 삭제된다.

```javascript
let dad = {name: "Daddy", age: 50};
let mom = {name: "Mommy", age: 50};

const family = new WeakSet([dad, mom]);

dad = null;
// 10초정도 기다린 후 console.log(family);를 하면 하나만 있다.
```



- 맵 : Set와 유사하지만 키/값 쌍

```javascript
const family = new Map();

family.set("Dad", 40);
family.set("Mom", 50);
family; // Map(2) {"Dad" => 40, "Mom" => 50}
family.size;

family.forEach((val, key) => console.log(key, val));
// Dad 40
// Mom 50

for (const [key, val] of family) {
    console.log(key, val);
}
// Dad 40
// Mom 50
```



- 위크맵 : 키/값 쌍 모음이지만 키는 객체여야 한다. 키로 사용된 객체 참조가 손실되어 가비지 컬렉터에 의해 수집되면 weakmap에서도 해당 키/값 쌍이 자동으로 제거된다. 열거가능하지 않아 원소 반복을 수행하는 것이 불가능하다. 

---

### 17. ES2016의 새로운 기능

- Array.prototype.includes() : 전달하는 첫 값은 검색할 원소, 두번째 값은 검색 시작할 인덱스. 음수 전달해서 끝에서 첫번째부터 찾을 수도 있다.
- 지수 연산자(**)

---

### 18. ES2017

- 문자열 패딩 : hello가 5글자기 때문에 지정한 숫자에서 빈 공간이 각각 1개, 4개 남는다. 공백만이 아니라 문자열이나 숫자를 덧붙이는 것도 가능하다.

```javascript
"hello".padStart(6); // " hello"
"hello".padEnd(10); // "hello     "

// 문자열 오른쪽 정렬 : 가장 긴 문자열을 찾아서 길이를 측정하고 그 길이를 기준으로 패딩 추가.
const strings = ["short", "medium length", "very long string"];
const longerString = strings.sort(str => str.length).map(str => str.length)[0];
strings.forEach(str => console.log(str.padStart(longerString)));
```



- Object.entries() : 키와 값을 모두 포함하는 배열의 배열 반환
- Object.values() : 모든 값이 담긴 배열 반환
- Object.getOwnPropertyDescriptors() : 객체가 소유한 모든 속성 설명자 반환. 속성의 value, writable, get, set, configurable, enumerable 등을 반환



- 후행 쉼표 : 사소한 문법 변경. 객체나 함수 작성 시 마지막 매개변수인지 여부 관계없이 각 매개변수 뒤에 쉼표 찍는 것이 허용된다.



- 자바스크립트는 기본적으로 웹 브라우저 위에서 단일 스레드로 동작하지만, HTML5 웹 워커 API 도입으로 백그라운드 스레드에서도 코드 실행이 가능해짐에 따라 멀티 스레드 환경을 지원하기 위해 공유 메모리 모델과 어토믹스가 도입되었다.
- 어토믹스 : 메모리가 공유되면 여러 스레드가 메모리에서 동일한 데이터를 읽고 쓸 수 있다. Atomics를 이용한 작업은 이런 환경에서도 정확하게 값을 읽고 쓸 수 있게 해준다. 또 Atomics를 이용한 작업은 다음 작업이 시작되기 전에 완료되고, 중단되지 않는 것이 보장된다. / 생성자가 아니며 모든 속성과 메서드는 정적이므로 new 연산자와 함께 사용하거나 함수 형태로 호출할 수 없다.
  - 메서드 : add / sub, and / or / xor, load / store
  - 범용 고정 길이 바이너리 데이터 버퍼를 표현하는 SharedArrayBuffer객체와 함께 사용된다.

```javascript
// .add() : 3개의 인수. 배열, 인덱스, 값을 받고 더하기 수행 전에 해당 인덱스에 존재하던 이전 값 반환

// sharedArrayBuffer를 생성
const buffer = new SharedArrayBuffer(16);
const unit8 = new Unit8Array(buffer);
unit8[0] = 10;
console.log(Atomics.add(unit8, 0, 5)); // 10
console.log(unit8[0]) // 15
console.log(Atomics.load(unit8, 0)); // 15
```

---

### 19. ES2017 - async와 await

```javascript
function walk(amount) {
    return new Promise((resolve, reject) => {
        if (amount < 500) {
            reject ("the value is too small")l
        }
        setTimeout(() => resolve(`you walked for ${amount}ms`), amount);
    });
}

// 비동기 함수 선언. 함수 앞에 async 키워드를 넣는다. 자바스크립트에게 항상 Promise를 반환하도록 지시한다. 프로미스가 아닌 값을 반환하게 작성하면 자바스크립트가 해당 값을 자동으로 프로미스로 감싼 후에 반환
async function go() {
    // 프로미스가 완료될 때까지 기다리기 위해 await 키워드 사용
    const res = await walk(500);
    console.log(res);
    const res2 = await walk(800);
    console.log(res2);
    const res3 = await walk(400);
    console.log(res3);
    const res4 = await walk(800);
    console.log(res4);
}

go();
```

---

### 20. ES2018

- 객체에 레스트 / 스프레드 구문 사용 가능

- 비동기 반복 : 데이터를 비동기적으로 반복 가능. 비동기 반복자는 next() 메서드가 {value, done} 쌍에 대한 프로미스를 반환한다는 점을 제외하면 동기 반복자와 매우 유사 / 비동기 반복을 위해 각각의 이터러블을 프로미스로 변환해서 작동하는 for-await-of 루프 사용 가능

- Promise.prototype.finally() : 프로미스가 완료될 때 호출할 콜백 등록. finally도 프로미스를 반환하므로 .then() .catch()를 계속 연결할 수 있지만 finally가 반환한 값이 아니라 그 전의 프로미스가 반환한 값을 전달받게 된다.

- 정규식 기능 추가 => 넷 다 무슨 말인지 전혀 모르겠다.

  - s(dotAll) 플래그 : .표현식이 개행 문자를 포함한 모든 문자를 포함하도록 한다.

  ```javascript
  /foo.bar/s.test('foo\nbar'); // true 
  ```

  

  - 명명된 캡처 그룹
  - 룩비하인드 어서션
  - 유니코드 속성 이스케이프

---

### 21. ES2019

- Array.prototype.flat() : 지정한 깊이까지 배열을 재귀적으로 평면화. 깊이 인수가 지정되지 않으면 1이 기본 값. Infinity로 지정하면 모든 중첩 배열 평면화

```javascript
const letters = ['a', 'b', ['c', 'd', ['e', 'f']]];
letters.flat(); // ["a", "b", "c", "d", Array(2)]
letters.flat(2); //  ["a", "b", "c", "d", "e", "f"]
letters.flat().flat(); // ["a", "b", "c", "d", "e", "f"]
letters.flat(Infinity); // ["a", "b", "c", "d", "e", "f"]
```



- Array.prototype.flatMap() : 배열 평면화 대신 새로운 값으로 매핑되어 생긴 배열을 평면화

```javascript
let greeting = ["Greetings from", " ", "Vietnam"];

greeting.map(x => x.split(" "));
//  ["Greetings", "from"], ["", ""], ["Vietnam"]

greeting.flatMap(x => x.split(" "));
// ["Greetings", "from", "", "", "Vietnam"]
```



- Object.fromEntries() : 키/값 쌍이 포함된 배열을 객체로 변환한다. 배열, 맵 등 이터러블 프로토콜을 구현하는 객체라면 무엇이든 Object.fromEntries()의 인수로 전달 가능하다.

```javascript
const keyValueArray = [
    ['key1', 'value1'],
    ['key2', 'value2']
];

const obj = Object.fromEntries(keyValueArray);
console.log(obj);
// {key1: "value1", key2: "value2"}
```



- String.prototype.trimStart(), trimEnd() : 문자열 시작 부분과 끝 부분 공백 제거 / trimLeft(), trimRight()와 동일

- 선택적 catch 할당 : catch절에 항상 예외 변수를 포함해야 했지만 이를 생략 가능. catch(error)가 아니라 그냥 catch 가능

- Function.prototype.toString() : 함수의 소스 코드를 나타내는 문자열을 반환. 주석도 함께 반환

- Symbol.prototype.description : 해당 심벌 객체의 설명 반환

  

---

### 22. ES2020

- 모든 브라우저가 지원하는 것은 아니므로 크롬, 파이어폭스 이용해 테스트. 해당 기능 지원되지 않는 프로젝트에서 사용하려면 바벨 같은 컴파일러 필요. 사용하면 7.8부터 기본적으로 ES2020을 지원하므로 그 밖의 플러그인 사용할 필요 없음

- BigInt : 매우 큰 정수 저장 가능. BigInt 생성자를 사용하거나 큰 정수 뒤에 n을 붙이면 된다.
- 모듈 동적으로 가져오기
- 옵셔널 체이닝 : elon의 university가 존재하는지 확인하고 graduation을 확인해야 했지만 ?.를 사용해 간결하게 작성할 수 있다.

```javascript
const elon = {
    name: 'Elon Musk',
    education: {
        primary_school: {},
        university: {
            name: "University of Pennsylvania",
            graduation: {
                year: 1995,
            },
        },
    },
};

const elonGraduationYear = elon.education.university? .graduation?.year;
// 1995 만약 존재하지 않을 시 undefined 반환.
```



- Promise.allSettled() : 성공, 실패 여부와 무관하게 모든 프로미스가 완료될 때까지 기다렸다가 각각의 결과 설명하는 객체 배열 반환(all은 모두 성공할 때 까지 기다리는 거)

```javascript
const arrayOfPromises = [
    new Promise((res, rej) => setTimeout(res, 1000)),
    new Promise((res, rej) => setTimeout(res, 1000)),
    new Promise((res, rej) => setTimeout(res, 1000)),
];

Promise.allSettled(arrayofPromises).then(data => console.log(data));
/* [
	{status: "fulfilled", value: undefined},
	{status: "rejected", value: undefined},
	{status: "fulfilled", value: undefined},
] */
```



- null 계열의 값 병합 : 거짓 값과 null 계열의 값(null, undefined)은 때때로 비슷할 수 있지만 엄연히 다른 값이다. 새로 도입된 연산자를 사용하 구분할 수 있다. 빈 문자열과 undefined를 구별하고 싶다면 null 병합 연산자(??)가 유용하다.

```javascript
const str = "";
console.log(!!str); // false

const str = undefined;
console.log(!!str); // false

const x = '' ?? 'empty string';
console.log(x); // ''

const u = undefined ?? "it's undefined";
console.log(u); // it's undefined
```



- String.prototype.matchAll() : 지정된 정규식에 대해 문자열과 일치하는 모든 결과의 반복자를 반환
- 모듈 네임스페이스 export 문법 
- import.meta : url등 모듈에 대한 정보 노출

```javascript
<script type="module" src="test.js"></script>
console.log(import.meta); // {url: "file://home/..."}
```



- globalThis : 브라우저에서 window, Node에서 global, 웹 워커에서 self를 사용해서 전역 객체 참조. ES2020부터 어떤 환경에서든 항상 전역 객체를 참조하는 globalThis를 사용할 수 있다. 

---

### 23.타입스크립트 기초

- userId를 사용해 사용자 정보 조회 api를 호출하는 것 같은 상황에서 자바스크립트는 강타입 언어가 아니라 자료형을 정의할 필요 없어 혼란스럽다. 타입스크립트를 사용하면 userId: number등으로 알려줄 수 있다.
- 타입스크립트는 자료형을 명시하는 방식을 지원하고 일반 자바스크립트로 컴파일된다. 자료형이 있는 자바스크립트 상위집합이라고 볼 수 있다. 타입스크립트 파일에 일반 자바스크립트를 작성해도 되며 오류가 발생하지 않는다. 브라우저는 타입스크립트를 이해하지 못하기 때문에 일반 자바스크립트로 트랜스파일 해야한다.

- npm install -g typescript
- .ts파일에서 코드를 작성하고 터미널에서 tsc greeter.ts 명령어를 실행하면 greeter.js 파일이 생성된다.
- 기본 자료형 : boolean, number, string, Array, object, 튜플, enum, any, void, null, undefined, never
- Array : type[] 또는 Array<type>으로 정의
- object : 원시 자료형 아닌 모든 자료형 값. 여러 속성 포함 가능하며 값은 원시 자료형, 객체, 함수 등이 될 수 있음.

---

### 한국어판 부록 : ES2021

- String.prototype.replaceAll() : 문자열 패턴을 다른 것으로 바꿀 수 있다. replace()는 정규식 패턴이 아닌 단순 문자열 패턴을 사용할 시 일치하는 첫 번째 항목만 교체 가능했지만 replaceAll()은 정규식을 사용하지 않아도 전부 교체
- Promise.any() : 주어진 프로미스 중 하나라도 성공하면 실행 완료, 그렇지 않으면 모든 프로미스가 실패할 때까지 계속된다. race()는 주어진 프로미스 중 하나라도 성공하거나 실패하면 전체 프로미스 실행이 완료된다.
- 논리 연산자와 할당 표현식 : &&, ||, ??와 할당 표현식(=)을 결합할 수 있다.
  - a ||= b는 a가 참이면 a반환 거짓이면 b반환
  - c &&= d는 c와 d가 모두 참이면 d 반환 그렇지 않으면 c반환
  - e ??= f는 e가 null이나 undefined인 경우 f를 반환하고 아니면 e반환
- 숫자 구분 기호 도입 : 100_000는 100,000과 동일
- 약한 참조 : 가비지 콜렉터에서 객체를 회수하는 것을 방지하지 않는 참조.
- Intl.ListFormat : 언어별로 목록 서식 활성화하는 객체 생성자
- Intl.DateTimeFormat의 dateStyle 및 timeStyle 옵션 : 시간대에 따른 날자 및 시간 서식 지정 가능

