# Product Owner - Assets - Flow Templates - Process

Copy/apply patterns for a process model. Each pattern passes the rules, and Templates - Flow Type - Process holds the rules.

---

## 1. USAGE

- Keep the `%% type: process` line first, or the block reads as a user flow
- Name a lane after the actor, `subgraph agent ["CS agent"]`, and keep its id short and camelCase
- A lane takes the neutral pair or no style, and the one accent goes on the focal step, such as the step that hands work to the next lane. The composer draws that step in focus. A `linkStyle` changes nothing on a composed board
- `-.->` marks a step that is optional or proposed. A log write that runs today is drawn solid
- The patterns all run left to right, because every process in one file reads as one flow that runs one way

---

## 2. PATTERNS

### Decision tree

```mermaid
%% type: process
flowchart LR
    %% goal: done
    start([Request in]) --> size{Over the limit?}
    size -->|No| auto[Approve automatically]
    size -->|Yes| risk{Known customer?}
    risk -->|Yes| review[Manager reviews]
    risk -->|No| reject([Declined])
    auto --> done([Approved])
    review --> done
    style size fill:#FFC2EC,stroke:#F849C1
```

### Laned process with a handoff in focus

The step that hands work to operations is in focus, because that handoff adds the most delay.

```mermaid
%% type: process
flowchart LR
    subgraph requester ["Requester"]
        ask([Request sent])
    end
    subgraph team ["Support team"]
        triage{Complete?}
        more[Ask for details]
        approve[Approve]
    end
    subgraph ops ["Operations"]
        fulfil[Fulfil the request]
        closed([Request closed])
    end
    ask --> triage
    triage -->|No| more
    more --> triage
    triage -->|Yes| approve
    approve --> fulfil
    fulfil --> closed
    style requester fill:#F5F5F5,stroke:#B3B3B3
    style team fill:#F5F5F5,stroke:#B3B3B3
    style ops fill:#F5F5F5,stroke:#B3B3B3
    style approve fill:#C2E5FF,stroke:#3DADFF
```

### Pipeline with a store and data in and out

```mermaid
%% type: process
flowchart LR
    %% goal: done
    upload[/Upload a file/] --> parse[Parse rows]
    parse --> valid{Rows valid?}
    valid -->|Yes| save[Save the import]
    valid -->|No| errors[/Error report/]
    save --> store[(Imports)]
    save -->|"Later"| notify[[Notify the owner]]
    notify --> done([Import finished])
    style valid fill:#FFC2EC,stroke:#F849C1
```
