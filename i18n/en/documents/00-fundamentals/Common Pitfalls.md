```markdown
# 🕳️ Common Pitfalls Summary

> Common issues and solutions during the Vibe Coding process

---

<details open>
<summary><strong>🤖 AI Conversation Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| AI generated code doesn't run | Insufficient context | Provide full error message, explain execution environment |
| AI repeatedly modifies the same issue | Stuck in a loop | Try a different approach, or start a new conversation |
| AI hallucination, fabricating non-existent APIs | Outdated model knowledge | Provide official documentation link for AI reference |
| Code becomes messier after AI modifications | Lack of planning | Have AI propose a plan first, then confirm before coding |
| AI doesn't understand my requirements | Vague description | Use concrete examples, provide input/output samples |
| AI forgets previous conversation | Context loss | Re-provide key information, or use memory bank |
| AI modifies code it shouldn't have | Unclear instructions | Explicitly state "only modify xxx, don't touch other files" |
| AI generated code style is inconsistent | No style guide | Provide code style guide or example code |

</details>

---

<details open>
<summary><strong>🐍 Python Virtual Environment Related</strong></summary>

### Why use a virtual environment?

- Avoid dependency conflicts between different projects
- Keep the system Python clean
- Easy to reproduce and deploy

### Create and use .venv

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate virtual environment
deactivate
```

### Common Problems

| Problem | Reason | Solution |
|:---|:---|:---|
| Environment setup always fails | Global pollution | Delete and restart, isolate with `.venv` virtual environment |
| `python` command not found | Virtual environment not activated | Run `source .venv/bin/activate` first |
| Package installed but import error | Installed globally | Confirm virtual environment is active before `pip install` |
| Dependency conflicts between projects | Sharing global environment | Create a separate `.venv` for each project |
| VS Code uses wrong Python interpreter | Interpreter not selected correctly | Ctrl+Shift+P → "Python: Select Interpreter" → choose .venv |
| pip version too old | Virtual environment defaults to old version | `pip install --upgrade pip` |
| requirements.txt missing dependencies | Not exported | `pip freeze > requirements.txt` |

### One-click environment reset

Environment completely messed up? Delete and restart:

```bash
# Delete old environment
rm -rf .venv

# Recreate
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</details>

---

<details open>
<summary><strong>📦 Node.js Environment Related</strong></summary>

### Common Problems

| Problem | Reason | Solution |
|:---|:---|:---|
| Node version mismatch | Project requires specific version | Use nvm to manage multiple versions: `nvm install 18` |
| `npm install` error | Network/Permissions issue | Change registry, clear cache, delete node_modules and reinstall |
| Global package not found | PATH not configured | Add `npm config get prefix` to PATH |
| package-lock conflict | Collaborative work | Consistently use `npm ci` instead of `npm install` |
| node_modules too large | Normal phenomenon | Add to .gitignore, do not commit |

### Common Commands

```bash
# Change to Taobao registry
npm config set registry https://registry.npmmirror.com

# Clear cache
npm cache clean --force

# Delete and reinstall
rm -rf node_modules package-lock.json
npm install

# Switch Node version with nvm
nvm use 18
```

</details>

---

<details open>
<summary><strong>🔧 Environment Configuration Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Command not found | Environment variable not configured | Check PATH, restart terminal |
| Port in use | Not properly closed last time | `lsof -i :port_number` or `netstat -ano \| findstr :port_number` |
| Insufficient permissions | Linux/Mac permissions | `chmod +x` or `sudo` |
| Environment variables not taking effect | Not sourced | `source ~/.bashrc` or restart terminal |
| .env file not taking effect | Not loaded | Use `python-dotenv` or `dotenv` package |
| Windows path issues | Backslashes | Use `/` or `\\` or `Path` library |

</details>

---

<details open>
<summary><strong>🌐 Network Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| GitHub access slow/timeout | Network restrictions | Configure proxy, refer to [Network Environment Configuration](../从零开始vibecoding/01-网络环境配置.md) |
| API call failed | Network/Key issue | Check proxy, API Key validity |
| Terminal not using proxy | Incomplete proxy configuration | Set environment variables (see below) |
| SSL certificate error | Proxy/Time issue | Check system time, or temporarily disable SSL verification |
| pip/npm download slow | Source abroad | Use domestic mirror source |
| git clone timeout | Network restrictions | Configure git proxy or use SSH |

### Terminal Proxy Configuration

```bash
# Temporary setting (effective for current terminal)
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

# Permanent setting (add to ~/.bashrc or ~/.zshrc)
echo 'export http_proxy=http://127.0.0.1:7890' >> ~/.bashrc
echo 'export https_proxy=http://127.0.0.1:7890' >> ~/.bashrc
source ~/.bashrc

# Git Proxy
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

</details>

---

