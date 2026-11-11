# Product Owner - Examples - Task - Standard Feature

Instantiates Task Templates section 3, Parent Task. Shows shared feature scope stated once while independent child tasks carry their own detail.

---

# Vantage Analytics - Filter Presets v1 - Traffic Overview

## About

---

Vantage Analytics users rebuild the same filter combinations every time they open the Traffic Overview dashboard. This parent task coordinates the child work needed to save the current `Date range`, `Compare with`, `Channel`, `Country`, `Device` and `Campaign` values as one preset, manage saved presets and open the report with one personal default.

The first version covers presets owned by one user on the Traffic Overview report. Preset sharing, cross-report copying, organization-managed presets and new filter types are out of scope. The child tasks below own their behavior and acceptance checks. This parent holds only the shared feature boundary and delivery order.

**References**

---

Flows

- [Save and apply filter preset](figma-url)

Page

- [Traffic Overview dashboard](figma-url)

Components

- [Filter preset dropdown](figma-url)

**Epic**

---

- `Epic - Vantage Analytics - Dashboard Personalization`

### Requirements

---

1\. **Save and name the current filter combination**

---

[FE - Vantage Analytics - Filter Presets v1 - Save Preset](https://app.vantage.example/t/VA-241)

2\. **Rename and delete saved presets**

---

[FE - Vantage Analytics - Filter Presets v1 - Manage Presets](https://app.vantage.example/t/VA-242)

3\. **Apply a preset and restore all six filter values**

---

[FE - Vantage Analytics - Filter Presets v1 - Apply Preset](https://app.vantage.example/t/VA-243)

4\. **Set one personal default and handle no-presets fallback**

---

[FE - Vantage Analytics - Filter Presets v1 - Default Preset & Empty State](https://app.vantage.example/t/VA-244)
