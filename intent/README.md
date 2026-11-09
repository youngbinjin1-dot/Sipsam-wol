# intent/ — 모든 intent는 여기에

> 한 기능 = 한 폴더. intent·spec·plan이 함께 움직인다.
> 사람이 쓴 intent도, 에이전트가 만든 intent도 같은 곳에 쌓여 한 번에 검색·리뷰된다.

## 폴더 이름 규칙

```
intent/YYYY-MM-DD-영문-슬러그/
```

- 날짜는 **폴더를 만든 날**. 작성자가 달라도 날짜+슬러그라 겹치지 않는다.
- 슬러그는 영문 소문자·숫자·하이픈만 쓴다. (예: `2026-11-09-dulnaeyo-mvp`)
- 새 폴더는 [`_template.md`](_template.md)를 복사해 `intent.md`로 시작한다. 팀 공통 스킬 `.claude/skills/write-intent/`를 쓰면 같은 규칙으로 만들어진다.

## 폴더 안 파일

| 파일 | 필수 | 내용 |
|---|---|---|
| `intent.md` | ✅ | 무엇을, 왜 (한 문장 의도·대상·하지 않을 것·성공 기준) |
| `spec.md` | 선택 | 요구사항과 디자인 결정 (화면·동작·계산) |
| `plan.md` | 선택 | 구현 계획 (단계·체크리스트·위험) |
| `prd.md` | 선택 | 긴 제품 요구사항 문서가 따로 있을 때 |

구현물(HTML·코드·토큰)은 `src/`에, 장애·회고는 `lessons/`에 둔다.

## 상태 정의

각 `intent.md` 맨 위 메타에 `상태:`를 적는다.

| 상태 | 뜻 |
|---|---|
| `draft` | 작성 중. 리뷰 요청 전 |
| `review` | PR 올림. PO 승인 대기 |
| `approved` | PO 승인. spec·plan 작업 가능 |
| `in-progress` | 구현 중 |
| `done` | 출시·검증 완료 |
| `dropped` | 접음 (이유를 intent.md 끝에 남긴다) |

## 현재 intent 목록

| 폴더 | 내용 | 파일 | 상태 |
|---|---|---|---|
| [`2026-11-09-year-end-tax-toss-inapp`](2026-11-09-year-end-tax-toss-inapp/) | 덜내요 — 토스 인앱 연말정산 예상·카드 사용 슬라이더 (11월 시즌 버전) | intent · spec · prd | in-progress |
| [`2026-11-09-instagram-fakedoor-test`](2026-11-09-instagram-fakedoor-test/) | 인스타그램 페이크 도어 테스트 — 이메일 사전 신청으로 수요 확인 | intent | approved |
| [`2026-11-09-dulnaeyo-mvp`](2026-11-09-dulnaeyo-mvp/) | 덜내요 MVP — 페이크 도어 랜딩 + 앱 모의실행 (`src/mvp-dulnaeyo/`) | intent · spec · plan | in-progress |

> 상태 값은 정리하면서 붙인 초기값이다. 맞지 않으면 PO가 고쳐 주세요.

## 리뷰

`intent/` 아래 변경은 `.github/CODEOWNERS`에 따라 **PO가 승인**한다. 리뷰 기준은 저장소 루트 [`REVIEW.md`](../REVIEW.md).
