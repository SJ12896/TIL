## 자바스크립트 코딩의 기술

### 1장 변수 할당으로 의도를 표현하라

- ECMAScript : 자바스크립트를 위한 공식적인 기술 명세. 5, 6를 통해 주요한 문법 변경 소개했으며 매년 갱신된다. ES2017처럼 연도를 붙여 부르기도 한다.
- const는 블록 문맥 내에서 재할당할 수 없다. 하지만 `불변값`이 되는 것은 아니다. 배열을 할당하면 배열의 항목은 바뀔 수 있다.

---

### 2장 배열로 데이터 컬렉션을 관리하라

- 펼침 연산자를 slice() 메서드와 함께 사용해 원래 배열에 영향을 주지 않고 새로운 배열 생성하기

```javascript
function removeItem(items, removable) {
    const index = items.indexOf(removable);
    return [...items.slice(0, index), ...items.slice(index+1)];
}
```

---

### 3장 특수한 컬렉션을 이용해 코드 명료성을 극대화하라

- 객체는 정적인 정보에 적합하다. 게속해서 갱신, 반복, 대체, 정렬해야 하는 정보에는 적절하지 않다. 그럴 때는 맵을 사용하는 것이 낫다. 객체는 `정보의 경로`를 알고있을 때 적절한 방법이다.

- Object.assign() : 메서드는 일련의 객체를 전달받고 가장 먼저 인수로 받은 객체를 뒤이어 인수로 넘긴 객체의 키-값을 이용해서 갱신한다. 그리고 갱신된 첫 번째 객체를 반환한다. -> 첫 번째 객체에 빈 객체를 넣고, 그 다음 원본 객체, 그리고 새로운 객체를 넣으면 빈 객체에 새로운 값이 갱신되어 반환된다. 

  - 그러나 중첩된 객체인 경우 다르다. 중첩된 객체를 담고있는 객체가 가지고 있는 것은 중첩된 객체에 대한 참조뿐이다. 참조에 대한 복사만으로 중첩된 객체에 깊은 복사를 적용할 수 없다. 따라서 원본 객체나 복사한 객체 중 어디서라도 중첩된 객체의 값을 변경하면 원본, 복사 객체 모두 변경된다. 따라서 아래와 같은 방식으로 활용한다.

  - ```javascript
    const employee2 = Object.assign(
        {},
        defaultEmployee,
          	{
            name: Object.assign({}, defaultEmployee.name),
          	}
        );
    ```

  - 아니라면 lodash 라이브러리의 cloneDeep()메서드를 이용한다. 

- 객체 펼침 연산자 : 배열 펼침 연산자와 비슷하게 동작한다. 다른 점은 동일한 키에 서로 다른 값을 추가하면 어떤 값이든 가장 마지막에 선언된 값을 사용한다.

  - 위의 코드를 객체 펼침 연산자로 다시 작성한다면

  - ```javascript
    const employee = {
        ...defaultEmployee,
        name: {
            ...defaultEmployee.name,
        },
    };
    ```



- `데이터 변경이 잦은 키-값 컬렉션에 맵 객체 사용` : MDN에 일반적인 객체보다 맵을 컬렉션으로 선택하는 것이 더 나은 상황이 있다. 그 중 `키-값 쌍이 자주 추가되거나 삭제되는 경우`, `키가 문자열이 아닌 경우`

- 브라우저 엔진 : 자바스크립트 코드는 브라우저 엔진이 해석. 크롬, Node.js에서 사용하는 V8엔진 / 파이어폭스의 스파이더 몽키, 차크라 등. 엔진에 따라 기능도 서로 다르게 구현될 수 있음. 맵은 특화된 컬렉션으로 엔진 개발자들은 코드가 좀 더 빠르게 동작하도록 최적화할 수 있다. 객체에서 키 탐색은 선형 시간이 소요되나 맵이 브라우저에 내장 구현된 경우 맵의 키 탐색은 로그 시간이 될 수 있다. 

- ```javascript
  let filters = new Map();
  filters.set('견종', '래브라도레트리버');
  filters.get('견종'); // 래브라도레트리버
  
  // 메서드 체이닝
  let filters = new Map()
  	.set('견종', '래브라도레트리버')
  	.set('크기', '대형견')
  	.set('색상', '갈색');
  filters.get('크기'); // 대형견
  
  // 배열로 데이터 추가
  let filters = new Map(
  	[
          ['견종', '래브라도레트리버'],
          ['크기', '대형견'],
          ['색상', '갈색'],
      ]
  )
  
  filters.delete('색상');
  filters.clear() // 새로운 인스턴스를 생성할 필요없다.
  ```

- 객체의 경우 키에 사용할 수 있는 자료형에 제약이 있다. 정수를 키로 사용할 수 없다. 만약 키를 100으로 했다면 생성했을 때 모든 정수가 문자열로 변환된다. 맵은 여러가지 자료형을 키로 받을 수 있다.

- 맵도 객체처럼 .keys()를 통해 키만 모아서 확인할 수 있다. 다만 배열이 아닌 맵이터레이터가 반환된다. 

- 객체는 정렬할 수 없고 (키를 정렬한 뒤 순회하는 방식으로 해야한다.) 순회할 때 for...in문을 사용해야 한다. 반면 맵은 맵이터레이터에 순회 기능이 내장되어 있다. 이터레이터는 키-값 쌍을 넘겨준다. for문으로 맵 객체 순환 시 정보를 배열로 넘겨주지만 .entries(); 를 사용하면 맵에 있는 키-값을 싸응로 묶은 맵이터레이터를 반환한다. 

  - enteries()로 키-값을 받을 수 있는 기능은 매우 편리해서 ES2017부터 Object의 내장 메서드로 추가되었다. Object.entries()

