# NEXUS

### Verified Autonomous Software Maintenance Agent

**Investigate bugs. Generate tests. Propose fixes. Verify results.**

NEXUS is a developer-focused AI project designed to investigate software issues, understand code repositories, generate regression tests, propose controlled code changes, and independently verify whether a fix works.

> **Project status:** Early development. The initial FastAPI application is running, and the repository scanner file has been added. The complete autonomous maintenance workflow is still under development.

## Overview

NEXUS aims to help developers investigate and resolve software bugs through an evidence-driven workflow. Rather than trusting an AI-generated fix blindly, the system is designed to run tests and evaluate the outcome before reporting a fix as verified.

## Planned Workflow

1. **Repository Analysis** — Inspect the project structure and identify relevant source files.
2. **Code Retrieval (RAG)** — Retrieve code relevant to the reported issue.
3. **Bug Investigation** — Analyze errors, trace relevant code paths, and investigate possible root causes.
4. **Regression Test Generation** — Generate tests that capture the reported failure.
5. **Controlled Patch Proposal** — Propose a targeted code change and request approval before applying it.
6. **Independent Verification** — Execute relevant tests and assess whether the issue is resolved without introducing regressions.
7. **Evidence Report** — Report the outcome, test results, and any remaining issues.

*The workflow above describes the intended design; these stages are not all implemented yet.*

## Current Implementation

* [x] Initial FastAPI application
* [x] Initial API endpoint
* [x] Repository scanner file added
* [ ] Complete and test repository scanning
* [ ] Repository structure and code parsing
* [ ] Code-aware retrieval using RAG
* [ ] Bug investigation and regression test generation
* [ ] Controlled patch application and independent verification
* [ ] Benchmark-based evaluation

## Planned Technology Stack

| Component            | Technology                                |
| -------------------- | ----------------------------------------- |
| Backend API          | Python, FastAPI                           |
| Agent orchestration  | LangGraph or a controlled workflow        |
| Local coding model   | Ollama with a suitable coding LLM         |
| Code retrieval       | Embeddings, Qdrant, Tree-sitter           |
| Testing              | pytest and language-specific test runners |
| Version control      | Git and GitHub                            |
| Controlled execution | Docker sandbox                            |

*The technology stack is a plan and may evolve during development.*

## Core Principles

* **Evidence-driven investigation:** Ground findings in relevant code and execution results.
* **Human oversight:** Require approval before controlled code changes.
* **Independent verification:** Use actual test execution instead of relying only on an LLM's confidence.
* **Safe failure handling:** Report unsuccessful fixes honestly and avoid claiming success without evidence.
* **Reproducible evaluation:** Evaluate the system on software issues with known expected outcomes.

## Evaluation Plan

The project will be evaluated using repositories with known defects and expected behavior. Planned measurements include bug reproduction success, root-cause localization accuracy, regression-test effectiveness, patch correctness, regression rate, verification accuracy, and end-to-end task success.

No performance results are claimed at this stage.

## Project Roadmap

1. Repository scanning and validation
2. Repository structure analysis
3. Code-aware retrieval
4. Bug investigation tools and agent
5. Regression test generation
6. Controlled patching and human approval
7. Sandbox execution and independent verification
8. Multi-agent orchestration, security, and evaluation

## Getting Started

The project is currently under development. Setup instructions and usage examples will be added as the implementation becomes available.

## Project Status

NEXUS is an ongoing engineering project focused on verified, controlled AI-assisted software maintenance.
