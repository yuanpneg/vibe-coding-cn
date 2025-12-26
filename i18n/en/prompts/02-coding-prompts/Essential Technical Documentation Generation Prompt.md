# Essential Technical Documentation Generation Prompt

## Essential General Version

```
Based on the current project files, help me generate technical documentation:

【Project Information】
Name: {Project Name}
Problem: {Core Problem}
Technology: {Tech Stack}

【Document Structure - 4 Parts】

1️⃣ Problem and Solution (300 words)
   - What is the problem
   - Why it needs to be solved
   - How to solve it
   - Why this solution was chosen

2️⃣ Technical Implementation (300 words)
   - What technologies were used
   - Role of each technology
   - Explanation of key technical points
   - Key parameters or configurations

3️⃣ System Architecture (simple flowchart)
   - Complete data flow
   - Relationships between parts
   - Execution process

4️⃣ Achievements and Benefits (200 words)
   - What was solved
   - What benefits were brought
   - Reusable aspects
```

---

## CoinGlass Project - Practical Example

**1️⃣ Problem and Solution**

The heatmap on the CoinGlass website cannot be obtained via API and is dynamically rendered by React.

Solution: Use Playwright browser automation for screenshots.
- Launch a headless browser, visit the website, wait for animation to complete.
- Take a precise screenshot and crop it to get a clean heatmap.

Why this solution was chosen:
- API: No public API for the website ❌
- Scraper: Cannot handle JavaScript dynamic rendering ❌
- Screenshot: Directly obtains the final visual result, most accurate ✅

**2️⃣ Technical Implementation**

-   **Playwright** - Browser automation framework, controls browser behavior.
-   **Chromium** - Headless browser engine, executes JavaScript.
-   **PIL** - Python Imaging Library, for precise cropping.

Key technical points:
-   Waiting strategy: 5 seconds initial + 7 seconds animation (ensures React rendering and CSS animations complete).
-   CSS selector: `[class*="treemap"]` to locate the heatmap container.
-   Precise cropping: Left -1px, Right -1px, Top -1px, Bottom -1px → 840×384px → 838×382px (completely borderless).

**3️⃣ System Architecture**

```
Crontab scheduled task (hourly)
         ↓
   Python script starts
         ↓
Playwright launches browser
         ↓
Visit website → Wait (5s) → Click coin → Wait (7s)
         ↓
Screenshot (840×384px)
         ↓
PIL cropping (Left -1, Right -1, Top -1, Bottom -1)
         ↓
Final Heatmap (838×382px)
         ↓
Save to local directory
```

**4️⃣ Achievements and Benefits**

Achievements:
-   ✓ Automatically and regularly obtains heatmaps (no manual intervention).
-   ✓ 100% success rate (completely reliable).
-   ✓ Complete historical data (persistently saved).

Benefits:
-   Efficiency: From manual 5 minutes → automatic 16.5 seconds.
-   Annual savings: 243 hours of work time.
-   Quality: Consistent screenshot quality.

Reusable experience:
-   Playwright browser automation best practices.
-   Anti-scraping detection bypass strategies.
-   Dynamic rendering page waiting patterns.

---

*Version: v1.0 (Essential Edition)*
*Update: 2025-10-19*
