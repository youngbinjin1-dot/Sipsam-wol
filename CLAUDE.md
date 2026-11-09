# CLAUDE.md

덜내요(가제) — 토스 인앱 연말정산 예상·절세 파트너 기획 저장소.

## 저장소 구조

| 경로 | 무엇 |
|---|---|
| `intent/` | 모든 intent. 한 기능 = 한 폴더(`YYYY-MM-DD-슬러그/`), 안에 intent·spec·plan. 규칙은 `intent/README.md` |
| `src/` | 구현물. `src/index.html` 앱 모의실행, `src/mvp-dulnaeyo/` 페이크 도어·MVP, `src/tokens/` 디자인 토큰 |
| `lessons/` | 회고·장애 사후 분석 |
| `docs/` | 시장분석, 카드뉴스, 회의록, 페르소나, 디자인 시스템, 사업계획 |
| `REVIEW.md` | 리뷰 기준 |
| `.github/CODEOWNERS` | `intent/` 리뷰어 = PO |

## 작업 규칙

- 새 intent는 `.claude/skills/write-intent/` 스킬로 만든다. 같은 기능 폴더가 있으면 그 안을 고친다.
- intent를 바꾸면 같은 폴더의 spec·plan도 맞춰 고친다.
- 금액은 모두 "예상·추정", 보장 표현 금지. 세무 상담·신고 대행 아님. 추가 소비 유도·금융상품 추천 금지.
- 문서는 한국어, 쉬운 말로 쓴다.
