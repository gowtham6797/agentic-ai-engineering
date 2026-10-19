# Agentic AI Engineering with Python 🚀

My hands-on journey from Python fundamentals to building, securing,
evaluating, and deploying production-ready AI agents.

This repository contains my own learning notes, practice code,
experiments, and projects as I follow the **Telusko Agentic AI
Engineering with Python** roadmap. The goal is to turn concepts into
working applications and build a portfolio of practical AI engineering
projects.

## Learning Approach

The roadmap follows six stages:

1.  **Foundations** --- Python, NLP basics, LLM concepts, and prompting.
2.  **Build** --- LLM APIs, structured outputs, LangChain, and RAG.
3.  **Orchestrate** --- LangGraph and CrewAI for workflows and
    multi-agent systems.
4.  **Connect** --- MCP and A2A for connecting tools and agents.
5.  **Harden** --- Security, reliability, evaluation, and observability.
6.  **Ship** --- APIs, user interfaces, cloud deployment, and a
    production-oriented capstone.

The emphasis is on practical code, real use cases, evaluation, security,
and deployment---not theory alone.

## Current Progress

-   [x] Started Python fundamentals and hands-on practice
-   [ ] Complete and consolidate Python foundations
-   [ ] Work through the AI engineering modules below
-   [ ] Build, test, document, and deploy projects as the relevant
    topics are learned

> Progress is intentionally updated as I complete and validate each
> topic. A folder or a watched lesson alone does not mean a topic is
> complete.

## Roadmap & Modules

### Stage 1 --- Foundations

#### M1. Agentic AI and Python Foundations

-   Agentic AI concepts and the LLM landscape
-   Tokens, embeddings, transformers, and context windows
-   Temperature, top-p, hallucinations, and tool calling
-   Python functions, classes, exceptions, modules, and files
-   Type hints, dataclasses, async/await, generators, decorators, and
    context managers
-   Virtual environments, dependencies, HTTP/JSON, basic SQL, Git, and
    command-line tools
-   Prompt engineering: few-shot prompting, decomposition, role
    prompting, reflection, and structured-output prompting

**Project direction:** Build a strong Python and LLM foundation before
moving into agent applications.

### Stage 2 --- Build

#### M2. LLM APIs, OpenAI Responses API & Agents SDK

-   Work with LLM APIs and SDKs
-   Multimodal inputs and cost control
-   Structured outputs and Pydantic
-   Function calling, hosted tools, and multi-turn interactions
-   Agents, tools, handoffs, sessions, guardrails, and tracing

**Project:** Intelligent Document Extraction Service

#### M3. LangChain

-   Models, prompts, tools, and agents
-   Structured outputs, memory, streaming, and batching
-   Embeddings and vector stores
-   Loading PDFs, web pages, CSVs, and databases
-   Handling OCR, tables, forms, images, charts, and page citations

**Project:** Tool-Enabled Customer Support Application

#### M4. Retrieval-Augmented Generation (RAG)

-   Indexing, retrieval, generation, and chunking
-   Grounded answers and citations
-   Retrieval evaluation: relevance, groundedness, and citation accuracy
-   Query rewriting, multi-query retrieval, hybrid search, metadata
    filtering, and reranking
-   Corrective/adaptive RAG, Self-RAG, GraphRAG, and retrieval
    optimization

**Project:** Secure Enterprise RAG Assistant

### Stage 3 --- Orchestrate

#### M5. LangGraph

-   Stateful workflows, persistence, and durable execution
-   Human-in-the-loop interactions and interrupts
-   Short-term and long-term memory
-   Parallel, conditional, and iterative workflows
-   Multi-agent patterns, supervisors, subgraphs, and tool routing

**Project:** Research & Report Agent

#### M6. CrewAI

-   Agents, tasks, crews, tools, and knowledge
-   Sequential and hierarchical processes
-   Delegation, memory, guardrails, callbacks, and observability
-   Flows, typed state, routing, asynchronous work, and checkpointing
-   Testing and deployment patterns

**Project:** Multi-Agent Customer Onboarding Workflow

### Stage 4 --- Connect

#### M7. MCP and A2A

-   Model Context Protocol (MCP): tools, resources, prompts, and server
    transports
-   Local and remote MCP servers, discovery, and error handling
-   Agent-to-Agent (A2A): agent cards, capability discovery, tasks,
    artifacts, and streaming
-   Authentication, OAuth, and MCP security
-   Integrating MCP with OpenAI, LangChain, LangGraph, and CrewAI

**Project:** Cross-Agent Workflow

### Stage 5 --- Harden

#### M8. Agent Security and Reliability

-   Timeouts, retries, backoff, rate limits, and idempotency
-   Limits for steps, tokens, and cost
-   Durable execution, queues, caching, and health checks
-   Prompt injection, goal hijacking, tool misuse, and memory poisoning
-   Input validation, least privilege, human approval, identity, and
    permissions
