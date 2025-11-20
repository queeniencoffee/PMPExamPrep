# The Agile Manifesto and Mindset

## 📑 Table of Content

### Key Concepts 
1. The Four Agile Values & Manifesto
2. The Agile 12 Clarifying Principles
3. Life Cycle Selection
      3a. Predictive / Waterfall
      3b. Iterative
      3c. Incremental
      3d. Agile

### Deep Dive
1. Whole team approach
2. Early and Frequent Feedback
3. Daily stand-ups
4. Retrospectives
5. Release and Iteration Planning
6. Collaborative User Story Creation
7. Demonstrations / Reviews
8. Continuous Integraiton
9. Sevant Leadership

### Other topics covereed in PMP Exam:  
10. Life Cycle Selection
11. 

------------------------------------------------------------------------------------------------

## The Four Agile Values & Manifesto

| # |   The Agile Four Values        | over |    Waterfall                 |
|----|-------------------------------| ---- |---------------------------- |
| 1 | Individuals and interactions   | over | Processes and Tools         |
| 2 | Working Software               | over | Comprehensive documentation |
| 3 | Customer collaboration         | over | Contract Negotiation        |
| 4 | Responding to change           | over | Following a Plan            |

The Agile Manifesto argues that although the concepts on the right have value, those on the left have greater value.

## The Agile 12 Clarifying Principles
1. Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.
   2-4 weeks, incremental delivery, put feedback back to the products
2. Welcome changing requirements, even late in development. Agile processes harness change for the customer’s competitive advantage.
   Get regular feedback through iteration, then make changes to the products if necessary intead of one change toward the end.
3. Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.
4. Business people and developers must work together daily throughout the project.
5. Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done.
6. The most efficient and effective method of conveying information to and within a development team is face-to-face conversation.
7. Working software is the primary measure of progress.
8. Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.
9. Continuous attention to technical excellence and good design enhances agility.
10. Simplicity–the art of maximizing the amount of work not done–is essential.
11. The best architectures, requirements, and designs emerge from self-organizing teams.
12. At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.

#### Ref: https://www.youtube.com/watch?v=hnxhqoenoXg&list=PLEWFSKHjyrwy1bYSi1WsoPGDno-LKOnhV&index=4

------------------------------------------------------------------------------------------------

# Life Cycle Selection
Projects come in all shapes and sizes, and there are a variety of ways to manage them. 
- Different organizational structures
- different lifecycles
- different management style
- different sizes
- different customer needs
- different products and outputs

Different types of projects drives different managing methods: 
- Have co-located teams or dispersed teams
- governed by a supportive, controlling or directive PMO, or functional manager
- Sponsor or customer may want daily reports, or weekly reports.
- Have more than one customer group receiving the benefit of the project
- Project may be technically simple or complex
- may have easily definable work, or high uncertainty work. 

# Life Cycle Comparison

| # |   Approach  | Requirements | Activities                               | Delivery                    | Goal                    | 
|---|-------------| ------------ | ---------------------------------------- | --------------------------- | ----------------------- |
| 1 | Predictive  | Fixed        | Performed once for the entire project    | Single Delivery             | Manage Cost             |
| 2 | Iterative   | Dynamics     | Repeated until correct (unfinished work) | Single Delivery          | Correctness of solution |
| 3 | Incremental | Dynamics     | Performed once for a given increment (finished work) | Frequent smaller deliveries | Speed                   |
| 4 | Agile       | Dynamics     | Repeated until correct                   | Frequent smaller deliveries | Customer value via frequent deliveries and feedback | 

## "Predictive" / Waterfall Approach
- The traditional "waterfall" approach, with the bulk of planning done up front, then executing in a single, sequential process. Release products every 2-4 weeks.
#### Predictive Lifecycle Characteristics:
- Take advantage of <ins>high certainty</ins> around requirements, a <ins>stable team</ins>, and <ins>low risk</ins>.
- Project activities often execute in a straight forward, serial manner.
- As the team progresses through the detailed plan, they monitor and control changes that might affect the Scope, Schedule, or Budget (cost).
- Project typically do not dliver business value until the end of project.  
```mermaid
graph LR
    A[Analyze] --> D[Design] --> B[Build] --> T[Test] --> L[Deliver]
```

## "Iterative" Life Cycle
- An approach that allows feedback for "unfinished" work to improve and modify that work.
#### Characteristics: 
- Iterative life cycles improve the product or result through successive prototpyes or proof of concepts.  Each new prototype yields new stakeholder feedback and team insights.
- Team may use time-boxing on a given iteration of two or four weeks to build, gather feedback, then put that feedback into the next iteration.
- Useful when complexity is high, or scope is subject to change.
- Iterative life cycles take longer aas they are optimized for learning, rather than speed of delivery.
```mermaid
graph LR
    A[Analyze] --> D[Analyze, Design] --> B[Build, Test] --> TL[Deliver]
    D -->|Prototype| D
    B -->|Refine| B
```

## "Incremental" Life Cycle
- An approach that provides "finished" deliverables that the customer may be able to use immediately. Release products regularly.
#### Characteristics: 
- When businesses or initiatives cannot afford to wait for everything to be completed.
- In this situation the customer, business, or sponsor are willing to receive a subset of the overall solution delivered in frequent small releases.
- You could provide a single feature at a time.
- Increments are time-boxed in iterative methods, or pulled in flow based methods like Kanban. 
```mermaid
graph LR
    A[Analyze, Design, Build, Test, Deliver] --> D[Analyze, Design, Build, Test, Deliver] --> B[Analyze, Design, Build, Test, Deliver] 
```