- 맵은 순서를 내장한다. 하지만 정렬 메서드가 내정되어 있지는 않다. 펼침 연산자를 사용 시 키-값 쌍이 반환된다.

- 정렬

  - ```javascript
    function sortByKey(a, b) {
        return a[0] > b[0] ? 1: -1;
    }
    
    function getSortedAppliedFilters(filters) {
        const applied = [...filters] // 맵을 배열로 변환한다.
        	.sort(sortByKey)  // 배열을 정렬한다.
        	.map(([key, value]) => {
                return `${key}:${value}`; // 배열에 담긴 키-값 쌍을 키:값 형식의 문자열로 변환한다.
            })
        .join(', ');
        return `선택한 조건은 ${applied} 입니다.`;
    }
    ```



- 맵에 has() 메서드를 사용해 키가 존재하는지 확인할 수 있다. 
- 맵은 객체와 마찬가지로 새로운 키로 맵을 생성하면 어떤 값이든 해당 키에 마지막으로 선언한 값을 사용한다. 값을 설정하는 대신 갱신한다.

- 세트(Set) : 각 고유 항목을 하나씩만 갖는 특화된 배열과 같다. new Set()를 사용해 고유값을 가진 세트 객체를 생성한 후 펼침 연산자를 이용해 배열로 반환할 수 있다.
  - 값 추가 : add()
  - 검증 : has()
  - delete(), clear()

---

### 4장. 조건문을 깔끔하게 작성하라

- 배열과 객체의 경우 빈 배열, 빈 객체라도 항상 참 값이기 때문에 비어있는지 확인하려면 .length, .keys() 등을 활용해 0또는 참값인 숫자를 반환하는 방법을 사용해야 한다.
- 의도치 않게 거짓값을 만드는 경우 -> ['a', 'b'].indexOf('a') => 0이 반환되며 0은 거짓 값
- for문 안에서 특정 값을 만들 경우 블록 밖에서 let 변수를 선언하거나 밖에서도 접근 가능한 var로 선언해야하지만 `삼항 연산자`를 사용하면 추가 코드를 줄일 수 있다.
- 또는 삼항연산자가 복잡해지는 경우에는 분리된 함수의 반환값을 const에 할당할 수 있다.

```javascript
function getTimePermissions({title}) {
    if (title === '과장') {
        return ['근로시간', '초과근무승인', '수당'];
    }
    if (title === '부장') {
        return ['근로시간', '초과근무승인'];
    }
    return ['근로시간'];
}

const permissions = getTimePermissions({ title: '사원' });
```

- 삼항 연산자를 더 간결하게 바꿀 수 있도록 `단락 평가`를 활용한다. (가장 타당한 정보를 먼저 위치시켜서 정보 확인을 건너뛰기)
  - 단락평가의 가장 좋은 점은 표현식 끝에 `기본값`을 추가할 수 있다는 것

---

### 5장. 반복문을 단순하게 만들어라

- 콜백 함수 : 다른 함수의 매개변수로 전달된다.
- 익명 함수 -> 화살표 함수 : function 키워드 제거하고 두꺼운 화살표로 대체 / 매개변수가 하나라면 괄호 제거 / 중괄호 안 함수 몸체가 한 줄이라면 화살표, 매개변수, return문을 한 줄에 담을 수 있다. (return 키워드, 중괄호 사용할 필요 없음)
- 콜백함수 사용하기

```javascript
applyCustomGreeting('mark', function (name) {
    return `안녕, ${name}!`;
});

// 화살표 함수로 다시 작성
applyCustomGreeting('mark', name => `안녕, ${name}!`;);
```



- map() : 형태를 바꿀 수 있지만 길이는 유지된다. 전체 팀원의 이름만 가져오기 / 입력한 배열의 정보 중 한 조각을 받아 새로운 값을 반환하거나 정보의 일부를 반환한다.
- sort() : 형태, 길이 변경되지 않고 순서만 바꾼다. 팀원 이름 알파벳순 정렬
- filter() : 길이 변경하지만 형태 유지한다. 개발자만 선택하기 / 전달하는 함수는 반드시 참 값을 반환해야 한다. 각 항목 순회 시 참 값을 반환하면 그 값은 유지된다. / 항상 배열을 반환하기 때문에 조건에 일치하는 값이 없는 경우에도 배열을 반환한다.
- every() : 배열의 모든 항목을 대상으로 콜백 함수를 실행해 모든 항목에서 참 값이 반환되면 결과적으로 true를 반환한다.
- find() : 배열을 반환하지 않고 한 개 데이터만 반환, 형태 유지된다. 팀의 관리자 찾기 / 조건에 일치하는 항목이 최대 하나라는 사실을 알고 있다면 filter()대신 find()를 사용한다. / 참 값을 반환하는 첫 번째 항목만 반환하며 없다면 undefined를 반환한다. 단락평가를 이용해서 default 값을 지정해주면 좋다.
- forEach() : 형태 이용하고 아무것도 반환하지 않는다. 모든 팀원에게 상여를 지급한다. / forEach()에서 처리하는 동작은 모두 함수 외부에 영향을 준다. 함수 유효 범위 밖에 있는 무언가를 변경하는 것을 부수 효과라고 한다. 초대 이메일을 보낼 때 처럼 부수 효과지만 데이터를 조작하지 않는 경우에 사용한다.
- reduce() : 길이와 형태를 바꾸는 것을 비롯해 무엇이든 처리할 수 있다. 개발자와 개발자가 아닌 모든 팀원의 수를 계산한다. / 반환값이 정수뿐 아니라 세트 같은 컬렉션도 될 수 있다. / 배열을 이용해 근본적으로 다른 새로운 데이터를 만들어야 할 경우가 있다. 특정 항목의 수나 배열을 객체처럼 다른 형태 자료구조로 변환해야 하는 경우도 있다. 

