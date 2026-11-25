---
title: "Product Owner - Examples - Task - Design Briefing Single App"
description: "Instantiates Task Templates section 7, Design Briefing. Shows one app with no audience labels, two link blocks and a Contrast facet."
contextType: general
importance_tier: normal
trigger_phrases: ["design briefing single app example"]
version: 0.17.0.1
---

# Briefing - Creator - Chat - Frosted Glass Surfaces

## About
* * *
Chat in the Creator app draws its glass surfaces with a third-party library that mimics Apple liquid glass. It causes contrast issues in chat, and we have no real control over how it renders.

Every chat surface that uses the liquid glass moves to the frosted glass from DS Variables v1.2.0, so chat glass follows our own tokens. The library stays installed, because other screens still use it.

## Briefing
* * *
*   The design starts from the chat components on the DS Chat page and swaps their glass for the frosted glass
*   Chat uses the light frosted glass only, so the dark background and border stay out of chat
*   Readability over whatever sits behind a surface comes before matching the old glass look
*   Screens outside chat keep the liquid glass and are out of scope for design

#### **References**
* * *
*   [DS - Design System: Chat](https://www.figma.com/design/XZfiyOGBp4wAKxhnl2V2ek/%E2%80%A2-DS---Design-System?node-id=103620-2286346&t=XsGwsE4uNDnMJjUC-1)
*   [background | glass effect](https://www.figma.com/design/XZfiyOGBp4wAKxhnl2V2ek/%E2%80%A2-DS---Design-System?node-id=115254-66607&t=Z6lLXWgg1NkKlNhH-1)

#### **Related tasks**
* * *
*   `DS - Variables - v1.2.0 - Creator - Frosted Glass, Effects & Button Gap Update`

## Requirements
* * *
**Display**
- [] The inputs use the frosted glass: text, expanded, audio and emoji search
- [] The overlays use the frosted glass: the upload menu, the context pill and the focused chat modal
- [] The search action bar and the rich text action bar use the frosted glass
- [] Each surface carries the frosted glass background, border and blur together, never only some of them
- [] The stacked context pill shows the pills behind the front one as glass too

**Contrast**
- [] Text and icons on every surface stay readable over a dark chat background, a light one and a photo

## Deliverables
* * *
- [] Each surface over a dark background, a light one and a photo
- [] Each input in its enabled and active states, marking which states carry the frosted glass shadow
- [] The single and stacked context pill
