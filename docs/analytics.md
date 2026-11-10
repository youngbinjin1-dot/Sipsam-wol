# 분석(GA4) 설정

덜내요 프로토타입(`src/prototype/index.html`)의 사용 데이터를 Google Analytics 4로 측정합니다.

| 항목 | 값 |
|---|---|
| 측정 ID | `G-0JRX0EMYMS` |
| 관리자 화면(속성 사용자 관리) | https://analytics.google.com/analytics/web/provision/#/a415645979p563481818/admin/suiteusermanagement/property |

관리자 화면은 구글 계정으로 로그인하고 권한이 있는 사람만 열 수 있습니다. 보고 싶은 팀원은 위 화면에서 사용자로 추가해야 합니다.

## 보내는 이벤트

개인정보와 입력한 금액(연봉, 월세 등)은 보내지 않고, 화면 이름과 클릭 여부만 보냅니다.

| 이벤트 | 언제 | 무엇을 보려고 |
|---|---|---|
| `screen_view` (`screen_name`) | 화면이 바뀔 때마다 | 단계별 이탈률 (`start` → `consent` → `toss` → `found` → `qRent` … → `result` → `plan` → `saved` → `home`) |
| `mvp_link` | 토스 데이터 연동에 동의했을 때 | 연동 동의율 |
| `slider_touch` | 지출 계획 슬라이더를 처음 움직였을 때 (한 번) | 슬라이더 사용률 |
| `recommend_ratio` | 추천 비율로 맞췄을 때 | 추천 기능 사용 |
| `big_spend_add` | 큰 지출을 추가했을 때 | 큰 지출 입력 사용 |
| `mvp_plan` | 계획을 저장했을 때 | 계획 저장률 |
| `mvp_sheet` | 문턱 알림 시트가 떴을 때 | 전환 알림 도달 |
| `report_view` | 12월 마무리 리포트를 봤을 때 | 리포트 도달 |
| `mvp_sub_remind` | 구독 알림을 신청했을 때 | 구독 관심 |
| `mvp_helper` | 도우미를 끝냈을 때 | 도우미 완료율 |

## 확인 방법

1. 배포된 주소(`http` 또는 `https`)로 앱을 엽니다. 파일을 더블클릭해서 열면 기록되지 않습니다.
2. GA4 → 보고서 → 실시간에서 방문과 이벤트가 몇 분 안에 보이는지 확인합니다.
3. 클릭률을 보려면 GA4 관리 → 이벤트에서 `mvp_plan`, `mvp_link` 등을 "주요 이벤트"로 표시합니다.

## 열린 문제

- 방문자 데이터가 구글 서버로 전송됩니다. 쿠키 동의 배너와 개인정보 처리방침 문구가 필요한지 정해야 합니다.
- 다른 페이지(`promo/fakedoor-metrics/index.html`)는 팀 내부용 지표 시트라서 GA를 넣지 않았습니다.