<details open>
<summary><strong>📝 Code Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Code file too large, AI cannot process | Exceeds context | Split files, only provide relevant parts to AI |
| Modified code not taking effect | Cache/Not saved | Clear cache, confirm save, restart service |
| Merge conflicts | Git conflict | Let AI help resolve: paste conflict content |
| Dependency version conflicts | Version incompatibility | Specify version number, or isolate with virtual environment |
| Chinese garbled characters | Encoding issue | Unify to UTF-8, add `# -*- coding: utf-8 -*-` at file beginning |
| Hot update not taking effect | Listening issue | Check if file is within listening range |

</details>

---

<details open>
<summary><strong>🎯 Claude Code / Cursor Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Claude Code cannot connect | Network/Authentication | Check proxy, re-`claude login` |
| Cursor completion is slow | Network latency | Check proxy configuration |
| Quota used up | Limited free quota | Switch accounts or upgrade to paid |
| Rule file not taking effect | Path/Format error | Check `.cursorrules` or `CLAUDE.md` location |
| AI cannot read project files | Workspace issue | Confirm opened in correct directory, check .gitignore |
| Generated code in wrong location | Cursor position | Place cursor at correct position before generating |

</details>

---

<details open>
<summary><strong>🚀 Deployment Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Runs locally, but fails to deploy | Environment differences | Check Node/Python versions, environment variables |
| Build timeout | Project too large | Optimize dependencies, increase build time limit |
| Environment variables not taking effect | Not configured | Set environment variables on deployment platform |
| CORS cross-origin error | Backend not configured | Add CORS middleware |
| Static files 404 | Path issue | Check build output directory configuration |
| Insufficient memory | Free tier limitations | Optimize code or upgrade plan |

</details>

---

<details open>
<summary><strong>🗄️ Database Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Connection refused | Service not started | Start database service |
| Authentication failed | Incorrect password | Check username and password, reset password |
| Table does not exist | Not migrated | Run migration |
| Data loss | Not persisted | Docker with volume, or use cloud database |
| Too many connections | Connections not closed | Use connection pool, close connections promptly |

</details>

---

<details open>
<summary><strong>🐳 Docker Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Image pull failed | Network issue | Configure image accelerator |
| Container failed to start | Port conflict/Configuration error | Check logs `docker logs container_name` |
| File changes not taking effect | Volume not mounted | Add `-v` parameter to mount directory |
| Insufficient disk space | Too many images | `docker system prune` to clean up |

</details>

---

<details open>
<summary><strong>🧠 Large Language Model Usage Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Token limit exceeded | Input too long | Refine context, only provide necessary information |
| Reply truncated | Output token limit | Ask AI to output in segments, or say "continue" |
| Significant differences in results between models | Different model characteristics | Choose model based on task: Claude for code, GPT for general purpose |
| Temperature parameter effect | Temperature setting | Use low temperature (0-0.3) for code generation, high for creativity |
| System prompt ignored | Prompt too long/conflicting | Simplify system prompt, put important parts first |
| JSON output format error | Model unstable | Use JSON mode, or ask AI to output only code blocks |
| Multi-turn conversation quality degrades | Context pollution | Regularly start new conversations, keep context clean |
| API call returns 429 error | Rate limit | Add delayed retries, or upgrade API plan |
| Streaming output garbled | Encoding/Parsing issue | Check SSE parsing, ensure UTF-8 |

</details>

---

<details open>
<summary><strong>🏗️ Software Architecture Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Code becomes messier | No architectural design | Draw architecture diagram first, then write code |
| Changing one place breaks others | Too tightly coupled | Split modules, define clear interfaces |
| Don't know where to put code | Directory structure messy | Refer to [General Project Architecture Template](../模板与资源/通用项目架构模板.md) |
| Too much duplicate code | No abstraction | Extract common functions/components |
| State management chaotic | Overuse of global state | Use state management libraries, one-way data flow |
| Configuration scattered | No unified management | Centralize in config files or environment variables |
| Difficult to test | Too many dependencies | Dependency injection, mock external services |

</details>

---

<details open>
<summary><strong>🔄 Git Version Control Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Committed files that shouldn't be | .gitignore not configured | Add to .gitignore, `git rm --cached` |
| Committed sensitive information | Not checked | Use git-filter-branch to clean history, change key |
| Don't know how to resolve merge conflicts | Unfamiliar with Git | Use VS Code conflict resolution tools, or ask AI for help |
| Committed with wrong message | Mistake | `git commit --amend` to modify |
| Want to undo last commit | Committed wrongly | `git reset --soft HEAD~1` |
| Too many messy branches | No standard | Use Git Flow or trunk-based |
| Push rejected | New commits on remote | `pull --rebase` first, then push |

### Common Git Commands

```bash
# Discard changes in working directory
git checkout -- filename

# Discard changes in staging area
git reset HEAD filename

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View commit history
git log --oneline -10

# Stash current changes
git stash
git stash pop
```

</details>

---

<details open>
<summary><strong>🧪 Testing Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Don't know what to test | Lack of testing mindset | Test edge cases, abnormal situations, core logic |
| Tests are too slow | Test granularity too large | Write more unit tests, fewer E2E |
| Tests are unstable | Dependent on external services | Mock external dependencies |
| Tests pass but bugs appear online | Incomplete coverage | Add edge case tests, check with coverage |
| Changing code requires changing tests | Tests coupled to implementation | Test behavior, not implementation |
| AI generated tests are useless | Only tests happy path | Ask AI to supplement edge case and abnormal tests |

