# Product Owner - Examples - Task - DS Variables - v0.100

Instantiates Task Templates sections 3 and 4 in the ClickUp format the team ships, a Parent Task with one Subtask per app. Shows a design token release listed once in the parent while each app's subtask carries its own token file and the checks that file needs.

---

# DS - Variables - v1.0.7 - Size Variables & Disabled States

## About
* * *
v1.0.7 changes 34 Button and Label size values. It also renames `--states-border-disabled` to `--states-border-disabled-base` with the same color and adds `--states-border-disabled-light`. Every other token keeps its name and every existing color keeps its value, so the only reference change is moving code off the old disabled border name.

*   Partner reads `barter-ds-variables.css`
*   Creator reads `barter-ds-variables.ts`

Each app lands v1.0.7 in its own subtask, the tables below are the full change list for both.
###   

#### Variables
* * *

[barter-ds-variables--v1.0.7.ts](clickup-attachment-url)

[barter-ds-variables--v1.0.7.css](clickup-attachment-url)

###   

### Requirements
* * *
**1\. Partner App integration**
* * *
- [ ] Integrate `barter-ds-variables--v1.0.7.css` in the Partner app

**2\. Creator App integration**
* * *
- [ ] Integrate `barter-ds-variables--v1.0.7.ts` in the Creator app
###   

### **Change Overview**
* * *
1\. **Button - Size Token Changes**
* * *

| Size | `button-content-gap` | `button-text-link-content-gap` | `button-content-text-size` |
| ---| ---| ---| --- |
| Extra Small | `0.25rem` | unchanged | unchanged |
| Small | `0.25rem` | `0.25rem` | body-small (`0.875rem`) |
| Base | `0.3125rem` | `0.3125rem` | unchanged |
| Large | `0.375rem` | `0.375rem` | unchanged |
| Extra Large | `0.4375rem` | unchanged | unchanged |
| Display | `0.5rem` | unchanged | unchanged |
| Display Large | `0.5rem` | unchanged | unchanged |

2\. **Label - Size Token Changes**
* * *

| Size | `label-content-text-size` | `label-padding-left`, `label-padding-right` | `label-size-icon`, `label-size-icon-close` |
| ---| ---| ---| --- |
| Extra Large | body-large (`1.125rem`) | `0.75rem` | `1.125rem` |
| Display | body-large (`1.125rem`) | `0.75rem` | `1.125rem` |
| Display Large | body-large (`1.125rem`) | `0.75rem` | `1.125rem` |

| Size | `label-size-container` | `label-border-size` |
| ---| ---| --- |
| Extra Large | `2rem` | unchanged |
| Display | `2rem` | `0.0938rem` |
| Display Large | `2rem` | `0.0938rem` |

3\. **Label Icon - Size Token Changes**
* * *

| Size | `label-icon-hori-size-icon` | `label-icon-hori-size-container`, `label-icon-verti-size-container` |
| ---| ---| --- |
| Extra Large | `1.125rem` | `2rem` |

4\. **States - Disabled Border Tokens**
* * *
The 21 disabled state tokens that read `--states-border-disabled` now read `--states-border-disabled-base`, so they keep the same color. Nothing reads `--states-border-disabled-light` yet.

| Token | Change | Value |
| ---| ---| --- |
| `--states-border-disabled-base` | Replaces `--states-border-disabled` | `var(--border-neutral-base)`, `#cfcfcf` |
| `--states-border-disabled-light` | New | `var(--border-neutral-light)`, `#e8e8e8` |

<!-- Subtask 1 of 2: Partner app, which reads the CSS token file -->

# DS - Variables - v1.0.7 - Partner App

* * *
### About
* * *
Partner reads its design tokens from `barter-ds-variables.css`.
This subtask lands v1.0.7 there. The parent task lists every changed value.

#### Variables
* * *

[barter-ds-variables--v1.0.7.css](clickup-attachment-url)

### Requirements
* * *
**Update the CSS token file**
* * *
Size values change in place, so Partner components pick them up with no reference changes.
The rename is the exception:
*   A Partner style that still reads `--states-border-disabled` gets no value once the old name is gone

**Checklist**
- [ ] `barter-ds-variables.css` carries the 34 v1.0.7 values
- [ ] `--states-border-disabled` replaced by `--states-border-disabled-base`
- [ ] `--states-border-disabled-light` added
- [ ] No Partner code references `--states-border-disabled` any more

<!-- Subtask 2 of 2: Creator app, which reads the TS token file -->

# DS - Variables - v1.0.7 - Creator App

* * *
### About
* * *
Creator reads its design tokens from `barter-ds-variables.ts`.
This subtask lands v1.0.7 there. The parent task lists every changed value.

#### Variables
* * *

[barter-ds-variables--v1.0.7.ts](clickup-attachment-url)

### Requirements
* * *
**Update the TS token file**
* * *
Size values change in place, so Creator components pick them up with no reference changes.
The rename is the exception:
*   Creator code that still reads `STATES.Border.Disabled` or `--states-border-disabled` breaks once the old name is gone

**Checklist**
- [ ] `barter-ds-variables.ts` carries the 34 v1.0.7 values
- [ ] `STATES.Border.Disabled` replaced by `STATES.Border.DisabledBase`
- [ ] `STATES.Border.DisabledLight` and `BORDER_STATES.DisabledLight` added
- [ ] `FLAT_TOKEN_MAP` carries the same 34 values
    - [ ] `--states-border-disabled` replaced by `--states-border-disabled-base`
    - [ ] `--states-border-disabled-light` added
- [ ] No Creator code references `STATES.Border.Disabled` or `--states-border-disabled` any more
