# 🧠 PMP Formula Sheet (Brain Dump)

Creating and practicing your own **brain dump** is a key strategy for success on the PMP exam.

Below is a comprehensive **PMP Formula Sheet and quick reference guide**.  
Focus heavily on **Earned Value Management (EVM)**, as it has the most calculations and concepts.

---

## 1a. Earned Value Management (EVM)

This section measures project performance and forecasts future performance.

| Abbreviation | Definition            | Formula                                                   | Interpretation |
| :----------- | :-------------------- | :-------------------------------------------------------- | :------------- |
| **PV**       | Planned Value         | $\text{PV} = \text{BAC} \times \text{Planned \% Complete}$ | Budgeted cost for work *scheduled* |
| **EV**       | Earned Value          | $\text{EV} = \text{BAC} \times \text{Actual \% Complete}$  | Budgeted cost for work *performed* |
| **AC**       | Actual Cost           | Actual money spent to date                                | Actual cost for work *performed* |
| **BAC**      | Budget at Completion  | Total project budget                                      | N/A |
| **CV**       | Cost Variance         | $\text{CV} = \text{EV} - \text{AC}$                      | $\text{CV} > 0$: Under Budget, $\text{CV} < 0$: Over Budget |
| **SV**       | Schedule Variance     | $\text{SV} = \text{EV} - \text{PV}$                      | $\text{SV} > 0$: Ahead of Schedule, $\text{SV} < 0$: Behind Schedule |
| **CPI**      | Cost Performance Index | $\text{CPI} = \text{EV} / \text{AC}$                    | $\text{CPI} > 1$: Efficient, $\text{CPI} < 1$: Inefficient (Cost Overrun) |
| **SPI**      | Schedule Performance Index | $\text{SPI} = \text{EV} / \text{PV}$                  | $\text{SPI} > 1$: Efficient, $\text{SPI} < 1$: Inefficient (Behind Schedule) |
| **EAC**      | Estimate at Completion | *(4 formulas based on assumptions)*                      | Forecasted final cost of the project |
| **ETC**      | Estimate to Complete  | $\text{ETC} = \text{EAC} - \text{AC}$                    | Cost needed to complete the remaining work |
| **VAC**      | Variance at Completion| $\text{VAC} = \text{BAC} - \text{EAC}$                  | Forecasted final budget variance |
| **TCPI**     | To Complete Performance Index | *(2 formulas based on goal)*                         | Efficiency needed to meet a target |

### 1b. Earned Value Management (EVM) (printable version)

| Formula | Description |
| :--- | :--- |
| **Cost Variance (CV)** | CV = EV - AC |
| **Schedule Variance (SV)** | SV = EV - PV |
| **Cost Performance Index (CPI)** | CPI = EV / AC |
| **Schedule Performance Index (SPI)** | SPI = EV / PV |
| **Budget at Completion (BAC)** | BAC = Total project budget |
| **Estimate at Completion (EAC)** (Typical Variances) | EAC = BAC / CPI |
| **Estimate at Completion (EAC)** (Atypical Variances) | EAC = AC + (BAC - EV) |
| **Estimate at Completion (EAC)** (Considering both CPI & SPI) | EAC = AC + ((BAC - EV) / (CPI * SPI)) |
| **Estimate to Complete (ETC)** | ETC = EAC - AC |
| **Variance at Completion (VAC)** | VAC = BAC - EAC |
| **To Complete Performance Index (TCPI)** (To hit BAC) | TCPI = (BAC - EV) / (BAC - AC) |
| **To Complete Performance Index (TCPI)** (To hit EAC) | TCPI = (BAC - EV) / (EAC - AC) |
| **Planned Value (PV)** | PV = BAC * Planned % Complete |
| **Earned Value (EV)** | EV = BAC * Actual % Complete |

* **Rule of Thumb:** For CV and SV, a positive number is good. For CPI and SPI, a number **greater than 1** is good.

### EAC Formulas (Estimate at Completion)

1. **If current variances are *atypical* (not expected to repeat):**

   $$\text{EAC} = \text{AC} + (\text{BAC} - \text{EV})$$  

   *Remaining work will be performed at the budgeted rate (CPI = 1).*

2. **If current variances are *typical* (expected to repeat):**

   $$\text{EAC} = \text{BAC} / \text{CPI}$$  

   *Remaining work will be performed at the current CPI rate.*

3. **If current variances are *typical* (considering both cost and schedule):**

   $$\text{EAC} = \text{AC} + \left(\frac{\text{BAC} - \text{EV}}{\text{CPI} \times \text{SPI}}\right)$$

### TCPI Formulas (To Complete Performance Index)

1. **To meet the original budget (BAC):**

   $$\text{TCPI}_{\text{BAC}} = \frac{\text{BAC} - \text{EV}}{\text{BAC} - \text{AC}}$$

2. **To meet the new forecast (EAC):**

   $$\text{TCPI}_{\text{EAC}} = \frac{\text{BAC} - \text{EV}}{\text{EAC} - \text{AC}}$$  

   *If $\text{TCPI} > 1.0$, the remaining work is harder/must be more efficient.  
   If $\text{TCPI} < 1.0$, the remaining work is easier/can be less efficient.*

---

## 2. Time Management / Scheduling

### Critical Path Method (CPM) – Node Logic

