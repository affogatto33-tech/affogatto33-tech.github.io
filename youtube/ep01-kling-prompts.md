# EP.01 — Kling 프롬프트 세트

대본 실측 타임코드에 1:1 매칭. **Kling 12클립** + 스톡/그래픽 슬롯.
총 5분 04초 (304초).

---

## 0. 고정 스타일 토큰 (모든 프롬프트에 그대로 붙일 것)

편 전체 톤을 일관되게 유지하는 장치입니다. **한 글자도 바꾸지 마세요.**
2편 이후에도 같은 토큰을 써야 채널 전체가 한 덩어리로 보입니다.

```
STYLE:
clean modern medical documentary, soft diffused natural window light,
muted palette of teal / warm beige / off-white, shallow depth of field,
slow deliberate camera movement, photorealistic, cinematic 24fps,
no text, no logos, no on-screen writing
```

```
NEGATIVE PROMPT:
text, letters, numbers, watermark, logo, subtitles, signage,
distorted hands, extra fingers, deformed anatomy, warped face, morphing,
oversaturated colors, neon, cartoon, anime, 3d render look,
low resolution, flicker, jitter, fast cuts, crowded frame
```

### 반드시 지킬 4가지

1. **화면에 글자를 만들지 마세요.** Kling은 한글은 물론 영문도 깨뜨립니다.
   날짜·수치·기준은 전부 편집 단계에서 얹으세요.
2. **얼굴 클로즈업을 피하세요.** 손·뒷모습·어깨 아래·사물 위주.
   얼굴 없는 채널 포맷과 맞고, 기형 생성 리스크도 없앱니다.
3. **주사 바늘을 화면에 크게 넣지 마세요.** 주사 공포가 있는 시청자가
   이탈합니다. 백신 바이알, 알코올 솜, 접종 후 밴드 정도로 대체합니다.
4. **가능하면 Image-to-Video를 쓰세요.** 정지 이미지를 먼저 확정한 뒤 움직임만
   주면 재생성 횟수가 절반으로 줍니다.

---

## 1. 클립 목록

각 프롬프트는 `[내용] + STYLE`, 네거티브는 위 블록 그대로.

### K-01 · [00:00–00:08] 훅 — 9월의 아침
> **의도**: 계절 전환을 몸으로 느끼게 해서 "지금이 그 시기"임을 각인.
```
Early autumn morning light through a window, a thin cotton cardigan draped
over the back of a chair, faint condensation on the glass, dust motes
drifting in the beam, camera pushes in very slowly, quiet domestic mood
```
`5초 · Image-to-Video 권장`

### K-02 · [00:08–00:18] 훅 — 달력
```
A wall calendar page turning slowly by itself in still air, pages settling,
soft side light raking across the paper texture, camera locked off, macro,
extremely shallow focus on the page edge
```
`10초 · 날짜 숫자는 편집에서 합성. 프롬프트에 숫자를 넣지 말 것`

### K-03 · [00:18–00:27] 훅 — 백신 바이알
```
A small glass vaccine vial standing on a stainless steel tray beside a
folded alcohol swab, cool clinical light from above, faint reflections on
the metal, camera slowly orbits left to right, macro, no needle in frame
```
`10초 · 바늘 금지. "no needle in frame" 반드시 유지`

---

### [00:27–00:50] 도입 → **그래픽 구간** (Kling 미사용)
> 오늘 다룰 세 가지를 텍스트 모션으로 순차 노출.

---

### K-04 · [00:50–01:00] 챕터1 — 겨울 거리
```
A city street in early winter seen from a distance, people walking bundled
in coats, breath visible in the cold air, muted grey blue tones, camera
static wide shot, shallow focus, no recognizable faces
```
`10초 · 12월 1차 유행 구간의 배경. 얼굴 식별 안 되게 원경 유지`

### K-05 · [01:00–01:10] 챕터1 — 초봄 거리
> **의도**: K-04와 같은 구도, 계절만 다르게. 2차 유행을 대비로 보여줍니다.
```
The same city street in early spring, thin bare branches beginning to bud,
people in lighter jackets, pale warm light, camera static wide shot,
shallow focus, no recognizable faces
```
`10초 · K-04의 첫 프레임을 참조 이미지로 쓰면 구도가 맞습니다`

### [01:10–01:35] 챕터1 — **그래픽 구간**
> 유행 곡선(12월 피크 + 2~3월 피크)과 항체 지속 구간(2주 후 시작 → 6개월)을
> 겹쳐 그리는 애니메이션. **이 편에서 가장 중요한 화면입니다.**
> Kling으로 만들 수 없고, 만들어서도 안 됩니다. 편집 프로그램에서 직접 그리세요.

