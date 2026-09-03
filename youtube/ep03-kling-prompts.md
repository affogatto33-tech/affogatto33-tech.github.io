# EP.03 — Kling 프롬프트 세트

대본 실측 타임코드 매칭. **Kling 11클립** + 그래픽. 총 5분 13초.

## 0. 고정 스타일 토큰 (1·2편과 동일 — 절대 바꾸지 말 것)

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

---

## 1. 클립 목록

### K-01 · [00:00–00:12] 훅 — 결과지의 한 줄
```
A stapled report lying on a desk seen from a steep side angle so print is
illegible, a single line marked with a faint red highlight, warm lamp light,
camera pushes in extremely slowly, macro, very shallow focus
```
`10초 · 175는 편집에서 합성`

### K-02 · [00:12–00:35] 훅 — 갈림길
```
A quiet road forking into two paths in soft morning haze, both paths equally
lit and inviting, no signage, no people, camera static wide, muted tones
```
`10초 · 같은 지점에서 두 갈래. 어느 쪽도 어둡게 만들지 말 것`

---

### K-03 · [00:35–00:50] 챕터1 — 운반
```
Small glass beads travelling along a narrow transparent tube, steady and
unhurried, soft backlight making the tube glow faintly, macro, camera
tracks alongside slowly
```
`10초 · LDL = 배달의 시각화`

### K-04 · [00:50–01:05] 챕터1 — 회수
> **의도**: K-03과 같은 튜브, 방향만 반대. 대비가 핵심이니 연속 생성하세요.
```
The same transparent tube, beads now travelling in the opposite direction
and fewer in number, dimmer backlight, macro, camera tracks alongside slowly
```
`10초 · K-03의 프레임을 참조로 쓰면 연속성이 삽니다`

### K-05 · [01:05–01:18] 챕터1 — 쌓임
```
Fine sediment slowly settling and building up along the inner wall of a
narrow glass tube, the passage gradually narrowing, cool clinical light,
macro, camera locked off, very slow
```
`10초 · 혈관 내부를 직접 그리지 말고 유리관으로 은유. 혐오감 방지`

---

### [01:18–02:10] 챕터2 위험 조건 → **그래픽 (핵심 화면)**
> 조건(심혈관 병력·당뇨·고혈압·흡연·가족력)을 하나씩 쌓으면서
> 목표선이 내려가는 애니메이션. **이 편에서 가장 중요한 화면입니다.**
> 대본의 `〈 위험군별 목표치 표 〉` 표시 지점이 여기입니다.
> Kling 불필요.

### K-06 · [02:10–02:22] 챕터2 — 생활습관 경로
```
A pair of worn walking shoes by a door in early morning light, laces loose,
one turned slightly as if just set down, camera pushes in low and slow
```
`10초`

### K-07 · [02:22–02:33] 챕터2 — 약 경로
```
A small unlabelled white pill bottle on a clean surface beside a glass of
water, soft window light, camera slowly orbits, macro, label turned away
```
`10초 · 라벨 노출 금지. 특정 제품이 보이면 의료광고 문제가 됩니다`

---

### K-08 · [02:33–02:50] 챕터3 — 식사
```
A simple home meal on a wooden table, grilled fish, vegetables and a small
bowl of rice, warm natural light from the side, camera slowly pushes in,
shallow focus, no hands in frame
```
`10초`

### K-09 · [02:50–03:05] 챕터3 — 운동
```
Low angle following shot of legs walking briskly along a tree-lined path in
autumn light, dappled shadows moving across the ground, camera tracks
forward at knee height
```
`10초 · 무릎 아래만. 얼굴 없음 포맷 유지`

### K-10 · [03:05–03:32] 챕터3 — 유전
> **의도**: "의지가 아니라 타고난 차이"를 말이 아니라 그림으로.
```
Two nearly identical potted seedlings side by side in the same light and
same soil, one noticeably taller than the other, soft window light, camera
slowly slides right, shallow focus
```
`10초 · 같은 조건, 다른 결과`

---

### [03:32–04:24] 챕터4 오해 → **그래픽 + 스톡**
> 오해 세 가지는 텍스트 모션으로 처리하는 게 빠릅니다.
> 달걀·튀김 이미지가 필요하면 Pexels 무료 푸티지로 대체하세요.

### K-11 · [04:24–04:45] 마무리 — 상담
```
A quiet consultation desk with two empty chairs facing each other, a folded
document and a pen resting on the surface, soft window light, camera pushes
in very slowly, warm and calm, no people
```
`10초 · "결과지 들고 오세요" CTA의 배경`

---

### [04:45–05:13] 마무리 → **그래픽 + K-01 재사용**
> 요약 3줄 + CTA. 배경에 K-01을 흐리게 재활용해 수미상관.

---

## 2. 화면 배분

| 소스 | 분량 | 비중 |
|---|---|---|
| Kling 생성 (11클립) | 약 110초 | 35% |
| 그래픽 · 텍스트 모션 | 약 145초 | 46% |
| 스톡 · 재사용 | 약 58초 | 19% |

## 3. 생성 순서

1. **K-03 → K-04를 먼저.** 같은 튜브로 방향만 바꾸는 게 제일 어렵습니다.
   K-03 확정 후 마지막 프레임을 K-04의 참조 이미지로 쓰세요.
2. K-01, K-06, K-07, K-08, K-11은 정물이라 실패율이 낮습니다. 묶어서 큐 투입.
3. K-05, K-10은 은유라 2~3회 재생성 예상.
4. **크레딧이 빡빡하면 K-09(걷기)를 Pexels로 대체**하세요. 11 → 10클립.

## 4. 재생성 판단 기준

- 약병에 라벨·글자가 생겼다 ← **이 편에서 가장 위험한 실패**
- 종이에 글자 비슷한 형체가 생겼다
- K-05가 혐오스럽게 나왔다 → `glass tube` 를 더 강조해 재생성
- 손가락 기형 · 모핑 · 과채도 · 카메라 과속