| Calculation | Forward Pass                               | Backward Pass                                | Float |
| :---------- | :------------------------------------------ | :------------------------------------------- | :---- |
| **EF** (Early Finish) | $\text{EF} = \text{ES} + \text{Duration}$ | N/A                                          | **Total Float (TF)** = $\text{LS} - \text{ES}$ or $\text{LF} - \text{EF}$ |
| **ES** (Early Start)  | $\text{ES} = \text{Max}(\text{EF}_\text{Predecessors})$ | **LS** (Late Start) = $\text{LF} - \text{Duration}$ | **Free Float (FF)** = $\text{ES}_\text{Successor} - \text{EF}_\text{Activity}$ |
| **LF** (Late Finish)  | N/A                                         | $\text{LF} = \text{Min}(\text{LS}_\text{Successors})$ | |

**Key Concept:**  
The **Critical Path** is the **longest path** through the network diagram and has a **Total Float of Zero (TF = 0)**.

### Three-Point Estimating

| Method                               | Formula (Expected Activity Duration)              | Formula (Standard Deviation / Range)                          |
| :----------------------------------- | :----------------------------------------------- | :------------------------------------------------------------ |
| **Triangular Distribution (Simple Average)** | $E = (\text{O} + \text{M} + \text{P}) / 3$      | N/A |
| **PERT (Beta Distribution)**        | $E = (\text{O} + 4\text{M} + \text{P}) / 6$      | $\text{Standard Deviation}(\sigma) = (\text{P} - \text{O}) / 6$ |

*Where: **O** = Optimistic, **M** = Most Likely, **P** = Pessimistic*

### 2b. Time Management and Scheduling (printable version)

| Formula | Description |
| :--- | :--- |
| **Early Finish (EF)** | EF = ES + Duration |
| **Late Start (LS)** | LS = LF - Duration |
| **Total Float (TF)** | TF = LS - ES or TF = LF - EF |
| **Critical Path** | The longest path, with Total Float = 0. |
| **Free Float** | FF = ES of Successor - EF of Activity |
| **PERT (Beta) Expected Duration** | $E = (O + 4M + P) / 6$ |
| **PERT Standard Deviation $(\sigma)$** | $\sigma = (P - O) / 6$ |
| **Triangular Expected Duration** | $E = (O + M + P) / 3$ |

* **Key:** O = Optimistic, M = Most Likely, P = Pessimistic


---

## 3a. Risk Management

| Term | Formula | Use |
| :--- | :------ | :--- |
| **Expected Monetary Value (EMV)** | $\text{EMV} = \text{Probability} \times \text{Impact (Cost)}$ | Calculates the average outcome when dealing with uncertainty (e.g., decision tree analysis). Add EMV for opportunities (positive value) and subtract EMV for threats (negative value). |
| **Risk Priority Number (RPN)** | $\text{RPN} = \text{Severity} \times \text{Occurrence} \times \text{Detection}$ | Used in **FMEA (Failure Mode and Effects Analysis)** to prioritize risks in a qualitative assessment. |

### 3b. Risk and Financial Analysis (printable version)

| Formula | Description |
| :--- | :--- |
| **Expected Monetary Value (EMV)** | EMV = Probability * Impact (Cost/Value) |
| **Number of Communication Channels** | $C = n(n - 1) / 2$ |
| **Benefit-Cost Ratio (BCR)** | BCR = Present Value of Benefits / Present Value of Costs |
| **Point of Total Assumption (PTA)** (FPIF Contracts) | $\text{PTA} = \left(\frac{\text{Ceiling Price} - \text{Target Price}}{\text{Buyer's Share Ratio}}\right) + \text{Target Cost}$ |

* **Decision Rules:**
    * **NPV:** Choose the **Highest Positive NPV**.
    * **IRR:** Choose the **Highest IRR** (if IRR > Hurdle Rate).
    * **Payback Period:** Choose the **Shortest Payback Period**.
    * **BCR:** Choose the project with $\text{BCR} > 1$.

---

## 4. Communication

| Term | Formula | Use |
| :--- | :------ | :--- |
| **Number of Communication Channels** | $C = n(n-1) / 2$ | Calculates the total number of communication channels possible between `n` stakeholders (or team members). |

---

## 5. Procurement and Contract Types

| Term | Formula | Use |
| :--- | :------ | :--- |
| **Point of Total Assumption (PTA)** (for FPIF contracts) | $\text{PTA} = \left(\frac{\text{Ceiling Price} - \text{Target Price}}{\text{Buyer’s Share Ratio}}\right) + \text{Target Cost}$ | Cost point at which the seller assumes all further cost overruns (the seller will not make additional profit above this point). |
| **Target Price (TP)** | $\text{TP} = \text{Target Cost} + \text{Target Fee}$ | Initial expected final price of a contract. |
| **Final Price (FP)** | $\text{FP} = \text{Actual Cost} + \text{Fee}$ (Fee is calculated using the share ratio up to PTA) | Final amount paid to the seller. |

---

## 6. Financial Analysis (Project Selection)

| Term | Concept | Decision Rule (Best Choice) |
| :--- | :------ | :-------------------------- |
| **Net Present Value (NPV)** | Total present value of all future cash flows (inflows – outflows). | Choose the project with the **highest positive NPV**. |
| **Internal Rate of Return (IRR)** | Discount rate at which the NPV of the project becomes zero. | Choose the project with the **highest IRR** (provided IRR > hurdle rate). |
| **Payback Period** | Time required to recover the cost of an investment. | Choose the project with the **shortest payback period**. |
| **Benefit–Cost Ratio (BCR)** | $\text{BCR} = \text{Present Value of Benefits} / \text{Present Value of Costs}$ | Choose the project with the **highest BCR** (and $\text{BCR} > 1$). |

---

**Tip:**  
👉 Practice writing this entire sheet out repeatedly until **December 14th**.  
The repetition will help you memorize not just the **formulas**, but also their **context and application**, which is crucial for the PMP exam.

