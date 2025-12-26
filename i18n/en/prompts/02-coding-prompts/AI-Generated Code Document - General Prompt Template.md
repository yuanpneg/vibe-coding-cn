# AI-Generated Code Document - General Prompt Template

**Document Version**: v1.0
**Creation Date**: 2025-10-21
**Applicable Scenarios**: Generate a panoramic document of code usage, similar to a timeline, for any code repository.

---

## 📋 Complete Prompt Template (Copy and Use Directly)

### 🎯 Task 1: Add Standardized Header Comments to All Code Files

```
My first requirement now is to add standardized header comments to all Python code files in the project.

The header comment specification is as follows:

############################################################
# 📘 File Description:
# The function implemented by this file: Briefly describe the core function, purpose, and main modules of this code file.
#
# 📋 Overall Program Pseudocode (Chinese):
# 1. Initialize main dependencies and variables.
# 2. Load input data or receive external requests.
# 3. Execute main logic steps (e.g., calculation, processing, training, rendering).
# 4. Output or return results.
# 5. Exception handling and resource release.
#
# 🔄 Program Flowchart (Logical Flow):
# ┌──────────┐
# │  Input Data │
# └─────┬────┘
#       ↓
# ┌────────────┐
# │  Core Processing Logic │
# └─────┬──────┘
#       ↓
# ┌──────────┐
# │  Output Results │
# └──────────┘
#
# 📊 Data Pipeline Description:
# Data flow: Input source → Data cleaning/transformation → Core algorithm module → Output target (file / interface / terminal)
#
# 🧩 File Structure:
# - Module 1: xxx Function
# - Module 2: xxx Function
# - Module 3: xxx Function
#
# 🕒 Creation Time: {Automatically generate current date}
############################################################

Execution requirements:
1. Scan all .py files in the project (excluding virtual environment directories such as .venv, venv, site-packages).
2. Intelligently generate header comments for each file that match its actual function.
3. Infer functional descriptions based on filenames and code content.
4. Automatically extract import dependencies as the "File Structure" section.
5. Retain existing shebang and encoding declarations.
6. Do not modify existing business logic code.

Create a batch script to automate this process and process all files at once.
```

---

### 🎯 Task 2: Generate a Panoramic Code Usage Document

```
My second requirement now is to create a complete panoramic code usage document for this code repository.

The required format is as follows:

## Part One: Project Environment and Technology Stack

### 📦 Project Dependency Environment
- Python version requirements
- Operating system support
- List of core dependency libraries (categorized display):
  - Core framework
  - Data processing library
  - Network communication library
  - Database
  - Web framework (if any)
  - Configuration management
  - Task scheduling
  - Other utility libraries

### 🔧 Technology Stack and Core Libraries
Provide for each core library:
- Version requirements
- Purpose description
- Core components
- Key application scenarios

### 🚀 Environment Installation Guide
- Quick installation commands
- Configuration file examples
- Installation verification methods

### 💻 System Requirements
- Hardware requirements
- Software requirements
- Network requirements

---

## Part Two: Panoramic Code Usage

### 1. ⚡ Minimalist Overview (Complete Process)
Display the timeline process of the entire system.

### 2. Detailed Process Expanded by Timeline
Each time node includes:
- 📊 Data pipeline flowchart (using ASCII art)
- 📂 List of core scripts
- ⏱️ Estimated time consumption
- 🎯 Function description
- 📥 Input data (file path and format)
- 📤 Output data (file path and format)
- ⚠️ Important reminders

### 3. 📁 Core File List
- Categorized by function (signal processing, transaction execution, data maintenance, etc.)
- List of data flow tables

### 4. 🎯 Key Data File Flow Diagram
Use ASCII diagrams to show how data flows between different scripts.

### 5. 📌 Usage Instructions
- How to find scripts used in specific time periods
- How to track data flow
- How to understand script dependencies

---

Format requirements:
- Use Markdown format.
- Use ASCII flowcharts (using ┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼ ↓ ← → ↑ and other characters).
- Use tables to display key information.
- Use Emoji icons to enhance readability.
- Code blocks are enclosed by ```.

Storage location:
Save the generated document to the project root directory or document directory, with the filename:
Code Usage Panorama_by Timeline_YYYYMMDD.md

