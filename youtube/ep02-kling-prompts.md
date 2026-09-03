# EP.02 — Kling 프롬프트 세트

대본 실측 타임코드에 매칭. **Kling 10클립** + 그래픽. 총 4분 50초.

> **이 편은 정보 밀도가 높아 그래픽 비중이 큽니다.** 판정 구분표, 다섯 줄 하이라이트가
> 핵심 화면이고, Kling은 그 사이를 잇는 역할입니다. 클립 수를 억지로 늘리지 마세요.

## 0. 고정 스타일 토큰 (1편과 동일 — 절대 바꾸지 말 것)

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

**주의**: 이 편은 소재가 "종이 문서"라 Kling이 글자를 만들려는 압력이 강합니다.
`no text`가 있어도 새어 나옵니다. **결과지는 항상 뒷면·측면·접힌 상태로**
프롬프트를 쓰고, 실제 수치는 편집에서 얹으세요.

---

## 1. 클립 목록

### K-01 · [00:00–00:12] 훅 — 봉투
```
A plain white envelope resting unopened on a kitchen table, morning light
from a side window, one corner slightly lifted, camera pushes in extremely
slowly, shallow focus, quiet anticipation
```
`10초 · 검진 결과지가 도착한 순간`

### K-02 · [00:12–00:30] 훅 — 펼쳐진 서류
```
Stapled sheets of paper fanned open on a wooden table seen from a steep
side angle so the printed surface is not legible, warm lamp light raking
across the paper grain, camera drifts slowly right, macro, very shallow focus
```
`10초 · 글자가 안 읽히는 각도가 핵심. 빨간 표시는 편집에서 합성`

---

### [00:30–00:49] 도입 → **그래픽**
> 오늘 다룰 세 가지를 텍스트 모션으로.

### [00:49–01:42] 챕터1 판정 구분 → **그래픽 (핵심 화면)**
> 정상A / 정상B / 질환의심 / 유질환자 네 칸을 만들고 하나씩 밝힙니다.
> **정상B에서 멈추고 강조**하세요. 이 편에서 가장 중요한 순간입니다.
> Kling 불필요. 만들지 마세요.

### K-03 · [01:30–01:42] 챕터1 마무리 — 갈림길
```
Three stacked paper trays on a desk, the middle one holding a single sheet
while the others are empty, soft overhead light, camera slowly tilts down,
minimal composition
```
`10초 · "정상B는 따로 기억해 둔다"의 시각화`

---

### K-04 · [01:42–01:54] 챕터2 — 전날 술
```
An empty wine glass and a water glass side by side on a counter at night,
window reflection behind them, cool blue tone, camera static, macro,
shallow focus on the rims
```
`10초`

### K-05 · [01:54–02:08] 챕터2 — 전날 운동
```
Running shoes and a crumpled towel by a doorway in dim early light, faint
steam rising from a nearby mug, camera pushes in low and slow
```
`10초`

### K-06 · [02:08–02:22] 챕터2 — 공복
```
An empty white ceramic plate with clean fork and knife placed neatly across
it, soft morning light from the left, camera slowly orbits, macro
```
`10초 · 공복 상태의 상징`

### K-07 · [02:22–02:38] 챕터2 — 다시 재기
```
Two identical glass beakers side by side on a lab bench, one being slowly
filled while the other stays still, cool even light, camera locked off,
macro, calm
```
`10초 · "한 번으로 판단하지 않는다"`

---

### [02:38–03:34] 챕터3 다섯 줄 → **그래픽 (핵심 화면)**
> 결과지 이미지 위에서 **다섯 줄만 남기고 나머지를 회색으로** 떨어뜨립니다.
> 한 줄씩 순차 강조하며 각각 다른 영상으로 갈 수 있음을 암시하세요.
> **썸네일도 이 화면으로 만듭니다.**

### K-08 · [03:20–03:34] 챕터3 — 영상 소견
```
A backlit film viewer panel glowing softly in a dim room, a blank
translucent sheet clipped to it, no image content visible, camera pushes in
very slowly, cool clinical light
```
`10초 · 판독 이미지를 만들지 말 것. 빈 필름 + 조명만`

---

### K-09 · [03:34–03:52] 챕터4 — 작년 결과지
```
Two stapled paper documents lying overlapped on a desk, the lower one
slightly yellowed with age, seen from a steep angle so text is illegible,
warm side light, camera slowly slides right
```
`10초 · 작년 것과 올해 것. 색 차이로 시간을 표현`

### K-10 · [03:52–04:08] 챕터4 — 약 목록
```
A few assorted pill bottles and a small notebook with a pen resting on a
kitchen counter, soft window light, camera pushes in slowly, shallow focus,
labels turned away from camera
```
`10초 · 라벨이 안 보이게. 특정 제품 노출은 의료광고 문제가 됩니다`

---

### [04:08–04:50] 마무리 → **그래픽 + K-01 재사용**
> 다섯 줄 요약을 텍스트로 노출하고, 배경에 K-01(봉투)을 흐리게 재활용.
> **CTA는 텍스트로 또렷하게**: "결과지 들고 오세요"

---

## 2. 화면 배분

| 소스 | 분량 | 비중 |
|---|---|---|
| **그래픽 · 텍스트 모션** | 약 155초 | **53%** |
| Kling 생성 (10클립) | 약 100초 | 34% |
| 재사용 · 정지+줌 | 약 35초 | 13% |

**이 편은 그래픽이 절반을 넘습니다.** 정상입니다. 정보 밀도가 높은 편에서
영상이 계속 움직이면 오히려 방해가 됩니다.

## 3. 재생성 판단 기준

- **종이에 글자 비슷한 형체가 생겼다** ← 이 편에서 가장 흔한 실패
- 약병 라벨에 글자가 생겼다
- 필름 뷰어에 판독 이미지가 생겼다
- 손가락 기형 · 모핑 · 과채도

종이·라벨은 전부 **각도를 더 눕히거나 초점을 더 얕게** 해서 재생성하세요.