</details>

---

<details open>
<summary><strong>⚡ Performance Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Page loading slow | Resources too large | Compression, lazy loading, CDN |
| API response slow | Unoptimized queries | Add index, caching, pagination |
| Memory leak | Resources not cleaned up | Check event listeners, timers, closures |
| High CPU usage | Infinite loop/Repetitive calculation | Use profiler to locate hot spots |
| Slow database queries | N+1 problem | Use JOIN or batch queries |
| Frontend stuttering | Too many re-renders | React.memo, useMemo, virtual list |

</details>

---

<details open>
<summary><strong>🔐 Security Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| API Key leaked | Committed to Git | Use environment variables, add to .gitignore |
| SQL injection | String concatenation for SQL | Use parameterized queries/ORM |
| XSS attack | User input not escaped | Escape HTML, use CSP |
| CSRF attack | No token verification | Add CSRF token |
| Passwords stored in plaintext | Lack of security awareness | Use bcrypt or other hashing algorithms |
| Sensitive information in logs | Printed what shouldn't be | Anonymize data, disable debug in production |

</details>

---

<details open>
<summary><strong>📱 Frontend Development Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Styles not taking effect | Priority/Cache | Check selector priority, clear cache |
| Mobile adaptation issues | No responsive design | Use rem/vw, media queries |
| White screen | JS error | Check console, add error boundaries |
| State not synchronized | Asynchronous issues | Use useEffect dependencies, or state management library |
| Component not updating | Reference not changed | Return new object/array, do not modify directly |
| Bundle size too large | No optimization | On-demand import, code splitting, tree shaking |
| Cross-origin issue | Browser security policy | Backend configure CORS, or use proxy |

</details>

---

<details open>
<summary><strong>🖥️ Backend Development Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| API response slow | Synchronous blocking | Use asynchronous, put time-consuming tasks in queue |
| Concurrency issues | Race conditions | Add locks, use transactions, optimistic locking |
| Service crashed without detection | No monitoring | Add health checks, alerts |
| Logs not helping to find issues | Incomplete logs | Add request_id, structured logging |
| Different environment configuration | Hardcoding | Use environment variables to distinguish dev/prod |
| OOM crashes | Memory leak/Too much data | Paging, streaming, check for leaks |

</details>

---

<details open>
<summary><strong>🔌 API Design Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| API naming chaotic | No standard | Follow RESTful, use HTTP methods as verbs |
| Return format inconsistent | No agreement | Unify response structure `{code, data, message}` |
| Version upgrade difficult | No version control | Add version number to URL `/api/v1/` |
| Documentation and implementation inconsistent | Manual maintenance | Use Swagger/OpenAPI to auto-generate |
| Error messages unclear | Only returns 500 | Refine error codes, return useful information |
| Pagination parameters inconsistent | Each written differently | Unify `page/size` or `offset/limit` |

</details>

---

<details open>
<summary><strong>📊 Data Processing Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Data format incorrect | Type conversion issue | Perform type validation and conversion properly |
| Timezone issues | Timezones not unified | Store in UTC, convert to local for display |
| Precision loss | Floating-point issues | Use integers for currency (cents), or Decimal |
| Large file processing OOM | Loaded all at once | Stream processing, chunked reading |
| Encoding issues | Not UTF-8 | Unify to UTF-8, specify encoding when reading files |
| Null value handling | null/undefined | Perform null checks, provide default values |

</details>

---

<details open>
<summary><strong>🤝 Collaboration Related</strong></summary>

| Problem | Reason | Solution |
|:---|:---|:---|
| Code style inconsistent | No standard | Use ESLint/Prettier/Black, unify configuration |
| PR too large, difficult to review | Too many changes | Small, incremental commits, one PR per feature |
| Documentation outdated | No one maintains | Update code and documentation together, CI check |
| Don't know who is responsible | No owner | Use CODEOWNERS file |
| Reinventing the wheel | Unaware of existing solutions | Establish internal component library/documentation |

</details>

1.  **Check error message** - Copy it completely to AI
2.  **Minimal reproduction** - Find the simplest code that reproduces the issue
3.  **Bisection method** - Comment out half of the code, pinpoint the problem area
4.  **Change environment** - Try a different browser/terminal/device
5.  **Restart magic** - Restart service/editor/computer
6.  **Delete and restart** - If the environment is messy, delete and recreate the virtual environment

---

## 🔥 Ultimate Solution

Still can't figure it out? Try this prompt:

```
I encountered a problem and have tried many methods without success.

Error message:
[Paste full error]

My environment:
- Operating System:
- Python/Node Version:
- Relevant dependency versions:

I have already tried:
1. xxx
2. xxx

Please help me analyze possible causes and provide solutions.
```

---

## 📝 Contribution

Found a new pitfall? Welcome to PR to supplement!
```