```javascript
const prices = ['1,0', '2,15']
const formattedPrices = prices.map(price => parseFloat(price));

// 배열 메서드 연결
const prices = ['1,0', '2,15', '흥정가능'];
const formattedPrices = prices.map(price => parseFloat(price)) // 글자는 NaN으로 변환된 상태
.filter(price => price);

// 기명함수로 사용할 수도 있다.
function getInstrument(member) {
    return member.instrument;
}
const instruments = band.map(getInstrument); // 악기 이름만 담은 배열 반환

// 다시 화살표 함수로
const instruments = band.map(member => member.instrument);

// 커링 사용
const findByLibrary = library => instructor => {
    return instructor.libraries.includes(library);
}
const librarian = instructors.find(findByLibrary('미디어교육정보 도서관'));
```

reduce예시

- 기본값은 선택적으로 넘겨줄 수 있지만 대부분 작성. 기본값 작성 시 반환값을 담을 수 있다.
- map() 메서드의 결과값을 세트에 넘겨주는 방법으로 고윳값을 분류할 수 있는데 왜 reduce()를 사용할까? 리듀서가 더 많은 값을 쉽게 다룰 수 있도록 코드에 `유연성`을 제공하기 때문이다. 한 가지 속성 값을 모아야 한다면 map() 메서드를 쓰는 것이 더 적절하다.
  - 강아지 객체의 모든 키에 대해 고윳값을 분류하려면 map()을 여러 번 실행해 세트에 값을 전달할 수 있지만 초깃값을 빈 세트로 한 reduce() 메서드를 사용해 객체를 채울 수 있다.

```javascript
const callback = function(collectedValues, item) {
    return [...collectedValues, item];
};

const saying = ['test', 'hi', 'hello'];
const initialV = [];
const copy = saying.reduce(callback, initialV); // 콜백 함수와 기본값 전달

console.log(copy); //(3) ["test", "hi", "hello"]

// 원하는 고윳값 : 색상
// 중복 색상을 제외해 크기를 변경했고 여러 속성 중 색상만 변경해 형태도 변경한 상황.
const colors = dogs.reduce((colors, dog) => {
    if (colors.includes(dog['색상'])) {
        return colors;
    }
    return [...colors, dog['색상']];
}, []);

// 모든 키에 대한 고윳값
const filters = dogs.reduce(filters, item) => {
    filters.breed.add(item['견종']);
    filters.size.add(item['크기']);
    filters.color.add(item['색상']);
    return filters;
},
{
    breed: new Set(),
    size: new Set(),
    color: new Set(),
});

// 예제
const aggregated = developers.reduce((specialities, developer) => {
    const count = specialities[developer.language] || 0;
    return {
        ...specialities,
        [developer.language]: count + 1,
    };
}, {});
```





- match() : 문자열이 정규 표현식과 일치하면 일치한 항목에 대한 정보 배열로 반환, 일치하지 않으면 null 반환.

- `체이닝` : 값을 다시 할당하지 않고 반환된 객체(또는 경우에 따라 원래 객체)에 메서드를 즉시 호출하는 것
  - 마지막 문장까지 세미콜론이 없는 것 확인

```javascript
// 단점은 새로운 메서드를 호출할 때마다 반환된 배열 전체를 다시 반복한다는 점이다. for문을 사용하면 name, active, email에 각 한 번씩 세 번을 순회하지만 체이닝을 사용하면 일곱 번 반복한다.(filter적용 시 3번, map에 2번, forEach에 2번)

// map과 filter의 순서를 바꾸면 모든 sailor.active가 undefined를 반환하기 때문에 아무런 오류도 발생하지 않는다.

sailors
.filter(sailor => sailor.active)
.map(sailor => sailor.email || `${sailor.name}@wiscsail.io`)
.forEach(sailor => sendEmail(sailor));
```



- 배열이 아닌 컬렉션을 다룰 때 배열 메서드를 사용하려면 Object.keys()를 사용해 키 배열을 만들어 원하는 모든 메서드를 실행하거나 펼침 연산자를 사용하면 맵을 키-값 쌍이 담긴 배열로 변환할 수 있다. 
- `for...of` : 색인 대신 컬렉션의 멤버를 직접 순회한다. 배열 메서드가 명확하고 적합하면 배열 메서드를 우선해서 사용한다.

```javascript
for (const firm of firms) {
    const [id, name] = firm;
    if (!isAvailable(id)) {
        return `${name}는 사용할 수 없습니다`;
    }
}
return '모든 회사를 사용할 수 있습니다';
```



- `for...in` : 키-값 객체에서만 작동하는 for...of와 비슷하지만 다른 반복문. Object.keys()의 과정을 피할 수 있다. 각 항목을 한 번에 하나씩 받아 매번 키를 사용해 전체 컬렉션을 참조해야 한다. 