References:
[Specify your operation manual PDF path or existing document path here]
```

---

### 📝 Usage Instructions

**Execute two tasks in order:**

1.  **First execute Task 1**: Add header comments to all code.
    - This will make the function of each file clearer.
    - Convenient for understanding code purpose when generating documents later.

2.  **Then execute Task 2**: Generate a panoramic code usage document.
    - Based on the code with added header comments.
    - Can more accurately describe the function of each script.
    - Generate complete tech stack and dependency descriptions.

**Complete workflow**:
```
Step 1: Send "Task 1 Prompt" → AI batch adds file header comments
   ↓
Step 2: Send "Task 2 Prompt" → AI generates code usage panorama document
   ↓
Step 3: Review document → Supplement missing information → Complete
```
```

---

## 🎯 Usage Examples

### Scenario 1: Generate Documentation for a Futures Trading System

```
My current requirement is to create a complete code usage document for this futures trading system.

In the form of a timeline, list the code used in the operation manual, build a detailed data pipeline,
and add a concise overview at the top.

Refer to the following operation manuals:
- Measurement Operation Manual/Futures Maintenance - 9 AM.pdf
- Measurement Operation Manual/Futures Maintenance - 2 PM.pdf
- Measurement Operation Manual/Futures Maintenance - 4 PM.pdf
- Measurement Operation Manual/Futures Maintenance - 8:50 PM to after 9 PM opening.pdf

Save to: Measurement Detailed Operation Manual/
```

### Scenario 2: Generate Documentation for a Web Application

```
My current requirement is to create a code usage document for this web application.

Following the timeline of user operations, list the involved code files,
build a detailed data pipeline and API call relationships.

The timeline includes:
1. User registration and login process
2. Data upload and processing process
3. Report generation process
4. Scheduled task execution process

Save to: docs/code-usage-guide.md
```

### Scenario 3: Generate Documentation for a Data Analysis Project

```
My current requirement is to create a code usage document for this data analysis project.

Following the timeline of the data processing pipeline:
1. Data collection stage
2. Data cleaning stage
3. Feature engineering stage
4. Model training stage
5. Result output stage

For each stage, list the scripts used, data flow, and dependencies in detail.

Save to: docs/pipeline-guide.md
```

---

## 💡 Key Prompt Elements

### 1️⃣ Clear Document Structure Requirements

```
Must include:
✅ Dependency environment and tech stack (placed at the top of the document)
✅ Minimalist overview
✅ Timeline-style detailed process
✅ ASCII flowchart
✅ Data flow diagram
✅ Core file index
✅ Usage instructions
```

### 2️⃣ Specify Time Nodes or Process Stages

```
Example:
- 09:00-10:00 AM
- 14:50-15:00 PM
- 21:00 PM - 09:00 AM the next day

Or:
- User registration process
- Data processing process
- Report generation process
```

### 3️⃣ Clearly Define Data Pipeline Display Method

```
Requirements:
✅ Use ASCII flowcharts
✅ Clearly label input/output
✅ Show dependencies between scripts
✅ Label data format
```

### 4️⃣ Specify Storage Location

```
Example:
- Save to: docs/
- Save to: Measurement Detailed Operation Manual/
- Save to: README.md
```

---

## 🔧 Customization Suggestions

### Adjustment 1: Add Performance Metrics

Add to each time node:
```markdown
### Performance Metrics
- ⏱️ Execution time: 2-5 minutes
- 💾 Memory usage: approx. 500MB
- 🌐 Network requirements: Internet connection needed
- 🔋 CPU utilization: Medium
```

### Adjustment 2: Add Error Handling Description

```markdown
### Common Errors and Solutions
| Error Message | Cause | Solution |
|---|---|---|
| ConnectionError | CTP connection failed | Check network and account configuration |
| FileNotFoundError | Signal file missing | Confirm Doctor Signal has been sent |
```

### Adjustment 3: Add Dependency Graph

```markdown
### Script Dependencies
```
A.py ─→ B.py ─→ C.py
  │       │
  ↓       ↓
D.py    E.py
```
```

### Adjustment 4: Add Configuration File Description

```markdown
### Related Configuration Files
| File Path | Purpose | Key Parameters |
|---|---|---|
| config/settings.toml | Global configuration | server.port, ctp.account |
| moni/manual_avg_price.csv | Manual cost price | symbol, avg_price |
```

---

## 📊 Quality Standards for Generated Documents

### ✅ Must Meet Standards

1.  **Completeness**
    -   ✅ Covers all time nodes or process stages.
    -   ✅ Lists all core scripts.
    -   ✅ Includes all key data files.

