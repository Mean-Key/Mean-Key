![header](https://capsule-render.vercel.app/api?type=waving&color=6DD5FA&text=%20Open%20Source%20Software%20Term%20Project&height=200&fontSize=40&fontColor=ffffff)
# Card Gatcha & Collecting Web Simulation
포켓몬 카드 웹 시뮬레이션

## 소개
이 프로그램은 주어진 코인을 이용해 포켓몬 카드를 뽑고 수집하는 웹 시뮬레이션입니다. <br>
사용자는 등록된 계정을 통해 로그인하고, 코인을 사용해 얻은 카드로 포켓몬 도감을 완성해 나갈 수 있습니다. <br>
관리자모드로 로그인시 추가적인 기능을 통해 사용자 데이터를 제어할 수 있습니다.

---
## 목차 
1. [개발 목적](#개발-목적)
2. [프로젝트 구조](#프로젝트-구조)     
3. [페이지 구성](#페이지-구성)
4. [주요 구형 기능](#주요-구현-기능)   
5. [기술 스택](#기술-스택)   
6. [실행 화면](#실행-화면)      
7. [참조](#참조)    

## 개발 목적
어렸을적 500원들고 문방구에서 카드를 사던 기억 <br>
사용자의 경험을 극대화하고 포켓몬이라는 친숙한 주제를 통해 수집의 재미를 제공하기 위해 개발되었습니다. 

![moveball](https://github.com/user-attachments/assets/c5efedb6-d6c7-4b85-a01c-2b0b1f4cb1b4)

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
## 페이지 구성

### A. 로그인 페이지 (`login.html`)
- **개발자 계정과 일반 사용자 계정 지원**:
  - 개발자 계정: 고급 기능 및 관리자 권한 제공.
  - 일반 사용자 계정: 기본 게임 및 도감 이용 가능.
- **LocalStorage를 이용한 로그인 유지**.
  - 성공적으로 로그인하면 해당 정보를 URL 쿼리 문자열을 통해 페이지 간 전달.

### B. 메인 페이지 (`main.html`)
- 사용자 로그인 계정에 따른 상태 표시:
  - 관리자는 "개발자님 어서오세요".
  - 일반 사용자는 "어서오세요".
- 메인 페이지로서 다른 페이지로 이동하는 링크 제공: `gamble.html`, `pokedex.html`.

### C. 카드 뽑기 시뮬레이션 페이지 (`gamble.html`)
- 코인을 사용하여 랜덤한 결과를 얻는 카드 뽑기 게임.

- 획득한 카드는 그 자리에서 확인 가능.

### D. 포켓몬 도감 페이지 (`pokedex.html`)
- 포켓몬 150종의 데이터를 기반으로 한 카드 형태의 UI.
- 검색 및 필터링 기능으로 원하는 포켓몬을 쉽게 탐색.
- 획득한 카드는 `미보유 -> 보유` 상태 변경.
<img src="https://github.com/user-attachments/assets/3764d9c1-f5fb-4210-b672-440aef87feb5" width="600" height="400">

---
## 주요 구현 기능
<br>

1. **로그인 및 인증**  
- 개발자 계정과 일반 사용자 계정 구분
      
      개발자 계정 : seoultech | 암호 : 1234
     
      일반 계정 : qwer | 암호 : 1234

- 로그인 성공 시 사용자 정보 저장 및 페이지 전환
- 비 로그인상태에서 `login.html`외 다른 페이지 방문시 로그인 페이지로 자동이동 
<br>

2. **카드 뽑기**  
- 코인을 사용해 5장의 카드를 랜덤으로 획득

- 회득한 카드는 마우스에 의해 확대 및 위치 조절
- 초기 코인 5개 설정
     - 개발자 계정으로 로그인시 코인개수 999개로 변경

<br>

3. **포켓몬 도감**  
- 150마리의 포켓몬에 관한 정보가 있는 `.js`파일과 연동하여 각 포켓몬에 해당하는 정보 이용

- 포켓몬 카드 속성별 필터링 및 이름 번호 검색 기능
- 보유 현황 실시간 반영 ` 보유 카드 / 전체 카드`
- 관리자 로그인시 관리자 전용 ‘모두획득’ 버튼 활성화
- 카드를 클릭하여 확대후 회전시키며 다방향에서 관람가능

<br>

<details><summary> :egg: :egg: :egg:</summary>
<br>

**Easter Egg - 뮤 이벤트**

- 초기상태에선 150마리의 포켓몬 카드만 보임

- 150장의 포켓몬 카드를 모두 모으면 이벤트 발생

- 뮤를 획득하면 전체 카드가 총 `151`장으로 변경
</details>

---
## 기술 스택
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=&logo=html5&logoColor=white) : UI 레이아웃 및 구조 작성.

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=&logo=css3&logoColor=white) : 사용자 친화적이고 반응형 디자인 구현.

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=&logo=javascript&logoColor=%23F7DF1E) : 동적 동작과 사용자 상호작용, 로그인 상태와 사용자 데이터 저장.

---
## 실행 화면

#### 일반 계정 로그인 
![일반_로그인](https://github.com/user-attachments/assets/e541e634-1be2-4ca4-8e11-bd49092e387a)

#### 일반 계정 카드 뽑기
[![Pokedex Page](img/sample_pokedex.png))](https://github.com/user-attachments/assets/7dc804b0-3829-42fd-8298-5f7b2b1e6402)

- 코인 5개, 코인이 0개가 되면 카드 뽑기 불가

#### 일반 계정 포켓몬 도감
![일반_도감](https://github.com/user-attachments/assets/fce451e6-ed46-4049-8e46-3b5a70b6f1be)

- ALL 버튼 비활성화

#### 관리자 카드 뽑기
![개발자_카드](https://github.com/user-attachments/assets/125f4f2a-ac9b-47ad-a979-4563a152ab1e)

- 코인 999개
  
#### 포켓몬 도감 페이지
https://github.com/user-attachments/assets/18b10782-bc87-466a-b894-41ea01271271

#### 뮤 이벤트
https://github.com/user-attachments/assets/83bea38b-0655-4802-b5aa-9cb1ef1d10c6

---
## 참조
https://poke-holo.simey.me/ - 3D 회전 아이디어 참조<br>

<br>   

![footer](https://capsule-render.vercel.app/api?section=footer&type=waving&color=6DD5FA)