```javascript
for (const id in firms) {
    if (!isAvailable(parseInt(id, 10))) { // 키가 자동으로 문자열로 바뀌기 때문에
        return `${firms[id]}는 사용할 수 없습니다`;
    }
}
return '모든 회사를 사용할 수 있습니다';
```



---

### 6장. 매개변수와 return 문을 정리하라

- 자바스크립트에서 함수에 모든 매개변수를 전달할 필요는 없다. 매개변수를 선택적으로 적용할 수 있어 누락하면 undefined가 된다.
- 매개변수에 기본값을 정해뒀을 때 값을 전달하고 싶지 않으면 undefined를 전달하면 된다. 그러나 null을 전달하는 경우 같은 때 설정한 기본값이 사용되지 않는다.
- 해체 할당을 통해 객체의 정보를 곧바로 변수에 할당하자. 객체에 있는 키와 같은 이름의 변수를 생성하고 연결된 값을 생성한 변수 값으로 할당한다.

```javascript
const landscape = {
    photographer: 'Nathan',
};
const { photographer } = landscape;
photographer; // Nathan

// 객체에 키가 존재하지 않을 때 기본값 설정
const landscape = {};
const {photographer = 'Anonymous', title } = landscape;
photograpehr; // Anonymous
title; // undefined

// 객체의 키 이름을 모르면 남은 정보는 어떻게 가져올까? 정보를 수집하기 위해 마침표 세 개를 사용하는 경우에는 펼침 연산자가 아닌 `나머지 매개변수`라고 부른다. 변수 이름은 키 이름과 일치하지 않아야 된다. 변수에 할당하는 값은 객체에 남아있는 키-값 쌍을 모은 객체다.
const landscape = {
    photographer: 'Nathan',
    equipment: 'Canon',
    format: 'digital',
};

const {
    photographer,
    ...additional
} = landscape;

additional;
// { equipment: 'Canon', format: 'digital' } 객체에서 꺼낸 photographer를 제외한 나머지 키-값 쌍이 새로운 객체에 담긴다. 

// 변수 이름으로 원래 키와 다른 이름을 지정할 수도 있다.
const landscape = {
    src: '/landscape-nm.jpg',
};
const { src:url } = landscape;

url; // '/landscape-nm.jpg',
```



- 배열에도 해체 할당을 사용할 수 있는데 키가 없기 때문에 이름은 마음대로 정할 수 있지만 순서대로 할당해야 한다. 

```javascript
const landscape = {
    location: [32.7122, -103.1405],
};
const { location } = landscape;
const [latitude, longitude] = location;

latitude; // 32.7122

// 한 번으로 줄여도 된다.
const { location: [latitude, longitude] } = landscape;
```



- 미리 알 수 없는 과도한 양의 객체 안 정보를 받아 처리하는 방법으로 해체 할당 사용

```javascript
function displayPhoto({
    title,
    photographer = 'Anonymous',
    location: [latitude, longitude],
    src: url,
    ...other
}) {
    const additional = Object.keys(other).map(key => `${key}: ${other[key]}`);
    return (`
	<img alt="${title} 사진${photographer} 촬영" src="${url}" />`)
}
```



- `arguments`객체 : 함수에 전달된 모든 인수를 담은 배열과 유사한 컬렉션. `객체`이므로 배열로 변환해야 한다. 정확히 말하면 배열 인스턴스가 아닌 Array 객체에 정적으로 메서드를 호출해야 한다.

```javascript
function getArguments() {
    return arguments;
}
getArguments('Bloomsday', 'June 16');
// { '0': 'Bloomsday', '1': 'June 16' };

// arguments를 다루는 방법이 난해해 잘 사용하지 않는다.
function validateCharacterCount(max) {
    const items = Array.prototype.slice.call(arguments, 1);
    return items.every(item => item.length < max);
}

function getArguments(...args) {
    return args;
}
getArguments('Bloomsday', 'June 16'); // ['Bloomsday', 'June 16']

function validateCharacterCount(max, ...items) {
    return items.every(item => item.length < max);
}
```



- 인수에서 나머지 매개변수를 사용하는 경우 유일한 단점은 언제나 마지막 인수에 사용해야 한다는 점이다. 반드시 함수의 마지막 매개변수여야 한다. 해체 할당의 경우에도 마지막 값이어야 한다.

---

### 7장. 유연한 함수를 만들어라

- 테스트 프레임워크 : 재스민, 모카, 제스트
  - 이 팁을 활용하려면 describe(), it() 함수의 기본을 이해하고 기댓값을 알고 있어야 한다.
- 내가 만든 함수 안에서 외부 함수를 호출해 사용할 때 외부 함수를 실행하지 않으면 내가 만든 함수를 실행할 수 없다. 외부 함수가 외부 서비스나 설정 파일에 접근해야 하면 네트워크 통신과도 관련된다. 테스트 실행 시 외부 API에 접근해야 하며 테스트는 네트워크 접근, 응답 시간 등에 의존하게 된다. => 이런 문제를 피하려면 모의 객체를 생성해 함수를 가로채고 명시적인 반환값을 설정하게 만들어야 한다.

#### 테스트 관련 내용 잠시 패스

---

- 화살표 함수에서 해체 할당 사용하기

```javascript
// 일반 함수
const name = {
    first: 'Lemmy',
    last: 'Kilmister',
};

function getName({ first, last }) {
    return `${first} ${last}`;
}

// 화살표 함수로 바꾼다면? 괄호가 없어 함수라고 생각못해 에러 발생
// 특별한 매개변수를 사용할 때는 괄호로 감싸줘야 한다.
const getName = { first, last } => `${first} ${last}`;
```