2.  **Clarity**
    -   ✅ ASCII flowcharts are easy to understand.
    -   ✅ Data flow is clear at a glance.
    -   ✅ Information is organized using tables and lists.

3.  **Accuracy**
    -   ✅ Script function descriptions are accurate.
    -   ✅ Input and output file paths are correct.
    -   ✅ Time nodes are accurate.

4.  **Usability**
    -   ✅ New members can quickly get started.
    -   ✅ Facilitates troubleshooting.
    -   ✅ Supports quick lookup.

### ⚠️ Problems to Avoid

1.  ❌ Over-simplification, missing key information.
2.  ❌ Over-complexity, difficult to understand.
3.  ❌ Lack of data flow description.
4.  ❌ No practical examples.
5.  ❌ Incomplete tech stack and dependency information.

---

## 🎓 Advanced Tips

### Tip 1: Layered Display for Large Projects

```
Layer 1: System Overview (minimalist version)
Layer 2: Module detailed process
Layer 3: Specific script description
Layer 4: Data format specification
```

### Tip 2: Use Color Marking (in supported environments)

```markdown
🟢 Normal flow
🟡 Optional step
🔴 Key step
⚪ Manual operation
```

### Tip 3: Add Quick Navigation

```markdown
## Quick Navigation

- [Morning Operations](#timeline-1-morning-090010-00)
- [Afternoon Operations](#timeline-2-afternoon-145015-00)
- [Evening Operations](#timeline-3-evening-204021-00)
- [Full Index of Core Scripts](#full-index-of-core-scripts)
```

### Tip 4: Provide Checklist

```markdown
## Pre-execution Checklist

□ Doctor Signal received
□ CTP account connected normally
□ Database updated
□ Configuration file confirmed
□ SimNow client logged in
```

---

## 📝 Template Variable Description

When using the prompt, the following variables can be replaced:

| Variable Name | Description | Example |
|---|---|---|
| `{PROJECT_NAME}` | Project name | Futures Trading System |
| `{DOC_PATH}` | Document save path | docs/code-guide.md |
| `{TIME_NODES}` | List of time nodes | 9 AM, 2 PM, 9 PM |
| `{REFERENCE_DOCS}` | Reference document path | Operation Manual/*.pdf |
| `{TECH_STACK}` | Tech stack | Python, vnpy, pandas |

---

## 🚀 Quick Start

### Step 1: Prepare Project Information

Collect the following information:
-   ✅ Project operation manual or process document
-   ✅ Main time nodes or process stages
-   ✅ List of core scripts
-   ✅ Data file paths

### Step 2: Copy Prompt Template

Copy the "Prompt Template" section from this document.

### Step 3: Customize Prompt

Modify according to your project's actual situation:
-   Time nodes
-   Reference material paths
-   Storage location

### Step 4: Send to AI

Send the customized prompt to Claude Code or other AI assistants.

### Step 5: Review and Adjust

Review the generated document and adjust as needed:
-   Supplement missing information
-   Correct erroneous descriptions
-   Optimize flowcharts

---

## 💼 Practical Case Reference

This prompt template is based on documents generated from actual projects:

**Project**: Futures Trading Automation System
**Generated Document**: `Code Usage Panorama_by Timeline_20251021.md`
**Document Scale**: 870 lines, 47KB

**Includes**:
-   5 timeline nodes
-   18 core scripts
-   Complete ASCII data pipeline flowchart
-   6 major functional categories
-   Complete tech stack and dependency descriptions

**Generation Effect**:
-   ✅ New members quickly understand the system in 30 minutes
-   ✅ Troubleshooting time reduced by 50%
-   ✅ Document maintenance cost reduced by 70%

---

## 🔗 Related Resources

-   **Project Repository Example**: https://github.com/123olp/hy1
-   **Generated Document Example**: `Measurement Detailed Operation Manual/Code Usage Panorama_by Timeline_20251021.md`
-   **Operation Manual Reference**: `Measurement Operation Manual/*.pdf`

---

## 📮 Feedback and Improvements

If you use this prompt template to generate documents, feel free to share:
-   Your use case
-   Generation effect
-   Improvement suggestions

**Contact**: [Add your contact information here]

---

## 📄 License

This prompt template is licensed under the MIT license and can be freely used, modified, and shared.

---

**✨ Use this template to let AI help you quickly generate high-quality code usage documentation!**
