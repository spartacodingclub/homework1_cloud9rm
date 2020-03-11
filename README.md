# Web Study Homework #1

1주차 과제 
-
원페이지 쇼핑몰의 메인 페이지 제작
* 상품: 8주 완강 후 나에게 하고 싶은 선물
* 부트스트랩 또는 템플릿 활용 
* Git Push 제출

TIP
-
VS Code 단축키
* `shift + alt + f` : 자동 정렬
* `ctrl + /`, `cmd + /`: 주석 처리
* `ctrl + z`, `cmd + z`: Undo(실행취소)
* `ctrl + shift + z`, `cmd + shift + z`: Redo(재실행)

1주차 수업 목표
-
1. 서버와 클라이언트의 역할에 대해 이해한다.
2. HTML, CSS의 기초 지식을 이해한다. 부트스트랩을 가져다 쓸 줄 안다!
3. 해커정신(검색하면 다 된다!)을 체험하고, 몸에 익힌다.

1주차 학습 내용 
-
* HTML & CSS 
    * HTML: 뼈대, CSS: 꾸미기
    * HTML 구성
        * Head: 페이지 속성 정보
        * Body: 페이지 내용
        * Tag, Attributes, Contents 
        ```
        <tag attributeKey="attributeValue"> Contents </tag> 
        ```
    * CSS 구성
        * 선택자로 선택
        * class 는 그룹, id는 유일
        * Selector, Property
        ```
        selector { 
            propertyKey: propertyValue
        }
        ```
        ```
        <tag class="className" id="idName"></tag>

        tag { }
        .className { }
        #idName { }
        ```
    * 주석 처리 `ctrl + /` , `cmd + /`

* Bootstarp
    * CSS를 이용하여 디자인을 미리 만들어 둔 것
        * Url: https://getbootstrap.com/
    * 적용
    ```
    <!doctype html>
    <html lang="en">
        <head>
            <!-- Webpage Title -->
            <title>Hello, world!</title>

            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            
            <!-- JS -->		
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            
        </head>
        <body>
            <h1>Hello, world!</h1>
        </body>
    </html>
    ```

* Git
    * 버전 관리 시스템
    * `git commit`: 저장
    * `git push`: 원격저장소 업로드
    * `git pull`: 원격저장소 다운로드