- `고차 함수` : 다른 함수를 반환하는 함수. 화살표 함수로 만들면 좋다.

```javascript
const discounter = discount => {
    return price => {
        return price * (1 - discount);
    };
};
const tenPercentOff = discounter(0.1);
tenPercentOff(100); // 90

// 반환값 함수도 화살표 함수화 하기
const discounter = discount => price => pirce * (1 - discount);

// 첫 번재 매개변수 바로 뒤에 괄호를 연결해 두 번째 매개변수 전달하기
discounter(0.1)(100); // 90
```



- 고차 함수는 함수 실행이 완전히 끝날 때까지 최소한 두 단게에 걸친 매개변수가 존재한다. 부분 적용 함수를 사용할 경우, 일부 매개변수를 전달하면 해당 매개변수를 잠그는 함수가 반환되어 여기에 더 많은 매개변수를 사용할 수 있다. =>  한 번에 전달해야 할 함수 인수의 수가 줄어드는 대신 인수를 더 전달해야 하는 다른 함수를 반환한다.
- 서로 독립적인 여러 매개변수 집합을 둘 수 있다. 단일 책임을 지는 것처럼 보이지만 입력값 간에 서로 다른 관계를 갖기도 한다. 
- 한 개의 함수를 사용해 세 가지 매개변수를 받지 말고 고차 함수를 적용해 (2개)(1개)로 가능



- 지역 이름이 담긴 배열을 받아 지역을 상징하는 새 이름을 반환하는 함수

```javascript
const zip = (...left) => (...right) => {
    return left.map((item, i) => [item, right[i]]);
};
zip('kansas', 'wisconsin', 'new mexico')(...birds);
// [
// ['kansas', 'meadowlark'],
//    ...
// ]
```



- 함수의 부분 적용을 통해 변수를 저장해두는 방법. 같은 매개변수를 반복해서 사용할 경우 같은 매개변수를 여러 번 전달하고 있다. 고차 함수를 사용하면 값을 한 번 저장한 후 나중에 사용할 수 있는 새로운 함수를 만들어서 반복을 피할 수 있다. 고차 함수에서 반환된 함수는 바로 다시 호출할 필요가 없다. 고차 함수를 한 번 호출하면 계속해서 사용할 수 있는 새로운 함수가 반환되기 때문이다.

```javascript
const setStringHallProgram = mergeProgramInformation(building, manager);
const programInfo = setStrongHallProgram(program);
const exhibitInfo = setStringHallProgram(exhibit);
```

- 고차 함수를 이용하면 매개변수를 별도로 분리할 수 있다. 함수를 완전히 분리하기 전에 필요한 인수의 수를 줄일 수 있도록 인수를 분리하는 것이 훨씬 더 중요하다. 한 번에 인수를 하나만 받는 함수를 `커링currying`이라고 하며 하나의 인수만 전달하는 메서드를 다룰 때 매우 유용하다. 자바스크립트는 순수한 형태의 커링을 완벽하게 지원하진 않지만 부분 적용을 이용해 일련의 단일 매개변수로 매개변수 숫자를 줄이는 방법이 일반적
  - 부분 적용 함수 : 매개변수를 여러 번 받을 수 있음. 커링과 혼동되지만 다르다.
  - 부분 적용 함수, 커링 함수 모두 원래보다 필요한 인수의 수가 적은 함수를 반환해 인수의 수를 줄인다. 함수가 받을 수 있는 전체 인수의 수는 `항수`라고 한다. 부분 적용 함수는 원래 함수보다 `항수`가 적은 함수를 반환한다. 인수가 총 세 개 필요한 경우 두 개를 먼저 전달했다면 반환된 함수에는 하나만 있으면 된다. 
  - 커링 함수는 여러 개 인수를 받는 함수에서 정확히 인수 하나만 받는 일련의 함수를 반환할 때 사용한다. 가령 인수 세 개가 필요한 함수가 있으면 먼저 인수 하나를 받는 고차 함수가 다른 함수를 반환하고 반환된 함수도 인수 하나를 받는다. 



```javascript
const dogs = [
    { 이름: '맥스',
    무게: 10,
    견종: '보스턴테리어',
    지역: '위스콘신',
    색상: '검정색',
    },
    { 이름: '도니',
    무게: 90,
    견종: '래브라도레트리버',
    지역: '캔자스',
    색상: '검정색',
    },
]
    
// 강아지 배열과 필터 조건을 인수로 받아 필터링 조건에 맞는 강아지 이름만 모아서 반환하는 함수 작성. 강아지 배열이 첫 매개변수, 배열 메서드 filter()와 map() 조합
function getDogName(dog, filter) {
    const [key, value] = filter,
    return dogs
    	.filter(dog => dog[key] === value)
    	.map(dog => dog['이름']);
}

getDogNames(dogs, ['색상', '검정색']); // ['맥스', '도니']

// 정해진 체중보다 무게가 적게 나가는 강아지 찾기. 비교 함수를 하드 코딩하지 않고 필터 함수에 콜백 함수로 전달한다.
function getDogNames(dogs, filterFunc) {
    return dogs
    .filter(filterFunc)
    .map(dog => dog['이름'])
}

getDogNames(dogs, dog => dog['무게'] < 20); // ['맥스']

// 부분 적용 함수를 변수에 할당해서 다른 함수에 데이터로 전달하는 방법으로 나머지 인수 제공
const weightCheck = weight => dog => dog['무게'] < weight;
getDogNames(dogs, weightCheck(20)); // ['맥스']

// 두 개의 함수와 두 개의 인수 집합으로 제한할 필요 없다.
const identity = field => value => dog => dog[field] === value;
const colorCheck = identity('색상');
const stateCheck = identity('지역');

getDogNames(dogs, colorCheck('갈색'));

// 모든 조건을 충족하는 강아지를 찾아야 한다면
function allFilters(dogs, ...checks) {
    return dogs
    .filter(dog => checks.every(check => check(dog)))
    .map(dog => dog['이름']);
}

allFilters(dogs, colorCheck('검정색'), stateCheck('캔자스')); // ['도니']
```