### K-06 · [01:35–01:45] 챕터1 — 9월 접종 시나리오
```
A single sturdy umbrella opened and standing upright on a wooden floor,
soft rain shadows moving across the wall behind it, warm interior light,
camera slowly pushes in, calm and reassuring
```
`10초 · "미리 준비해두면 덮인다"의 은유`

### K-07 · [01:45–01:59] 챕터1 — 11월 접종 시나리오
```
A closed umbrella lying flat on a wet entryway floor, rain already visible
through the open doorway behind it, cool light, camera slowly pulls back,
slight sense of being late
```
`10초 · K-06과 대비. 같은 우산, 접힌 상태`

---

### [01:59–02:47] 챕터2 무료 대상 → **그래픽 구간 + 스톡**
> 세 그룹(어린이·임신부·어르신)은 아이콘 + 텍스트로 처리.
> 인물 영상이 필요하면 Pexels 무료 푸티지로 대체하세요.
> Kling으로 사람을 만들면 손·얼굴 기형 리스크만 커집니다.

---

### K-08 · [02:47–02:57] 챕터3 — 오해 1
```
A sealed glass vial on a clean surface, perfectly still, a soft light
sweeping slowly across it from one side to the other, nothing moving
inside, macro, camera locked off
```
`10초 · "살아있는 바이러스가 없다" = 정지·밀봉의 시각화`

### K-09 · [02:57–03:15] 챕터3 — 오해 2
```
Three identical glass vials in a row on a steel tray, lit one after another
by a slow moving light, each one slightly different in tone, camera slides
right at constant speed, macro
```
`10초 · 매년 새 백신. 3개 = 3개 절기`

### K-10 · [03:15–03:44] 챕터3 — 오해 3
```
Two contrasting still lifes side by side on a table, left a crumpled tissue
and a warm mug, right a folded blanket and a thermometer, soft window light,
camera slowly slides from left to right, shallow focus
```
`10초 · 감기(좌) vs 독감(우). 편집에서 라벨 얹기`

---

### K-11 · [03:44–04:10] 챕터4 — 진료실 대기
```
A quiet clinic waiting area with empty chairs in a row, soft natural light
from a tall window, a low table with neatly stacked magazines, warm and calm,
camera pushes in extremely slowly, no people
```
`10초 · 이 클립을 챕터4 앞부분 배경으로 깔고 4가지 수칙은 텍스트로 얹으세요.
속도 0.5배 + 루프로 26초를 버팁니다`

### K-12 · [04:10–04:34] 챕터4 — 접종 후
```
A small round adhesive bandage on a folded shirt sleeve resting on a chair
arm, soft afternoon light, gentle shadow, camera very slowly pushes in,
macro, calm and ordinary
```
`10초 · 접종 완료의 상징. 팔뚝 피부 클로즈업은 피하고 옷 위주로`

---

### [04:34–05:04] 마무리 → **그래픽 + K-01 재사용**
> 요약 3줄을 텍스트로 노출하고, 배경에 K-01(9월 아침)을 흐리게 재활용해 수미상관.
> **재사용은 낭비가 아니라 구성입니다.** 크레딧을 아끼는 가장 확실한 방법.

---

## 2. 화면 배분 점검

| 소스 | 분량 | 비중 |
|---|---|---|
| Kling 생성 (12클립) | 약 115초 | 38% |
| 그래픽 · 텍스트 모션 | 약 110초 | 36% |
| 스톡 푸티지 | 약 50초 | 16% |
| 재사용 · 정지+줌 | 약 30초 | 10% |

Kling 12클립이면 반나절 작업입니다. 격주 페이스가 유지됩니다.

## 3. 생성 순서 (크레딧 절약)

1. **K-04와 K-05를 먼저** 뽑습니다. 같은 구도로 계절만 바꾸는 게 이 편에서 가장
   어렵습니다. K-04 확정 후 그 프레임을 참조로 K-05를 뽑으세요.
2. K-01, K-02, K-03, K-08, K-09, K-12는 **사물 정물**이라 실패율이 낮습니다. 한 번에 큐 투입.
3. K-06, K-07(우산)은 **은유**라 2~3회 재생성을 예상하세요.
4. **크레딧이 빡빡하면 K-06·K-07부터 잘라내세요.** 나레이션만으로도 전달됩니다.
   12클립 → 10클립.

## 4. 재생성 판단 기준

아래에 하나라도 걸리면 다시 뽑으세요. 편집으로 못 살립니다.

- 화면에 글자·숫자 비슷한 형체가 생겼다
- **주사 바늘이 프레임에 들어왔다**
- 손가락이 5개가 아니거나 관절이 꺾였다
- 클립 중간에 물체가 변형(morphing)된다
- 카메라가 예상보다 빠르다 → 프롬프트에 `very slow` 추가 후 재생성
