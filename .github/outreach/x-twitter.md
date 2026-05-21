# Outreach draft — X (Twitter)

> **Status**: draft, not submitted. Maintainer reviews + posts manually.
> Identity-bound channel — do not delegate posting to an agent.

## Why X

Fastest broadcast for the EN agentic-AI community (the same crowd that
amplifies on HN / Reddit also lives here in shorter form). What X does
well: identity-signal-driven discovery (a PhD researcher posting a
curated learning artifact is read very differently from an anonymous
account), image-driven engagement (link cards + banner = ~2× CTR), and
quote-retweet amplification by mid-tier AI accounts. What X does poorly:
depth (280-char ceiling), context (no threading culture for awesome-list
type artifacts), and persistence (24-48h half-life).

Risk: X is also where overclaim and self-promotion are punished hardest.
Lead with the artifact, not adjectives.

## Pre-flight (verify before posting)

These are already shipped (`44b1cbe`), but re-check the live preview
before you tweet — X's card scraper caches aggressively:

- [ ] X card preview for `github.com/WenyuChiou/awesome-agentic-ai-zh`
      shows EN-lead description (paste URL into a draft tweet first, eyeball
      the card; if zh-TW-lead, the cache hasn't refreshed — wait ~1h or
      re-share via the Pages URL)
- [ ] Your X bio matches the LinkedIn reframe (PhD, Civil & Environmental,
      Lehigh · agent-based modeling · LLM / AI agent). Identity coherence
      across platforms is the discovery multiplier on X
- [ ] `banner.en.png` is uploaded as the tweet image (drag-attach, not URL
      auto-card — image attachment outperforms link card for first impression)

## Tweet options (pick one; no emoji-spam, no hype, ≤ 280 chars)

### A — EN-lead, broad AI audience (recommended)

```
A trilingual (EN / 繁中 / 简中) learning roadmap for agentic AI — staged
tracks for CLI power users and agent builders, 5 audience branches
(researcher / dev / teacher / knowledge worker / everyday user), 23
hands-on exercises (Ollama-default — no API key needed to start).

github.com/WenyuChiou/awesome-agentic-ai-zh
```

### B — research-first (matches your LinkedIn reframe)

```
PhD student working on agent-based flood-adaptation modeling. Open-
sourced the agentic-AI curriculum I built for my own learning —
trilingual (EN / 繁中 / 简中), 8 stages + 2 tracks + 5 audience branches
+ 23 exercises.

github.com/WenyuChiou/awesome-agentic-ai-zh
```

### C — bilingual lead (CJK AI-Twitter circle: 寶玉 / AK / 向阳乔木)

```
做了個三語 Agentic AI 學習路線圖（繁中 / 简中 / EN 全維護）:雙軌（CLI 使用者 / Agent 開發者）+ 5 個對象分支 + 23 個動手練習,預設 Ollama 本機跑,免 API key。

A trilingual agentic-AI roadmap — github.com/WenyuChiou/awesome-agentic-ai-zh
```

Recommended: **A** for the first push (EN-lead is where the audience is
and the meta tags are now aligned). Consider **C** as a separate post
~1 week later targeting CJK AI Twitter — different audience, different
time window, doesn't compete with the EN push.

## Timing

- **A (EN)**: weekday 08:00–10:00 US Eastern (US AI Twitter morning;
  overlaps EU evening). Avoid Fri PM / weekends.
- **C (CJK)**: weekday 20:00–22:00 Beijing time (CN evening; overlaps TW
  prime time).
- Don't post both same day — collisions hurt both.

## First-reply (optional, post yourself ~5 min after main tweet)

Use this only if engagement is picking up and a clarifier would unlock
more clicks. Don't pre-load it if the main tweet flops.

```
A few things that aren't obvious from the README:
- Stage 0 is for non-coders (web/desktop on-ramps before any CLI).
- Examples default to local Ollama, not paid APIs — the cloud path is
  the alt, not the default.
- The English edition is fully maintained alongside the Chinese
  canonical, gated by CI (anchor + locale checks).
```

## Image / link strategy

- **Attach**: `resources/diagrams/banner.en.png` (the 2026-05-13 ChatGPT-
  rendered EN banner, already in repo).
- **Link in tweet body**: `github.com/WenyuChiou/awesome-agentic-ai-zh`
  — GitHub URL beats Pages URL because the ★ count is the trust signal
  EN readers scan for. (Pages URL `wenyuchiou.github.io/awesome-agentic-ai-zh/en/`
  is a fallback if you want to land EN readers on an English doc page
  directly.)
- **No hashtags** in the main tweet — the audience is already targeted
  by who follows you and who you quote-mention. Hashtags dilute the
  reach signal more than they add discovery on X today.

## Engagement tactics (light)

- Quote-RT one of your own older posts about agent stuff with the new
  URL, ~6h after main tweet, if first push got <20 likes (re-broadcast,
  don't ask for boost)
- If a mid-tier AI account QTs you, reply with a *specific* follow-up
  (a stage they'd find useful for their audience), not a generic
  "thanks"
- If someone says "is the English just machine-translated?" — point them
  to the CI lint config + the audit comment in the HN draft. Don't
  defensively re-explain in the main thread.

## Don'ts

- ❌ Don't say "the best / definitive / world-class / production-grade"
- ❌ Don't lead with the ★ count (let the GitHub card show it)
- ❌ Don't @-mention famous AI accounts asking for amplification
- ❌ Don't post the same content to LinkedIn the same day (cross-platform
  redundancy on the same hour smells like a launch campaign, not an
  individual sharing). Stagger 24-48h
- ❌ Don't reuse the same tweet text after a flop — rewrite if going
  for a second push
- ❌ Don't post C and A on the same day (different audiences, but
  appearing twice in the same feed reads as spam)