- 함수의 유효 범위 : 함수가 접근할 수 있는 변수
- 문맥 : 함수, 클래스에서 this 키워드가 참조하는 것
  - 객체에서 this를 다룰 때는 큰 문제가 없지만 객체에 담긴 함수를 다른 함수의 콜백 함수로 사용할 경우 주의가 필요하다.
  - setTimeout(), setInterval() 메서드나 map(), filter() 메서드 등 자주 사용하는 배열 메서드를 사용할 때 이 함수들은 콜백 함수를 받으면 콜백 함수의 문맥도 변경한다.

```javascript
 // map 메서드에 콜백 함수로 전달한 경우 map() 메서드의 문맥에서 호출되므로 this 바인딩이 validator 객체가 아니라 전역 객체가 된다. 브라우저에서는 window, Node.js REPL 환경에서는 global이 된다.
const validator = {
    message: '는 유효하지 않습니다.',
    setInvalidMessages(...fields) {
        return fields.map(function (field) {
            return `${field}${this.message}`;
        });
    },
};

validatorProblem.setInvalidMessages(field); // TypeError

// 화살표 함수를 사용한 문제 해결 : 화살표 함수는 함수를 호출할 때 this 바인딩을 새로 만들지 않는다.
const validator = {
    message: '는 유효하지 않습니다.',
    setInvalidMessages(...fields) {
        return fields.map(field => {
            return `${field}${this.message}`;
        });
    },
};

validator.setInvalidMessages('도시');

// 메서드가 아니라 속성에 할당한 화살표 함수로 작성한다면? 
// 현재 객체에 대해 새로운 this 문맥 바인딩을 만들지 않아 전역 객체에 바인딩 됨.
const validator = {
    message: '는 유효하지 않습니다.',
    setInvalidMessages: field => `${field}${this.message}`,
};

validatorProblem.setInvalidMessages(field); // TypeError
```

- 화살표 함수는 이미 문맥이 있고 다른 함수 내부에서 이 함수를 사용할 때 유용하다. 그렇지만 새로운 this 바인딩을 설정할 필요가 있을 때 문제가 된다.

---

### 8장. 클래스로 인터페이스를 간결하게 유지하라

- 클래스에서 메서드를 추가할 때는 화살표 함수가 아닌 보통 함수로 작성한다. 화살표 함수를 사용하면 보통 함수와 다르게 동작한다.
- 상속 : 새로운 생성자에서 부모 클래스 생성자에 접근하려면 super()를 호출해야 한다. super()로 부모 클래스 생성자를 호출하기 때문에 부모 클래스의 생성자에 필요한 인수가 있다면 super()를 이용해서 넘겨줄 수 있다.
- 클래스로 객체 인스턴스를 생성하는 것처럼 생성자 함수로 객체 인스턴스를 생성할 수 있다. 함수를 생성자로 사용하려면 코딩 컨벤션으로 함수명을 대문자로 시작하고 내부에서 this를 사용해 속성을 연결할 수 있다. new를 이용해 새로운 인스턴스를 생성할 때는 함수를 생성자로 사용하고 this 문맥을 바인딩한다. 

```javascript
// 클래스에서와 다른 점은 메서드가 사라졌다는 것
function Coupon(price, expiration) {
    this.price = price;
    this.expiration = expiration || '2주';
}
const coupon = new Coupon(5, '2개월');
```

- 생성자에서 this에 메서드를 추가하기보다 프로토타입에 직접 추가하는 것이 효율적이다. `프로토타입`은 생성자 함수의 기반이 되는 객체다. 모든 객체 인스턴스는 프로토타입에서 속성을 가져온다. 새로운 인스턴스도 프로토타입에 있는 메서드를 사용할 수 있다. 프로토타입에 메서드를 추가하려면 생성자 이름 Coupon을 사용해 객체 인스턴스에 함수나 속성을 추가하는 것처럼 prototype 속성에 메서드를 추가하면 된다.

```javascript
// class 키워드로 객체를 생성할 때도 프로토타입을 생성하고 문맥을 바인딩한다.
// 프로토 타입을 이용해 생성한 레거시 코드에 새로운 코드를 추가할 때 클래스를 사용할 수도 있다. 클래스 문법으로 생성한 Coupon 클래스를 확장할 때 와 동일한 프로세스를 따른다.
Coupon.prototype.getExpirationMessage = function() {
    return `이 쿠폰은 ${this.expiration} 후에 만료됩니다.`;
}
coupon.getExpirationMessage();
```



- 비공개 속성은 기본적으로 지원하지 않는다. 대신 개발자들이 이름 앞에 밑줄을 입력해 비공개라는 점을 표시한다.



- `제너레이터` : 함수가 호출되었을 때 그 즉시 끝까지 실행하지 않고 중간에 빠져나갔다가 다시 돌아올 수 있는 함수. function 키워드 뒤에 *를 추가해서 생성한다. 이렇게 하면 next() 메서드에 접근해 함수가 내보낸 정보를 가져올 수 있다. next를 호출하면 value, done이 있는 객체를 가져온다. done은 남은 항목의 여부다. 함수 몸체 안에서는 yield를 사용해 정보를 반환한다. 

