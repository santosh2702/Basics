# GenAI / RAG / Prompt Engineering 

> Print‑friendly one‑pager followed by pocket flashcards. Keep this as your final‑hour cram sheet.

---

## 🔑 Quick Priorities

* Default stack: **Low temp + RAG + JSON schema validation + caching**.
* Chunking: **400–600 tokens**, **10–15% overlap**, heading‑aware; prefer **semantic** or **hybrid** splits.
* Retrieval: **Hybrid = BM25 (sparse) + dense embeddings**; rerank top‑k.
* Evaluation: **Faithfulness (citation precision/recall)** + **Task metric (EM/F1/ROUGE)** + **Ops (P95 latency, cost)**.
* Safety: guard vs **prompt injection**, **PII leakage**, **hallucinations**; enable **refusal** when unsure.

---

## 🧑‍💻 Prompt Engineering — Essentials

* **Zero‑shot / Few‑shot / CoT**: tradeoff between speed vs reasoning control; add final “**give concise answer**”.
* **Schema‑first prompts**: provide JSON schema & refusal clause; validate and auto‑repair if invalid.
* **Prompt chaining**: retrieve → plan → draft → critique → finalize.
* **Leakage/injection defense**: keep system server‑side, content isolation, tool allowlists, output filters.

### Reusable Prompts

**Summarization (JSON)**

```
System: You are a precise technical summarizer.
User: Summarize for a non‑technical reader in ≤5 bullets and 1 key quote.
Return valid JSON: {"bullets":[],"quote":""}.
If unsure, use nulls.
```

**Classification**

```
Label sentiment as one of {positive, neutral, negative}.
Return JSON {"label":"...","confidence":0‑1} only.
```

---

## 🤖 LLM Fundamentals

* **Encoder‑only (BERT)**: representations, search/classification.
* **Decoder‑only (GPT/LLaMA/Mistral/Claude‑style)**: generation & tool use.
* **Sampling**: temp↓ = deterministic; **top‑k** (fixed pool), **top‑p** (prob mass).
* **Adaptation**: full fine‑tune (costly) ⟶ **LoRA/PEFT** (efficient) ⟶ prompt‑tuning (cheapest).

---

## 📚 RAG Quick Diagram

Ingest → Split (400–600, 10–15% overlap) → Embed → Index (vector DB) → Query → Retrieve top‑k → (Rerank) → Compose prompt w/ citations → Generate → Validate JSON → Display + links.

**Vector DB options**: FAISS (local), Chroma (dev‑friendly), Pinecone/Weaviate/Milvus (managed/scale).

**Dense vs Sparse**: Dense = paraphrases/semantics; Sparse = exact/rare tokens. **Best: Hybrid**.

**Key knobs**: k (3–8), filters (metadata), reranker, cache, context window budget.

---

## 🧪 Evaluation Cheatsheet

* **Retrieval**: Recall\@k, MRR, nDCG.
* **Answering**: EM/F1/ROUGE; **faithfulness** (does answer quote retrieved text?).
* **Ops**: latency (P95/P99), error rate, token cost, cache hit.

---

## ☁️ Deployment Cliff Notes

* Serve via **FastAPI**; containerize; enable auth, rate limits, tracing.
* **Batch vs realtime**: throughput vs latency.
* **Monitoring**: schema validity, groundedness, jailbreak attempts, PII, cost.

---

## 🛠 Minimal Code Snips

**Word Frequency**

```python
from collections import Counter
Counter(t.lower() for t in text.split())
```

**Reverse String**

```python
s[::-1]
```

**JSON Parse (safe)**

```python
import json
try: obj=json.loads(s)
except json.JSONDecodeError as e: obj={"error":str(e)}
```

---

# 🧠 Flashcards (Front ▸ Back)

**What is prompt engineering?** ▸ Designing inputs/instructions to get reliable, safe, structured outputs.

**Zero‑shot vs Few‑shot vs CoT?** ▸ No examples vs examples vs guided reasoning; CoT improves reasoning, costs tokens.

**Prompt injection?** ▸ Inputs trying to override rules/exfiltrate secrets; mitigate with server‑side system, isolation, allowlists.

**Hallucination fixes?** ▸ RAG + lower temp + citations + verifier pass + schema validation + allow “I don’t know”.

**Temperature/top‑k/top‑p?** ▸ Temp scales randomness; top‑k = best k tokens; top‑p = smallest mass p set.

**Dense vs Sparse search?** ▸ Dense = semantic; Sparse (BM25) = keyword; use **hybrid**.

**Chunking heuristics?** ▸ 400–600 tokens, 10–15% overlap, heading/semantic aware.

**RAG steps?** ▸ Ingest → split → embed → index → retrieve → (rerank) → prompt+citations → generate.

**Evaluate chatbot?** ▸ Task metric + faithfulness + UX (resolution/CSAT) + Ops (latency/cost).

**Batch vs realtime?** ▸ Batch = throughput/cost; realtime = low‑latency SLA.

**Regularization?** ▸ L1/L2, dropout, early stop; reduces overfitting.

**Precision/Recall/F1?** ▸ TP/(TP+FP), TP/(TP+FN), harmonic mean.

**RF vs NN?** ▸ RF strong on tabular/low tuning; NN flexible, data‑hungry.

**Transfer learning?** ▸ Start from pre‑trained; fine‑tune minimal layers (e.g., LoRA).

---

## 🎯 Interview One‑liners

* “We use **hybrid retrieval** with reranking and measure **citation precision/recall** for faithfulness.”
* “Default: **low temp + schema‑first** prompts; invalid JSON triggers auto‑repair cycle.”
* “Chunking at **\~500 tokens** with **15% overlap** balanced recall and token cost.”
* “Caching at **embedding, retrieval, and generation** layers cut costs significantly.”

---

## 🧩 Mini RAG Demo (what you’ll get in the repo)

* `ingest.py` — loads sample docs, splits, embeds (MiniLM), indexes to **Chroma**.
* `app.py` — FastAPI with `/qa` (retrieval + simple generator); optional OpenAI plug‑in.
* `rag.py` — helpers for embed/query; hybrid ready stub.
* `data/` — a few example knowledge chunks.
