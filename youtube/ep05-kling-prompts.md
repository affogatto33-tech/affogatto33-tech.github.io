# EP.05 — Kling 프롬프트 세트

대본 타임코드에 1:1 매칭. **Kling 생성 14클립** + 스톡/그래픽 슬롯 표기.

---

## 0. 고정 스타일 토큰 (모든 프롬프트에 그대로 붙일 것)

편 전체의 톤을 일관되게 유지하는 장치입니다. **한 글자도 바꾸지 마세요.**

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

### 반드시 지킬 3가지

1. **화면에 글자를 만들지 마세요.** Kling은 한글은 물론 영문도 깨뜨립니다.
   숫자·기준표는 전부 편집 단계에서 얹으세요. (그래서 `no text`가 스타일 토큰에 있습니다)
2. **얼굴 클로즈업을 피하세요.** 손·뒷모습·어깨 아래·사물 위주로 갑니다.
   얼굴 없는 채널 포맷과도 맞고, 기형 생성 리스크도 없앱니다.
3. **가능하면 Image-to-Video를 쓰세요.** 정지 이미지를 먼저 확정한 뒤 움직임만 주면
   재생성 횟수가 절반으로 줄어듭니다. Text-to-Video는 구도 통제가 어렵습니다.

---

## 1. 클립 목록

각 프롬프트는 `[내용] + STYLE` 형태로 넣고, 네거티브는 위 블록을 그대로 사용합니다.

### K-01 · [00:00–00:06] 오프닝 훅 — 결과지
> **의도**: 시청자가 방금 겪은 장면을 그대로 재현해 즉시 몰입시킨다.
```
Close-up of a hand holding a plain white medical checkup report sheet on a
wooden kitchen table, morning light from a side window, the paper trembles
very slightly, camera slowly pushes in on the sheet, extremely shallow focus
```
`5초 · Image-to-Video 권장 · 카메라: 느린 push in`

### K-02 · [00:06–00:12] 훅 — 혈압계
```
A digital blood pressure monitor resting on a table, the cuff coiled beside
it, screen dark and blank, camera slowly orbits from left to right,
soft window light raking across the plastic surface
```
`5초 · 화면은 반드시 꺼진 상태로 (숫자 생성 방지). 130/85는 편집에서 합성`

### K-03 · [00:12–00:22] 훅 — 지구본 전환
> **의도**: "나라를 건너면 병명이 바뀐다" 를 물리적으로 보여준다.
```
A small vintage desk globe slowly rotating, Korea peninsula turning away and
North America turning into view, warm desk lamp light from the upper left,
dust motes floating in the beam, camera locked off, very slow rotation
```
`10초 · 회전 속도가 빠르면 재생성. "very slow" 유지`

---

### [00:22–00:48] 도입 → **그래픽 구간** (Kling 미사용)
> 챕터 3개를 텍스트 모션으로 순차 노출. 편집 프로그램에서 처리.

---

### K-04 · [00:48–00:58] 챕터1 — 심장 박동
```
Abstract anatomical heart shape made of soft translucent material,
gently contracting and expanding in a slow steady rhythm, floating in a
dark teal void, subtle rim light outlining the form, macro lens, camera static
```
`5초 · 해부학적 사실성보다 리듬감 우선. 징그럽지 않게 "translucent" 필수`

### K-05 · [00:58–01:12] 챕터1 — 수축기
```
Interior view of a blood vessel, smooth glossy pink-red walls, a strong
pressure wave surging through and pushing the walls outward, camera travels
forward through the tunnel, soft internal glow, slow motion
```
`10초 · 카메라: dolly forward`

### K-06 · [01:12–01:26] 챕터1 — 이완기
> **의도**: K-05와 같은 공간, 압력만 낮은 상태. 대비가 핵심이므로 **연속 생성**할 것.
```
Interior view of the same blood vessel, the wave has passed, walls settling
back but still held slightly open under residual pressure, camera drifts
forward slowly, dimmer internal glow, calm
```
`10초 · K-05 결과물을 첫 프레임으로 Image-to-Video 하면 연속성이 살아납니다`

### K-07 · [01:26–01:45] 챕터1 — 뻣뻣해진 혈관
```
Two glass tubes side by side, the left one soft and flexible bending gently,
the right one rigid and brittle with fine hairline cracks, cool studio light
on a matte grey backdrop, camera slowly slides right, macro
```
`10초 · 비교 구도. 좌=정상 우=경직. 편집에서 라벨 얹기`

---