```javascript
function* getCairoTrilogy() {
    yield '궁전 샛길';
    yield '욕망의 궁전';
    yield '설탕 거리';
}

const trilogy = getCairoTrilogy();
trilogy.next();
// { value: '궁전 샛길', done: false}
// ... 3번까지 출력한 후 next를 실행하면
// { value: undefined, done: true}

// 펼침 연산자를 사용해 배열에 담을 수 있다.
[...getCairoTrilogy()]; 
// [ '궁전 샛길', ... ]
```



- bind() 사용하기 : this가 참조하는 속성이 존재하지 않을 때 bind를 이용해 특정 객체를 명시적으로 this로 설정할 수 있다. `명시적 연결` / 단점은 다른 메서드에서 함수를 사용하면 다시 bind()로 연결해야 한다는 것이다. 생성자에서 메서드와 같은 이름을 가진 속성에 this를 연결한 메서드를 설정해 bind()를 여러 번 호출하는 것을 피한다.

```javascript
function sayMessage() {
    return this.message;
}

const alert = {
    message: '위험해!',
}

const sayAlert = sayMessage.bind(alert);
sayAlert(); // 위험해!

// bind() 여러 번 호출 피하기
const Validator {
    constructior() {
        this.message = '가 유효하지 않습니다.';
        this.setInvalidMessage = this.setInvalidMessage.bind(this);
        // 화살표 함수 이용
        // setMessage = filed => '${field}${this.message}';
    }
    
    setInvalidMessage(field) {
        return `${field}${this.message}`;
    }
    
    setInvalidMessages(...fields) {
        return fields.map(this.setInvalidMessage);
    }
}
```





---

### 9장. 외부 데이터에 접근하라

- 비동기 언어 : 이전 코드가 완전히 해결되지 않아도 이어지는 코드를 실행할 수 있는 언어
- 프라미스는 콜백 함수를 인수로 받는 대신 성공과 실패에 대응하는 메서드를 사용한다. 콜백 함수를 중첩하는 대신 여러 개의 비동기 프라미스를 연결할 수도 있다. / 비동기 작업을 전달받아 응답에 따라 두 가지 메서드 중 하나를 호출하는 객체
- 프라미스는 두 개의 인수, resolve()와 reject()를 전달받는다. resolve()는 코드가 의도대로 동작됐을 때 실행된다. resolve()가 호출되면 then() 메서드에 전달된 함수가 실행된다. 

```javascript
function getUserPreferences() {
    const preferences = new Promise((resolve, reject) => {
        resolve({
            theme: 'dusk',
        });
    });
    return preferences;
}

function failUserPreference() {
    const finder = new Promise((resolve, reject) => {
        reject({
            type: '접근 거부됨',
        });
    });
    return finder;
}

getUserPreferences()
	.then(preferences => {
    	console.log(preferences.theme);
});
// 'dusk'

failUserPreference()
	.then(preferences => {
    console.log(preferences.theme);
})
.catch(error => {
    console.error(`실패 : ${error.type}`);
}); // 실패: 접근 거부됨

// 여러 개의 프라미스 연결하기
function getMusic(theme) {
    if (theme === 'dusk') {
        return Promise.resolve({
            album: 'music for airports',
        });
    }
    return Promise.resolve({
        album: 'kind of blue',
    });
}

function failMusic(theme) {
    return Promise.reject({
        type: '네트워크 오류',
    });
}

getUserPreferences()
	.then(preference => getMusic(preference.theme))
	.then(music => { console.log(music.album); })
	.catch(e => {
    	console.log(e);
})
```



- async 키워드를 이용해 선언한 함수 : 비동기 데이터를 사용한다는 것을 의미
- 비동기 함수 내부에서 await 키워드를 사용하면 값이 반환될 때까지 함수의 실행 중지시킬 수 있다.
- async/await가 프라미스를 대체하지는 않는다. 단지 프라미스를 더 나은 문법으로 감싸는 것이다. 또 서버 측 자바스크립트에 사용할 때는 안전하지만, 브라우저에서 사용할 때는 문제가 발생할 수 있다.

```javascript
async function getTheme() {
    const { theme } = await getUserPreferences();
    return theme;
}

getTheme()
	.then(theme => {
    console.log(theme);
});

// 여러 개의 프라미스
async function getArtistByPreference() {
    const { theme } = await getUserPreferences();
    const { album } = await getMusic(theme);
    const { artist } = await getArtist(album);
    return artist;
}

getArtistsByPreference()
	.then(artist => {
    	console.log(artist);
	})
	.catch(e => {
    console.error(e);
});
```



- fecth() : 자바스크립트 명세의 일부가 아니다. 따라서 대부분의 최신 브라우저에서 지원되지만 Node.js에서는 기본적으로 지원되지 않는다. 패키지 사용 필요
  - 요청에 실패한 경우에도 응답 본문을 반환한다. 요청이 실패하는 경우를 catch() 메서드만으로 처리할 수 없다.

```javascript
fetch('https://~')
	.then(data => {
    if (!data.ok) {
        throw Error(data.status);
    }
    return data.json(); 
})
	.then(post => {
    console.log(post.title);
})
	.catch(e => {
    console.log(e);
});

// POST 요청 보내기
const update = {
    title: 'asdf',
    body: 'qwer',
    userId: 1,
};

const options = {
    method: 'POST',
    headers: {
        '	Content-Type' : 'application/json',
    },
    body: JSON.stringfy(update),
};

fetch('https://~', options).then(data => {
    ...
})
```



