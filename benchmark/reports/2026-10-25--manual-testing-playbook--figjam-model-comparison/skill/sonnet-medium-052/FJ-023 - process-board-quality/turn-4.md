The model passes the check, so this is the gate. It asks about the write only, and nothing is on the board yet.

**What the board must deliver**
* Question: who does what, in which order, and where does a damaged-item claim change hands between the customer, CS and the warehouse?
* Outcome: the product team can see where a claim leaves CS for the warehouse and what each team does at that point

**Glance lines**
* First glance: Approve the claim, the step that sends the claim to the warehouse queue
* Second glance: Damage reported, Check the photo, Damage clear in the photo?, Ask the customer for a second photo, Claims table, Send second photo, Book courier pickup, Inspect on arrival, then Refund released as the goal, in the order the check's Glance line prints
* Last glance: the key and the source line, since the goal comes last

**Sketch, the checked model as the check read it**
```text
%% type: process
flowchart LR
    %% title: Damaged-item refund
    %% subtitle: From a damage report to a released refund, for the product team
    %% source: Source: the Fernhouse support runbook. Left out: the under 20 euro pickup skip, a pilot that is not live.
    %% level: balanced
    %% goal: refund
    %% detail: book | Next working day
    %% detail: inspect | Held against the customer's photo
    %% about: customer | Help form asks: order number, photo, short description
    %% about: cs | Answers within 1 working day | Every decision is logged in the claims table
    %% about: warehouse | Refund within 5 working days of the inspection
    subgraph customer ["Customer"]
        report([Damage reported])
        second[Send second photo]
    end
    subgraph cs ["CS agent"]
        check[Check the photo]
        clear{Damage clear in the photo?}
        ask[Ask the customer for a second photo]
        approve[Approve the claim]
        log[(Claims table)]
    end
    subgraph warehouse ["Warehouse operator"]
        book[Book courier pickup]
        inspect[Inspect on arrival]
        refund([Refund released])
    end
    report --> check
    check --> clear
    clear -->|Clear| approve
    clear -->|Unclear| ask
    clear -->|"Decision logged"| log
    ask --> second
    second --> check
    approve -->|"Claim queued"| book
    book --> inspect
    inspect --> refund
    style customer fill:#F5F5F5,stroke:#B3B3B3
    style cs fill:#F5F5F5,stroke:#B3B3B3
    style warehouse fill:#F5F5F5,stroke:#B3B3B3
    style approve fill:#C2E5FF,stroke:#3DADFF
    %% focus: approve because claim leaves CS for warehouse
```
Check output:
```text
  diagram 1, process: ok, 10 nodes and 10 connectors, widest rank 3 steps, longest path 7 steps, 1.0 connectors per step, labels average 19 characters, 0 crossing pairs
Glance: Approve the claim (accent) > Damage reported > Check the photo > Damage clear in the photo? > Ask the customer for a second photo > Claims table > Send second photo > Book courier pickup > Inspect on arrival > Refund released (goal)
PASSED 1 diagram(s) in model.md
```

**Two changes from the playback**
* Three labels are reworded because the first wording left a single word alone on a line: Damage reported, Damage clear in the photo? and Ask the customer for a second photo
* The warehouse lane note no longer repeats the next working day pickup, which now sits only on Book courier pickup

**Critique of the sketch**
* Eye first: Approve the claim, the one accented step, and it is the node the board most needs read
* Reads second: Damage reported, then Check the photo and Damage clear in the photo?, then the claim on to Refund released, lane by lane. That shows who holds the claim at each step
* Could miss: the Send second photo loop. A reader who skips it assumes every claim passes the check once. That step is my reading of the runbook and not a line in it
* Remove next: the Claims table. Only one connector touches it, but the runbook logs every decision there, and the CS lane note says so

**The write**
* File: the existing FigJam file `<test-file-key>`. I read it once and its page is empty. No section shares the title, so the board keeps the title "Damaged-item refund"
* Writes: one composed section with 3 lanes, 10 nodes and 10 connectors, a title, a key and a source line, at the Laptop reading distance
* Left out: the under 20 euro pickup skip, a pilot that is not live. A photo that shows no damage, a second photo that is still unclear, an inspection that does not match the customer's photo and whether the refund waits on the inspection result, all points the runbook leaves open
* Extensions: none
* Calls: one `use_figma` to compose and one `get_figjam` to read back, on top of the session and the one read already made. On a Starter plan or a View or Collab seat, reads count against the six tool calls a month
* Rollback: delete the one section the write returns, through `use_figma`, and only on a yes that names it

Write it?