### [01:45–03:20] 챕터2 기준표 → **그래픽 구간** (Kling 미사용)
> 5단계 기준표를 정지 이미지 + 느린 줌으로 처리. 이 구간은 **정보 밀도가 높아
> 영상이 움직이면 방해**됩니다. 표를 화면에 띄우고 항목별로 하이라이트만 이동시키세요.

### K-08 · [03:05–03:20] 챕터2 마무리 — '나쁜 쪽 기준'
```
Two identical brass balance scales on a dark table, the left pan level and
still, the right pan slowly tipping down and settling, single warm spotlight
from above, deep shadows, camera slowly pushes in
```
`5초 · "나쁜 쪽으로 분류된다" 의 은유`

---

### K-09 · [03:20–03:35] 챕터3 — 갈림길
```
An empty road forking into two paths in soft morning fog, one path leading
toward a quiet park, the other toward a clinical white building, camera
static at the fork, cool desaturated light, no people
```
`10초 · 좌=생활습관 우=약물치료. 인물 넣지 말 것`

### K-10 · [03:35–03:55] 챕터3 — 예외 조건
```
A stack of transparent glass panes on a light table, each pane etched with
faint abstract line patterns, layering one over another to build density,
soft overhead light, camera slowly tilts down, minimal
```
`5초 · "조건이 겹칠수록 위험도가 올라간다" 의 추상 표현`

### K-11 · [03:55–04:15] 챕터3 — 체중 감량
```
Worn running shoes by an apartment doorway in early morning light, laces
loosely tied, one shoe slightly turned as if just placed down, camera slowly
pushes in low to the ground, warm side light, quiet domestic mood
```
`5초`

### K-12 · [04:15–04:30] 챕터3 — 저염식
```
A small ceramic dish of coarse salt on a wooden counter, a hand entering
frame and setting the salt shaker aside out of reach, natural kitchen light,
camera static, shallow focus on the salt
```
`5초 · 손은 프레임 가장자리에서 짧게만. 손가락 클로즈업 금지`

### K-13 · [04:30–04:45] 챕터3 — 걷기
```
Low angle following shot of legs briskly walking along a tree-lined park
path, autumn morning light filtering through leaves, dappled shadows moving
across the ground, camera tracks steadily forward at knee height
```
`10초 · 무릎 아래만. 얼굴 미노출 포맷 유지`

---

### K-14 · [04:45–05:45] 챕터4 — 집에서 재기
```
A quiet living room corner in soft morning light, an armchair with a small
side table holding a blood pressure monitor and a notebook, the chair empty,
sheer curtain moving slightly, camera very slowly pushes in
```
`10초 · 이 클립을 챕터4 배경으로 깔고, 4가지 수칙은 텍스트 모션으로 얹으세요.
클립 하나로 60초를 버티게 하는 구간입니다 (속도 0.5배 + 루프)`

---

### [05:45–06:10] 마무리 → **그래픽 + K-01 재사용**
> 요약 3줄을 텍스트로 노출하고, 배경에 K-01(결과지)을 흐리게 재활용해 수미상관.
> **재사용은 낭비가 아니라 구성입니다.** 크레딧을 아끼는 가장 확실한 방법.

---

## 2. 생성 순서 (크레딧 절약)

1. **먼저 K-05를 뽑습니다.** 이게 이 편에서 가장 어려운 클립입니다.
   여기서 톤이 결정되면 나머지가 쉬워집니다.
2. K-05가 확정되면 **마지막 프레임을 캡처해 K-06의 시작 이미지**로 씁니다.
3. K-01, K-02, K-11, K-12, K-14는 **사물 정물**이라 실패율이 낮습니다. 묶어서 한 번에 큐 투입.
4. K-03, K-04, K-08, K-10은 **추상/은유**라 2~3회 재생성을 예상하세요.
5. K-09, K-13은 **스톡 푸티지로 대체 가능**합니다.
   Pexels에서 "forest path fork", "walking legs autumn" 검색 → 무료.
   → 크레딧이 빡빡하면 **이 둘부터 스톡으로 돌리세요. 14클립 → 12클립.**

## 3. 재생성 판단 기준

아래에 하나라도 걸리면 그냥 다시 뽑으세요. 편집으로 못 살립니다.

- 화면에 글자·숫자 비슷한 형체가 생겼다
- 손가락이 5개가 아니거나 관절이 꺾였다
- 클립 중간에 물체가 다른 물체로 변형(morphing)된다
- 카메라가 예상보다 빠르다 → 프롬프트에 `very slow` 추가 후 재생성
- 색이 튄다(과채도) → 네거티브에 `oversaturated` 가 들어갔는지 확인