-   Output sanitization, sandboxing, PII protection, audit trails, and
    secrets management

**Project:** Hardening an Agent for Production

#### M9. Evaluation and Observability

-   Tracing, dashboards, alerts, and monitoring
-   Offline evaluation and regression testing
-   Tool-selection accuracy, agent trajectories, and task completion
-   Groundedness and citation correctness
-   LLM-as-judge limitations, safety tests, and adversarial tests
-   Cost and latency tracking

**Project:** Evaluation & Monitoring Harness

### Stage 6 --- Ship

#### M10. Production APIs and User Interfaces

-   FastAPI, server-sent events (SSE), and WebSockets
-   Authentication, secrets, sessions, and recovery
-   Human-approval interfaces, tool-call status, citations, feedback,
    and audit trails
-   Error handling and retries
-   UI options including Streamlit, Chainlit, Gradio, React, and Next.js

**Project:** Full-Stack Agent App

#### M11. AWS and Google Cloud Deployment

-   Docker and CI/CD with GitHub Actions
-   Deployment workflows, tests, evaluations, preview environments,
    staging, and rollback
-   AWS services and Bedrock AgentCore
-   Google Cloud agent platform and related services
-   Versioning, quality gates, privacy, and cost considerations

**Project:** Ship an Agent to AWS Bedrock AgentCore

#### M12. Forward Deployed Engineer (FDE) Capstone

Apply the full delivery loop:

**Discover → Scope → Build → Ship → Improve**

Capstone directions in the roadmap include: - Enterprise knowledge and
support agent - SQL/BigQuery analytics agent - Operations agent
integrating tools such as email, CRM, calendar, OAuth, approvals, MCP,
and A2A

Expected capstone practices include architecture documentation, source
control, automated tests, an evaluation dataset, a security checklist, a
live deployment, monitoring, and a demo.

## Project Portfolio

The roadmap's project sequence is intended to build toward practical,
production-oriented systems:

  -----------------------------------------------------------------------
  Module                              Project
  ----------------------------------- -----------------------------------
  M2 --- LLM APIs and Agents SDK      Intelligent Document Extraction
                                      Service

  M3 --- LangChain                    Tool-Enabled Customer Support
                                      Application

  M4 --- RAG                          Secure Enterprise RAG Assistant

  M5 --- LangGraph                    Research & Report Agent

  M6 --- CrewAI                       Multi-Agent Customer Onboarding
                                      Workflow

  M7 --- MCP and A2A                  Cross-Agent Workflow

  M8 --- Security and Reliability     Hardening an Agent for Production

  M9 --- Evaluation and Observability Evaluation & Monitoring Harness

  M10 --- APIs and UI                 Full-Stack Agent App

  M11 --- Cloud Deployment            Agent deployed to AWS Bedrock
                                      AgentCore

  M12 --- Capstone                    Customer-focused, deployed AI agent
                                      system
  -----------------------------------------------------------------------

Project folders and implementation details will be added as I reach each
module. The list reflects the roadmap; it does not imply that these
projects are already completed.

## Repository Structure

``` text
agentic-ai-engineering/
├── Python/
│   ├── basics/
│   ├── oops/
│   └── advanced/
├── 03-llm-foundations/
├── 04-llm-apis-and-agents-sdk/
├── 05-langchain/
├── 06-rag/
├── 07-langgraph/
├── 08-crewai/
├── 09-mcp-and-a2a/
├── 10-agent-security-and-reliability/
├── 11-evaluation-and-observability/
├── 12-production-apis-and-ui/
├── 13-cloud-deployment/
├── projects/
└── README.md
```

This is a suggested future structure. I will add folders when needed and
may adjust the numbering to match the way I organize the modules in
practice.

## Tools & Technologies

**Current tools** - Python - Visual Studio Code - Git and GitHub

**Planned exploration from the roadmap** - LLM APIs, OpenAI Responses
API, and Agents SDK - Pydantic and structured outputs - LangChain,
LangGraph, and CrewAI - Vector stores and RAG - MCP and A2A - FastAPI
and application UI frameworks - Docker, GitHub Actions, cloud
deployment, evaluation, and observability tools

## How I Document Each Topic

For each topic or project, I aim to include: - Concise notes on the key
concepts - Original code examples and practice exercises - Setup and run
instructions where applicable - Dependencies and configuration
guidance - What I learned, challenges, and improvements - Tests and
evaluation details for larger projects

## Safe and Responsible Development

-   Never commit API keys, passwords, tokens, or `.env` files.
-   Use environment variables or a local secrets mechanism for
    credentials.
-   Do not upload paid course recordings or copyrighted course
    materials.
-   Prefer original practice code, notes, and projects.
-   Test and evaluate agent behavior before treating an application as
    production-ready.

## Goal

Build the skills to take an AI application from a real customer problem
to a working, evaluated, secure, and deployed system---and document that
progress in public through code and projects.

**Learn continuously. Build practically. Ship responsibly.** 🚀