## "Agile" Life Cycle
- An approach that is both iterative and incremental, to refine work items and deliver frequently.
#### Characteristics: 
- In an Agile environment, the team expects requirements to change
- Iterative and Incremental approaches work together - to provide feedback for planning the next iteration, and uncovering hidden or misunderstood requiremetns (using increments)
- For Kanban, or Flow based Agile, it is iterated for the number of features in the Work in Progress (WIP) limit (on the board). The team pulls features from the backlog column on the Kanban board based on their capacity.
```mermaid
graph LR
    A[Requirements, Analyze, Design, Build, Test] --> D[Requirements, Analyze, Design, Build, Test] --> B[Requirements, Analyze, Design, Build, Test] 
```

## Hybrid Approach
- Projects often combine elements of different life cycles in order to achive their goals.
- A combination of predictive, iterative, incremetnal and agile approaches is hybrid approach.
#### Characteristics: 
- You might have:
      - Largely agile, with some predictive
            - Where you are integrating an external component developed by a different vendor
            - A single iteration might be required after their component is delivered.
      - Predominantly predictive, with some agile components
            - Where you are delivering a straight forward project (a shed or patio), but trialling a new roofing material.
      - A combined predictive and agile approach
            -  A serial or linear project, where tasks are tracked using Kanban and daily scrums are used for updating work. 

------------------------------------------------------------------------------------------------

## Definable Work v.s. High Uncertainty Work
Project work ranges from definable work to high-uncertainty work. 

Definable: Clear procedure, similar to past projects
e.g. Production of a car, appliance or home after the design is complete

High-Uncertainty: High rate of change, complexity and risk
e.g. System or problem solving engineers, product designers, doctors, lawyers etc.

![Agile Project Complexity](https://github.com/queeniencoffee/PMPExamPrep/raw/e9d2950de9ba83a10a8bfebb294fe0562c3467e8/Study-Notes/img/Agile%20Project%20Complexity.png)

## Project Life Cycle Selection

No Life cycle can be perfect for all projects.  Instead, each project finds a place on the continuum that provides an optimum balance. 

![Delivery vs Management Method](https://github.com/queeniencoffee/PMPExamPrep/raw/6fe16fe5b6686c6179e4e868fcfa42ef6546b72a/Study-Notes/img/Delivery%20vs%20Mgmt%20Method.png)

------------------------------------------------------------------------------------------------

### Where does Agile fit in Product and Project Management? 

#### Use "Waterfall" when: 
1. Definable: Clear Procedures, similar to past projects
   i.e. Production of a car, appliance or home after the design is completed
2. High-Uncertainty:  High rates of changes, complexity and risk
   i.e. System or problem solving engineers, product designers, doctors, lawyers

------------------------------------------------------------------------------------------------


## Whole Team approach
- The whoel team approach meaning involving everyone with the knowledge and skills necessary to ensure project success.
- The team should be "relative small" (successful teams have been observed with as few as three people and as many as nine).
- Ideally, the whole team shared the same workspace / co-located
- Team are often 100% dedlicated to the delivery because when switching or multitasking people make more mistakes adn experience between 20$ - 40% loss of productivity.

### Team Member
1. Cross Functional Team member: consists of team members with all the skills necessary to produce a working product.
2. In SW development, cross functional teams are comprised of designers, developers, testers, and any other required roles.
3. These teams deliver small, releasable products on a regular basis.
4. Thy are critical because they can deliver finished work in shortest possible time, with higher quality, without external dependencies.

### Product Owner
1. The Product Owner respresents the customer
2. Prodcut Owner ≠ Team Lead
3. Respnsible to generates, maintains, and prioritize the product backlog to ensure the highest business value without creating waste.
4. may work with stakeholder, customer and team to define product direction, and rank the work based on its business value. Typically, product owners have a business backgorund and bring deep subject mater expertise to the decisions. 

### Team Facilitator
1. The team facilitator, or servant leader, can be called a project manager, scrum master, project team lead, team coach, or team facilitator.
2. The whole team approach is supported through the daily stand-up meetings, facilitated by this servant leader role.
3. All agile teams need servant leadership on the team, and team members need to build their own servant leadership skills of facilitation, coaching, and removing blockers.

Ref: https://youtu.be/7mMQtDbfzCw?si=TrxXgXWKeZon3DEb

------------------------------------------------------------------------------------------------

## Agile Core Practice - Servant Leadership

- Agile is a Servant Leaders.  Customer are the team member, and you are the lead. You are here to help them to succeed. 
- Servant leaders approach project work in this order:
   - Purpose: Work with the team to define the "why"
   - People: Creating an environment where everyone can succeed
   - Process:  Look at the results over the process - if a team delivers value often and reflects on the product and the process, it is agile.

------------------------------------------------------------------------------------------------

## Early and Frequent Feedback
- Agile projects have short iterations enabling the project team to receive early and continuous feedback on product quality throughout the development lifecycle.
- By getting frequency customer feedback as teh project progresses, Agile teams can incorporate most new changes into the product, and the development process.

## The benefit of early and frequency feedback include: 
- Avoid requirements misundersatndings, which may not have been detected until alter in the development cycle when they are more expensive to fix.
- Clarifying customer feature requests, makign them availble for customer use early.  This way, the product better reflects what the customer wants.
- Discovering (via continuous integraiton), isolating, and resolving quality problems early.  Providing information to the Agile team regarding its productivity and ability to deliver.
- Promoting consistent project momentum.

#### Ref: https://youtu.be/qRCs-Th_pWs?si=im32t3ql6LIxk_lr

------------------------------------------------------------------------------------------------











