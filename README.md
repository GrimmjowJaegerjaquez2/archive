# The Archive

**Pair:** *(your two names)* **Repository:** *(link)*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

A record in our archive looks like a dictionary with 5 fields: id, title, year, city, condition

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | str | `MS001` | disallow the manuscript |
| title | str | "Barkum al-Sudan" | disallow the manuscript  |
| city | str | "Djenne"  | disallow the manuscript  |
| year | str | "1645" | disallow the manuscript  |
| condition | str | "good" | disallow the manuscript  |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | 1. is it  a str? 2. Does it start with MS and are it's last 3 elements numbers? | "M123" |
| title | 1. is it a str 2. Is its length > 3? 3. Are its elements all alphabets or spaces or hyphens | "w1" |
| city | 1. is it a str 2. Is it in KNOWN_CITIES?  | "New York" |
| year | 1. is it a str 2. is it in the range of 1100 - 1900?| "2099" |
| condition | 1. is it  a str | "Alright" |

### Who decided the year range?

We decided to keep the original range as we feel like most manuscripts would be in that range, and any others older or younger than that would be outliers.

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:**
We chose to reject it
**Why:**
It may be untrustworthy data.
**What it costs us:**
Because of this we lost some records in the archive

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid | valid  | Yes |
| Abnormal | Of Cource | invalid | invalid  | No |
| Extreme (low) | 1100 | valid | valid | Yes |
| Extreme (high) | 1900 | valid | valid | Yes |
| Boundary (below) | 1099 | invalid | invalid | No |
| Boundary (above) | 2001 | invalid | invalid | No |

### `Id` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| Normal | MS234 | Valid | Valid | -Yes |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(Lebone)*:** One thing my partner did that I will steal: Asking a lot of questions as it helped me understand my code One thing I would do differently next time: Do research on functions and understand them or find alternatives.

***(Sonia)*:** One thing my partner did that I will steal: Lots of logic and trying different approaches. One thing I would do differently next time: More research

---

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ YES ] Both of us can explain every line in this repository.

- [YES ] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**
 We used Github Desktop to explain some of the functions meanings and to learn some other functions, like .isalpha().
---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)