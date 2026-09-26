# Product Owner - Examples - Story - Medium Tier - v0.300

Instantiates the house Story shape at medium size: three safeguards on one settings form, with Requirements carrying only the hard constraints each control has to satisfy and outcome-led acceptance criteria grouped by surface, and no Delivery section, so the artifact ends on Acceptance criteria.

---

# Lumen - Profile settings - Identity updates

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The profile-settings form lets a member update their avatar, display name and login email. Each control fails at a different point today, and the failures surface at different moments: an avatar saves uncropped, a display name is rejected only on submit, and an email change applies before the owner can react. This story adds three independent safeguards so each control keeps its promise.

#### Problem
* * *
Each profile control breaks its own promise:
*   Avatar uploads save the raw image with no cropping, so off-center photos reach other members' feeds
*   Display-name errors only surface after the member tries to save, forcing guess-and-check
*   Email changes take effect the instant they are submitted, so a stolen session can move the login email before the owner notices

#### Solution
* * *
Catch each problem at the field where it starts instead of at the moment of saving. The avatar, display name and email address fail for unrelated reasons, so each gets a safeguard fitted to it rather than one generic validation pass:
*   The avatar is framed by the member before it is saved
*   The display name is checked as it is typed
*   An email change is confirmed from the address that is being replaced

**Expected outcomes**
* * *
*   Avatars reach other members' feeds with the framing the member chose
*   Display-name errors resolve while typing, not after submit
*   No email change lands without the owner confirming from the address on file

#### **References**
* * *
Components
*   [Page | Profile settings](https://design.lumen.example/profile-settings)
Flows
*   [Profile identity updates](https://design.lumen.example/flows/profile-identity)
* * *
##   

## Requirements
* * *
**Avatar image**
* * *
- [] A source photo smaller than `256x256` is not accepted
- [] The stored avatar is a square crop of at least `256x256`
- [] Only the cropped result is stored, never the raw upload

**Display name**
* * *
- [] Length is `3` to `30` characters after trimming
- [] Allowed characters are letters, numbers, spaces and `. ' - _`

**Email change**
* * *
- [] The confirmation link goes to the address on file, never to the requested address
- [] A pending change expires `24h` after it is requested
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Avatar
* * *
1\. **An avatar reaches other members with the framing the member chose**
* * *
*   **Given** the member picks a photo for their avatar
*   **When** they frame it and confirm
*   **Then** the avatar appears everywhere in exactly the framing they chose, square and sharp at the size other members see it
*   **And** a photo too small to make a usable square is refused before framing, with "Choose a photo at least 256 x 256 pixels." and the previous avatar left in place
* * *
- [] _Mark as done, if the criteria are met_

#### Display name
* * *
2\. **Display-name problems surface while typing, not after saving**
* * *
*   **Given** the member is editing their display name
*   **When** the value falls outside what the field accepts
*   **Then** the member sees which rule it breaks while they are still typing, and the save action is unavailable until it is fixed
*   **And** no invalid name can be saved by any route, including pressing Enter
* * *
- [] _Mark as done, if the criteria are met_

#### Email change
* * *
3\. **A login email moves only when the owner allows it**
* * *
*   **Given** a member requests to change their login email from `ana@example.com` to `ana.rivera@example.com`
*   **When** the request is submitted
*   **Then** `ana@example.com` keeps working as the login email, and the change lands only after the owner confirms from that address
* * *
- [] _Mark as done, if the criteria are met_

4\. **An unconfirmed email change lapses on its own**
* * *
*   **Given** a pending email change nobody confirmed
*   **When** it passes its expiry
*   **Then** the pending change is discarded and the login email stays `ana@example.com`
*   **And** the member is told the link expired and that a fresh request is the way forward
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
