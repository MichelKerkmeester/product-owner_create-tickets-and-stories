**Write gate.** The page in `<draft-file-key>` is empty, so no section there shares a title with either board.

**Question:** which screens does a new person pass through from the Loomlist landing page to the editor, and where do they choose?

**Outcome:** a product team can check each choice and the one error branch against the build.

**Sketch.** This is the checked model, with 6 nodes and 7 connectors on board 1, and 7 nodes and 9 connectors on board 2.
```text
1. Sign up (LR)
Landing page -> Which method? -(Email)-> Email code
                              -(Google)-> Email code
Email code -> Right code? -(Yes)-> Email verified
                          -(No)-> Wrong code error -(Resend)-> Email code

2. Workspace setup (LR)
Email verified -> Which plan? -(Free)-> Name workspace
                              -(Team)-> Add emails? -(Add emails)-> Teammates' emails -> Name workspace
                                                    -(Skip)-> Name workspace
Name workspace -> Start from? -(Template)-> Editor with welcome tip
                              -(Blank)-> Editor with welcome tip
```

**Glances**
- Board 1
  - First: "Right code?", the accented decision
  - Second: Landing page, Which method?, Email code, Email verified
  - Last: Wrong code error, drawn beside the row
- Board 2
  - First: "Which plan?", the accented decision
  - Second: Email verified, Add emails?, Teammates' emails, Name workspace, Start from?, Editor with welcome tip
  - Last: no node sits off the row, because the Free and Skip shortcuts are labelled edges

**Writes**
- Plan: Loomlist Product, as you named it. I haven't checked it with `whoami`, because writing into an existing file needs no plan.
- File: the existing FigJam file `<draft-file-key>`
- Content: two composed boards, each a new section with a title, subtitle, key and source line, at Laptop distance. Board 2 lands 400 pixels to the right of board 1.
- Existing content: none, so nothing already there changes.
- Extensions: none

**Left out**
- Workspace setup, split into "2. Workspace setup"
- Field-level detail, returning-user sign-in and any error beyond the wrong code
- Whether a Google sign-up skips the email code, because the doc doesn't say. I drew both methods leading to the code screen.
- The doc's status is assumed to be current behavior.

**Calls**
- Spent so far: `create_session` and one `get_figjam` read
- Still to spend: two `use_figma` calls, one per board, and one `get_figjam` read-back. A timeout could add a retry.
- Allowance: on a Starter plan or a View or Collab seat, Figma limits tool calls to six a month, and reads count against that.

**Rollback:** delete the two sections the write returns. That needs your yes to a question that names them.

Write both boards to this file?