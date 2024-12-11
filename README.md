# Card Web Simulation
포켓몬 카드 웹 애플리케이션

## 소개
이 프로젝트는 코인을 이용해 포켓몬 카드 뽑아 수집하는 웹 시뮬레이션입니다. <br>
사용자는 로그인하여 자신의 계정을 관리하고, 코인을 통해 얻은 카드로 포켓몬 도감을 완성해 나갈 수 있습니다. <br>
관리자는 추가적인 기능을 통해 사용자 데이터를 제어할 수 있습니다.

---
## 목차   
- [페이지 구성](#-페이지-구성)   
- [프로젝트 구조](#-프로젝트-구조)   
- [기술 스택](#-기술-스택)   
- [실행 화면](#-실행-화면)      
- [참조](#-참조)    

## 페이지 구성

### 1. 로그인 페이지 (`login.html`)
- **개발자 계정과 일반 사용자 계정 지원**:
  - 개발자 계정: 고급 기능 및 관리자 권한 제공.
  - 일반 사용자 계정: 기본 게임 및 도감 이용 가능.
- **LocalStorage를 이용한 로그인 유지**.
  - 성공적으로 로그인하면 해당 정보를 URL 쿼리 문자열을 통해 페이지 간 전달.

### 2. 메인 페이지 (`main.html`)
- 사용자 로그인 상태에 따라 다음 메시지 표시:
  - 관리자는 "개발자님 어서오세요".
  - 일반 사용자는 "어서오세요".
- 주요 기능으로의 링크 제공: `gamble.html`, `pokedex.html`.

### 3. 카드 뽑기 시뮬레이션 페이지 (`gamble.html`)
- 코인을 사용하여 랜덤한 결과를 얻는 간단한 슬롯 머신 게임.
- 관리자 계정으로 로그인 시 시작 코인을 999개로 설정.
- 게임 결과에 따라 코인이 증가하거나 감소.

### 4. 포켓몬 도감 페이지 (`pokedex.html`)
- 포켓몬 151종의 데이터를 기반으로 한 카드 형태의 UI.
- 검색 및 필터링 기능으로 원하는 포켓몬을 쉽게 탐색.
- 관리자는 모든 필터 버튼 옆에 "모두획득" 버튼으로 데이터를 조작 가능.
- 마우스 호버 시 상세 정보 표시.
- 151번째 카드를 보유하면 특별한 이벤트 표시.

## 프로젝트 구조
```
Project/
├── img
│   ├── symbol
│   │   ├── RED.png
│   │   └── ...
│   ├── poke151
│   │   ├── SV2a_001.png
│   │   ├── SV2a_002.png
│   │   └── ...
|   ├── etc
│   │   ├── cardpack.png
│   │   ├── pokeball.png
│   │   └── ...
├── music
│   ├── main.mp3
│   │   └── ...
├── main.html
├── pokedex.html
├── gamble.html
├── 151data.js
```
- 파일을 구조와 동일한 형태로 저장 후 프로그램 실행 권장
---

## 기술 스택
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=&logo=html5&logoColor=white) : UI 레이아웃 및 구조 작성.

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=&logo=css3&logoColor=white) : 사용자 친화적이고 반응형 디자인 구현.

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=&logo=javascript&logoColor=%23F7DF1E) : 동적 동작과 사용자 상호작용, 로그인 상태와 사용자 데이터 저장.

---

## 실행 화면

#### 로그인 페이지
![Login Page](img/sample_login.png)

#### 메인 페이지
![Main Page](img/sample_main.png)

#### 도박 게임 페이지
![Gamble Page](img/sample_gamble.png)

#### 포켓몬 도감 페이지
![Pokedex Page](img/sample_pokedex.png)

### 데모 영상
[![Watch the video](img/sample_video_thumbnail.png)](https://youtu.be/sample_video_link)

---

## 참조
이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

<br>   
