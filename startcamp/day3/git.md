[TOC]

- [Git](#git)
  * [1. 준비](#1-준비)
  * [2.  Local Repository](#2--local-repository)
    + [2.1 저장소 초기화](#21-저장소-초기화)
      - [2.1.2 그 외 작업](#212-그-외-작업)
    + [2.2 `add`](#22--add-)
    + [2.3 `commit`](#23--commit-)
  * [3. Remote Repository](#3-remote-repository)
    + [3.1 준비](#31-준비)
    + [3.2 원격 저장소 등록](#32-원격-저장소-등록)
    + [3.3 `Push`](#33--push-)
  * [4.Clone & Pull](#4clone---pull)
  * [5. 과거로 돌아가기](#5-과거로-돌아가기)
    + [reset](#reset)
  * [6. 충돌](#6-충돌)
    + [revert](#revert)
    + [history 삭제](#history-삭제)
  * [7.branch](#7branch)
    + [7-1. HEAD](#7-1-head)
    + [7-2. Merge](#7-2-merge)
    + [7-3. 기능별 push](#7-3-기능별-push)
    + [7-4. 다른사람과 함께 하면서 기능 push](#7-4-다른사람과-함께-하면서-기능-push)

# Git

> Git은 분산 버전 관리 시스템(DVCS)이다.
>
> 소스코드의 이력을 추적 & 관리한다. 개인 프로젝트 뿐만 아니라 협업 단계에서도 활용된다. 

<br/>

## 1. 준비

- 윈도우에서 git을 사용하기 위해서 `git bash`를 설치한다.

- git을 활용하기 위해서 GUI 툴인 `source tree`, `github desktop`등을 활용할 수도 있다. 

- 초기 설치를 완료한 이후에 컴퓨터에 작성자(author) 정보를 등록한다.

  ```bash
  # author 정보 등록
  $ git config --global user.name {user name}
  $ git config --global user.email {user email}
  
  # author 정보 확인
  $git config --global --list
  ```

<br/>

## 2.  Local Repository

<br/>

### 2.1 저장소 초기화

``` bash
$ git init
```

- `.git` 폴더가 생성되면, 이 곳에 git 관련된 정보가 저장된다.
- git bash에 `(master)`라고 표시된다. 이는 현재 master라는 branch에 있다는 뜻이다. 

<br/>

#### 2.1.2 그 외 작업

```bash
$ touch .gitignore
```

- git으로 관리 안할 파일을 따로 정리하기 위해 만들어준다.
- ignore파일에서 직접 파일명을 적거나 *.txt처럼 특정 확장자를 전부 관리 안하도록 할 수 있다.
- gitignore.io 사이트에서 python, visualstudiocode, windows등의 키워드를 입력해서 자동으로 관리 안할 파일을 설정해 주면 편하다.

<br/>

### 2.2 `add`

현재 작업 공간(working directory)에서 변경된 사항을 커밋으로 기록하기 위해서는  `staging area`를 거쳐야한다.

``` bash
$ git add . # 현재 디렉토리
$ git add images/ # 특정 폴더
$ git add hamster.jpg # 특정 파일
```

<br/>

### 2.3 `commit`

`commit`은 이력을 확정짓는 명령어다. 해당 시점의 스냅샷을 기록한다.

`commit`시에는 반드시 메시지를 작성해야하며, 메시지는 변경사항을 알 수 있도록 명확하게 작성한다.

```bash
$ git commit -m 'startcamp 소스코드 추가'
```

`commit`이후에는 아래의 명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log

$ git log --oneline # log 깔끔하게 보기
```

<br/>

## 3. Remote Repository

> 원격 저장소 기능을 제공하는 서비스에는 `Github`, `Gitlab`등이 있다.
>
> 우리는 그 중에서 가장 범용적으로 사용되는 Github를 활용한다.

<br/>

### 3.1 준비

- Github에 새로운 Repository 생성

<br/>

### 3.2 원격 저장소 등록

- git remote : 원격 저장소 관리 명령어, origin이라는 이름으로 주소를 등록한다.(다른 이름 가능). origin이라는 원격 저장소를 지우고 싶다면 git remote remove origin

```bash
$ git remote add origin (github url)

# [참고] 서로다른 원격 저장소를 사용하고 싶으면 이름을 다르게 연결시킨다.
$ git remote add github (github url)
$ git remote add gitlab (gitlab url)

$ git push github master
$ git push gitlab master
```

- 원격 저장소(`remote`)로 `origin`이라는 이름을 가진 `github url`을 등록(`add`)한다.
- 등록된 원격 저장소 목록을 보기 위해선 아래 명령어를 입력한다.

``` bash
$ git remote -v
```

<br/>

### 3.3 `Push`

```bash
$ git push origin master
```

- `origin`이라는 이름으로 설정된 원격 저장소에  `master` 브랜치를 업로드(`push`)
- 이후 변경사항이 생길 때마다 add -> commit -> push 순으로 작업을 수행한다.

<br/>

## 4.Clone & Pull

```bash
$ git clone url name # 클라이언트 상에 아무것도 없을 때 서버의 프로젝트를 내려받는 명령어. 저장소 내용을 다운받고 자동으로 init 된다. 어떤 이름인지 지정가능
$ git pull origin master # 다른 사람이 코드를 업데이트 했거나 commit했을 때 클라이언트로 내려받는 명령어
```

<br/>

## 5. 과거로 돌아가기

<br/>

- 5-1. staging area에 있던(add로 추가했던) 파일을 처음으로 제거 : working directiory로 돌아감

```bash
$ git rm --cached a.txt
```

- 이후에 a를 수정하고 다시 add하고 status를 보면 restore,reset(버전에 따라 다른 말이 나오지만 같다.)을 하라고 한다. 

<br/>

- 5-2. commit 작성하면서 오타가 들어갔을 때 : 가장 마지막 commit만 취소할 수 있다.

```bash
$ git commit --amend
```

- 저걸 입력하면 vim이 켜진다. 
- vim : 텍스트 에디터, 입력 모드와 이동 모드가 존재한다. 
  - 입력 모드(데이터 추가) : i 
  - 입력모드에서 내가 입력한 commit 멘트를 수정한다.
  - 입력 모드 취소 : esc
  - 저장 : `:wq` (write quit)

<br/>

- 5-3. 파일을 추가하지 않고 commit했을 때 : amend사용

- 다시 add해서 안 올린 파일을 올린 다음에 amend를 실행해서 전에 commit된 파일을 내리고 같이 올리기

```bash
$  git commit --amend
```

<br/>

### reset

- 5-4. 며칠 전 commit으로 돌아가기 (주의해서 사용하기. 안쓰는 걸 추천)

- git log --oneline을 보면 각 commit마다 고유한 key값을 가지고 있는 걸 볼 수 있다.

```bash
# commit 과거로 돌아감, 파일에서 내가 간 시점 이후 내용은 다 사라짐. add기록까지 삭제
$ git reset --hard (내가 가고싶은 커밋 이름, 지우기 직전 시점)

# commit은 과거로 돌아갔지만 status에서 보면 파일은 수정되지 않았음. add 기록은 남아있음.
$ git reset --soft (내가 가고싶은 커밋 이름, 지우기 직전 시점)

# default가 mixed라 안써도 됨. status에서 보면 파일이 수정되었다고 나옴. add 전단계 까지?
$ git reset --mixed (내가 가고싶은 커밋 이름, 지우기 직전 시점)
```

<br/>

## 6. 충돌

- git lab에서 web ide를 통해 바로 파일 수정 가능하다.
- 그런데 git lab에서 수정하고 커밋한 뒤 로컬에서 똑같이 수정한 후 커밋하면 내용은 같아도 history가 서로 달라 push가 할 수 없다.
- 마스터라는 큰 줄기에서 gitlab줄기와 나의 로컬 컴퓨터 줄기가 따로 있다. 이 두 버전을 하나로 먼저 합쳐야 한다.

```bash
$ git push origin master
To https://lab.ssafy.com/ubik0408/branch.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://lab.ssafy.com/ubik0408/branch.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
# pull 먼저 해보지 않을래?
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

$ git pull origin master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
...
# 충돌 발생
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

<br/>

- 파일에서 <<<와 ===을 지워야 한다. vs code상에서 보면 Compare Change, Aceept Both Changes, Accept Current Changes, Accept Incoming Changes 를 선택해서 편하게 볼 수 있다!

```markdown
<<<<<<< HEAD (Current Change), local에서 수정한 내용
# README

1. 프로젝트 진행.
======= 
1. 프로젝트 진행.
>>>>>>> 709995603fd1115b402d0c58dc73a5fab04af338(Incoming Change), WEB IDE에서 수정한 내용

```

<br/>

- bash에서 보면 뒤에 merging이 붙었다. 수정을 마치고 파일을 다시 commit하고 나면 사라져있다.

```bash
pcasj@DESKTOP-7F9IK5U MINGW64 ~/branch (master|MERGING)
```

<br/>

### revert

- reset대신 revert를 사용하면 충돌났을 때 처럼 변해보인다.
- reset과 가장 큰 차이는 code history인데 코드 자체는 과거로 돌아갔지만 revert가 history에 남고 과거 commit 기록도 남아있다.

<br/>

### history 삭제

- 그냥 .git을 지워버리면 된다.

```bash
$ rm -rf .git
```

<br/>

## 7.branch

- commit을 한 번이라도 해야 branch 목록을 볼 수 있다.

```bash
# 확인
$ git branch
* master

# 생성
$ git branch jin

# 이동 (더 명시적이라 주로 사용)
$ git switch jin
Switched to branch 'jin'

# 이동 2
$ git checkout jin
Switched to branch 'jin'

...@DESKTOP-7F9IK5U MINGW64 ~/branch (jin)

# 삭제
$ git branch -d jin
Deleted branch jin (was f338b7b).
```

<br/>

### 7-1. HEAD

- branch를 하나 더 만들고 commit한 뒤 log로 확인하면 HEAD가 나온다.

```bash
$ git log --oneline
216550e (HEAD -> master, jin) update README
f338b7b add README

$ git switch jin
Switched to branch 'jin'

# HEAD의 순서가 바꼈다.
$ git log --oneline
216550e (HEAD -> jin, master) update README
f338b7b add README

# 파일 수정 후 다시 커밋하고 보면 jin만 HEAD랑 한 단계 더 간 걸 볼 수 있다. 파일 수정하고 커밋안하고 master로 돌아가려고 하면 안됨
$ git log --oneline
2d0e9ad (HEAD -> jin) fix README
216550e (master) update README
f338b7b add README

# 그리고 다시 master로 이동한 순간 수정한 파일 내용이 사라지고 commit history에서도 안보인다.
# master에서 merge. 병합 후 보면 HEAD가 master도 가리키고 있다.
$ git merge jin
Updating 216550e..2d0e9ad
Fast-forward
 README.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
 
 # jin은 한 기능을 만들기 위해 뻗어나온 가지였기 때문에 병합을 마친 후에 삭제한다.
```

<br/>

### 7-2. Merge

- 이번엔 위에 동일하지만 기능을 위해 만든 feature/login과 별개로 master에서도 자신의 작업을 수행한 상태다.(서로 다른 파일)

```bash
$ git merge feature/login
Merge made by the 'recursive' strategy.
 views.py | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
 
 # 이번엔 log를 보면서 graph도 함께 본다. 기본 줄기에서 뻗어나와서 생긴 변화를 다른 형태로 볼 수 있다.
 $ git log --oneline --graph
*   5ce5eaa (HEAD -> master) Merge branch 'feature/login'
|\
| * bb8e0c8 (feature/login) 로그인 완성:
* | 7436f7b 필요없는 문장 삭제
|/
* 1d2e8ac update views.py
* 2d0e9ad fix README
* 216550e update README
* f338b7b add README
```

<br/>

- 그런데 두 명이 같은 파일을 수정했다면? 충돌발생

```bash
$ git merge feature/signup 
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

# 이 경우엔 회원가입 기능했던 게 더 중요하니까 그걸 선택하고 다시 commit하고 log를 보면
$ git log --oneline --graph
*   f10b662 (HEAD -> master) feature/login branch merge
|\  
| * c793250 (feature/signup) README 작성
| * 0571736 회원가입 기능 완성
* | ff96fe3 README.md
|/
* a6e2a96 회원가입
*   5ce5eaa Merge branch 'feature/login'
|\
| * bb8e0c8 로그인 완성:
* | 7436f7b 필요없는 문장 삭제
|/
* 1d2e8ac update views.py
* 2d0e9ad fix README
* 216550e update README
```

<br/>

### 7-3. 기능별 push

- test라는 branch를 만들어 test 기능을 구현하고 push한다.

```bash
$ git branch feature/test
$ git switch feature/test 
Switched to branch 'feature/test'

$ git add .
$ git commit -m "test기능"
[feature/test 3192fb5] test기능
 1 file changed, 4 insertions(+), 1 deletion(-)

$ git push origin feature/test
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.    
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 331 bytes | 110.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0        
remote: 
remote: To create a merge request for feature/test, visit:
remote:   https://lab.ssafy.com/ubik0408/branch/merge_requests/new?merge_request%5Bsource_branch%5D=feature%2Ftest
remote:
To https://lab.ssafy.com/ubik0408/branch.git     
   d035f52..3192fb5  feature/test -> feature/test
```

- 이제 원격저장소에 들어가보면 branch가 matser말고 feature/test도 선택할 수 있다. 그리고 로컬이 아닌 원격저장소에서 병합할 수 있게 됐다.

- 웹에서 병합하기 : merge request만들기 버튼 클릭 -> source branch는 test, target brach가 master로 되어있다. (local에서의 git merge feature/test같은거) -> 최종 merge버튼 클릭
- 이제 Repository -> Branches에 보면 feature/test는 merged되어있다. 그리고 삭제 버튼이 활성화되어있다. 할 일이 끝났으니 지울 수 있다는 뜻

- 그런데 이건 원격저장소 일이고 로컬에서 다르다. 현재 로컬에서만 병합하는 걸 추천한다.

```bash
# 여기선 색이 안보이지만 초록색이 local, 빨간색이 원격저장소
$ git log --oneline --graph
* 3192fb5 (HEAD -> feature/test, origin/feature/test) test기능
* d035f52 (origin/master, master) test

$ git pull origin master
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (1/1), 256 bytes | 23.00 KiB/s, done.
From https://lab.ssafy.com/ubik0408/branch
 * branch            master     -> FETCH_HEAD
   d035f52..c089fde  master     -> origin/master
Updating 3192fb5..c089fde
Fast-forward

$ git log --oneline --graph
*   c089fde (HEAD -> feature/test, origin/master) Merge branch 'feature/test' into 'master'
|\
| * 3192fb5 (origin/feature/test) test기능
|/
* d035f52 (master) test
```



### 7-4. 다른사람과 함께 하면서 기능 push

- local에서
  - a -> siwtch master -> git merge fature/signup -> git push origin master (signup 올림)
  - b -> git pull origin master(feature/login상태에서 하면 안됨. master상태에서 해야함, 충돌 일어남.), signup master에 받아옴 -> 그 다음 git merge feature/login -> git push origin master (signup + 내 login 올림)
  - a -> git pull origin master (로그인 추가됨)