- sessionStorage : 서버 측 렌더링과 클라이언트 측 기능이 혼합된 경우에 유용하다. 페이지를 새로 고침하면 저장한 데이터가 유지되고, 사용자가 페이지를 떠났다가 다시 돌아오면 저장한 데이터가 없는 기본 상태를 보여준다.



---

### 10장. 컴포넌트 아키텍처를 이용해 관련 파일을 모아라

- 파일 간 코드 공유

  - 내보내기 : 함수, 변수, 클래스를 내보낼 수 있다. 

  ```javascript
  const validator = {
      message: '는 유효하지 않습니다.',
      setInvalidMessage: field => `${field}${this.message}`,
  };
  export { validator };
  
  // 변수 내보내기
  const PI = 3.14;
  const E = 2.71828;
  
  export { E, PI };
  
  // 선언한 객체 파일 끝에 개별적으로 추가하는 대신, 각각의 함수 앞에 export 키워드 추가
  export function capitalize(word) {
      return word[0].toUpperCase() + word.slice(1);
  }
  
  // 내보내기 기본값(export default)을 선언하면 가져오기 과정이 좀 더 짧아진다.
  export default function normalize(address) {
      const street = parseStreet(address);
      const city = address.city;
      const region = parseRegion(address);
      return `${street} ${city}, ${region}`;
  }
  ```

  - 가져오기 : 현재 파일 기준으로 상대 경로로 작성 / 가져오기 기본값은 특히 클래스를 불러올 때 유용하다. 한 개의 파일에는 한 개의 클래스만 두는 것이 좋으므로

  ```javascript
  import { capitalize, roundToDecimalPlace } from './util';
  
  // export default인 함수 가져오기. 중괄호를 사용하지 않으면 내보내기 기본값만 가져온다. 함수 이름도 다르게 사용해도 된다. 
  import normalize from './address';
  
  // export default인 함수와 아닌 함수 혼합해서 가져오기
  import normalize, { parseRegion } from './address';
  ```

  

- npm을 이용해 외부코드 가져오기 : node package manager라는 도구를 이용한다. 페이스북이 만든 yarn처럼 npm을 대체할 수 있는 도구도 존재한다. 대부분 코드를 가져오기 위해 사용하지만 프로젝트 메타데이터와 구성 정보를 설정하고, 명령줄 스크립트 실행, 프로젝트 게시도 할 수 있다. npm을 이용하려면 `Node.js`를 설치해야 한다. Node.js를 설치할 때 npm도 설치된다. -> 프로젝트 초기화를 해야한다. 프로젝트 디렉터리 가장 상위에서 npm init 실행. package.json 파일의 생성을 도와주는 구성도구를 실행한다. 

  - `package.json` : 이름, 설명, 라이선스 등과 같은 프로젝트 메타데이터 정보와 외부 의존성 코드도 포함되어 있다. npm init은 package.json 파일만 생성하고 다른 숨김 파일이나 디렉터리는 생성하지 않는다.
  - 가져와서 쓸 만한 코드를 발견했다면 `npm install --save 이름` 명령을 실행해 설치한다. --save를 반드시 써야하는 건 아니지만 습관이 되면 좋다. npm install 명령은 node_modules 디렉터리가 없으면 생성하고 패키지를 내려받는다. 설치하는 패키지 버전 번호로 package.json파일을 갱신한다. 끝으로 설치하는 코드의 버전에 대한 세부 정보를 담은 package-lock.json 파일을 생성한다. 여기에는 해당 코드가 필요로 하는 다른 라이브러리에 대한 정보도 담겨 있다. 하나의 패키지를 설치할 때 실제로는 여러 개의 패키지를 설치하는 경우도 있다. 함께 설치되는 패키지는 package-lock.json 파일이나 node_modules 디렉터리에서 확인할 수 있고 package.json 파일에는 원래 설치했던 패키지만 표시된다. 

  ```javascript
  // 라이브러리를 설치했기 때문에 경로는 작성하지 않아도 된다. 개별 함수를 불러올 수도 있다.
  import lodash, { fromPairs } from 'lodash';
  ```

  - 테스트 실행기처럼 실환경 코드에서 필요하지 않은 코드는 npm을 이용해 개발 의존성을 다루고 실행할 수 있는 깔끔하게 사용할 수 있다. Prettier도 스타일 가이드에 맞게 코드 서식을 수정하는데 개발에는 필요해도 실환경 코드에는 필요하지 않으므로 `npm install --save-dev prettier`로 설치한다.
  - 전역 모듈로 설치하기 : `npm install -g 이름`
  - prettier로 탭 간격을 공백 네 칸으로 하고 싶다면 npm을 사용해 동일한 명령 실행 시 node_modules 디렉터리에 설치한 패키지를 실행한다. 명령을 실행하려면 package.json 파일의 scripts 필드에 명령을 추가한다. 
  - package.json : npm run clean을 실행하면 Prettier 패키지를 npm이 실행해준다.

  ```javascript
  {
      "name": "test",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
          "clean" : "prettier --tab-width=4 --write ./code/*.js" // 원래 이걸 실행해야 하는데 node_modules에 설치되어 있을 땐 명령줄에서 바로 실행할 수 없어서 이렇게 한다.
      },
      "author": "",
  }
  ```

  
