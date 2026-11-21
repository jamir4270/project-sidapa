# Lab 1 — Run a Language Model on Your Own Laptop

*Hands-on learning lab. Written 2026-11-21. Time: about 1 hour. Machine: your ThinkPad T14 (Windows).*

## What this lab is about

So far the study has been ideas on paper: "compression," "quantization levels," "Cebuano gets hurt more."
This lab makes them real. You will:

1. Install **llama.cpp**, the same tool your thesis uses to compress and run models.
2. Download a small AI model and **chat with it entirely offline** on your laptop.
3. Ask it the same question in **English, Tagalog and Cebuano** and compare.
4. Swap in a **heavily compressed** version of the same model and see what breaks.
5. **Measure your laptop's speed**, a number your methodology chapter needs.

**Analogy:** until now you've read about cars. Today you drive one around the block, first with a full tank
of fuel and then on fumes, and notice how it handles.

> **Important:** the model files in this lab were compressed by someone else (Unsloth). They're fine for learning.
> **The thesis never uses them**: for the real experiments you compress every model yourself from the original
> weights, so you control the calibration (see `docs/decisions.md`, 2026-11-17).

---

## Words you'll meet

| Term | Plain meaning |
|---|---|
| **Model** | The trained AI: billions of numbers (weights) learned by a company like Alibaba (Qwen) |
| **llama.cpp** | Free program that runs and compresses models on ordinary computers, without needing a big GPU |
| **GGUF** | The file format llama.cpp uses: one file holds the whole model. Think of it as an MP3 for models. |
| **Hugging Face** | The "GitHub of AI models": where companies publish model files for free download |
| **Quantization level** (e.g. `Q4_K_M`) | How much the model was compressed. `Q4` ≈ 4 bits per number; `K` = the modern "K-quant" method; `M` = medium (some important parts kept at higher precision). `Q2_K` ≈ 2–3 bits: much smaller, much rougher. |
| **Server** | A program that waits for requests. Here, `llama-server` waits for your chat messages and replies. |
| **localhost:8080** | "This computer, door number 8080." The chat page lives on your own laptop, not the internet. |
| **Token** | A chunk of text (a word or part of a word). Models read and write in tokens. |
| **Tokens per second (t/s)** | Speed. How fast the model reads your prompt, and how fast it writes its answer. |

---

## Step 1 — Install llama.cpp (~2 minutes)

**What you're doing:** installing the engine. Without it, a model file is just a big file of numbers;
llama.cpp is what loads those numbers and makes them answer.

**Why llama.cpp and not an easier app (like Ollama):** easier apps hide the parts your thesis is about.
llama.cpp gives you the exact tools you'll use later: `llama-quantize` (compress), `llama-imatrix` (calibrate)
and `llama-bench` (measure speed). Learning it now is learning your research instrument.

Run (winget is Windows' built-in app installer; this package was confirmed available on 2026-11-21, version b12602):

```bash
winget install ggml.llamacpp
```

Then **close the terminal and open a new one**, so Windows finds the new commands.

**Check it worked.** This should print a version number (like `b12602`):

```bash
llama-cli --version
```

**See what hardware it can use.** It lists the devices llama.cpp can run on: maybe your Vega iGPU (through
Vulkan, a graphics interface), maybe only the CPU:

```bash
llama-server --list-devices
```

| You see | Meaning |
|---|---|
| A Vulkan device (e.g. "AMD Radeon Graphics") | The installed build can use your iGPU. It might or might not be faster than the CPU; Step 5 tells you. |
| Only CPU | Fine. Your 8-core Ryzen handles a 1.7B model well. |
| `command not found` | You didn't reopen the terminal, or the install failed. Reopen; if it still fails, paste the error to Claude. |

**Thesis link:** your methodology chapter records the llama.cpp **version** for every run, because results can
change between versions (AGENTS.md rule 5). This version number is the first one you'll record.

---

## Step 2 — Download a model and chat with it (~5 minutes)

**What you're doing:** starting a small chat server with **Qwen3-1.7B**, compressed to **Q4_K_M**.

- **Why Qwen3-1.7B:** it's small (1.7 billion parameters) and one of the candidate models in your study
  (`docs/methodology/experiment-design.md`). Its compressed file is roughly 1 GB (estimate).
- **Why Q4_K_M:** it's the popular "good enough" level: about a quarter of the original size with small quality loss.

```bash
llama-server -hf unsloth/Qwen3-1.7B-GGUF:Q4_K_M
```

**What the command means:**

| Part | Meaning |
|---|---|
| `llama-server` | Start the chat server |
| `-hf` | "Download this from Hugging Face" (only the first time; afterwards it's cached on your disk) |
| `unsloth/Qwen3-1.7B-GGUF` | The repository: Unsloth's GGUF copies of Qwen3-1.7B |
| `:Q4_K_M` | Which compression level to pick from that repository |

**What you should see:** download progress, then a lot of loading messages, then a line like
`server is listening on http://127.0.0.1:8080`.

Open **http://localhost:8080** in your browser. That chat page is running **entirely on your laptop**: turn off
Wi-Fi and it still works.

To stop the server later: press **Ctrl+C** in the terminal.

**Analogy:** the GGUF file is a frozen meal; llama.cpp is the microwave; the browser page is your plate.

---

## Step 3 — Ask the same question in three languages

**What you're doing:** a tiny, informal version of your study's core comparison: same model, same question,
different language.

Add `/no_think` at the end of each message. Qwen3 normally "thinks out loud" at length before answering;
`/no_think` switches that off so you see the answer directly. (Your real experiments must also switch thinking
off and record that you did; this is an open risk noted in `docs/status.md`.)

1. English: `What should a family prepare before a typhoon? /no_think`
2. Tagalog: `Ano ang dapat ihanda ng isang pamilya bago dumating ang bagyo? /no_think`
3. Cebuano: `Unsa ang angay andamon sa usa ka pamilya sa dili pa moabot ang bagyo? /no_think`

**What to look for** (you're the native speaker, so you're the best judge here):

| Check | Why it matters for the thesis |
|---|---|
| Does the Cebuano answer stay in Cebuano, or drift into Tagalog or English? | That's the "language switching" error category in RQ3 |
| Are verb forms natural (*mopalit* vs *mipalit*, *gi-* vs *mi-*)? | That's the "morphology error" category |
| Is the Cebuano answer as long and detailed as the English one? | Hints at how much less Cebuano the model knows |
| Does it invent strange facts? | The "hallucination" category |

Write a few notes in the table at the end of this lab.

**Important:** this is **exploration, not data**. One question can't prove anything; the real study uses 900
questions per language with error bars. The point is to build intuition, so the numbers later mean something to you.

---

## Step 4 — Feel the compression

**What you're doing:** loading the **same model** at a much harsher compression level, **Q2_K**, and asking the
**exact same questions**.

Stop the server (Ctrl+C), then:

```bash
llama-server -hf unsloth/Qwen3-1.7B-GGUF:Q2_K
```

Reload http://localhost:8080 and ask the three questions again.

**What's happening inside:** at Q4, each of the model's numbers is stored with about 4 bits (16 possible values).
At Q2, about 2–3 bits (4 to 8 possible values). Every number gets rounded much more coarsely.

**Analogy:** rounding every price in a store. Rounding ₱47.85 to ₱48 changes almost nothing (Q4). Rounding it to the
nearest ₱50 makes the receipts unreliable (Q2). The question is which language's "receipts" go wrong first.

**What to look for:** compare against your Step 3 notes. Does the Q2 version get worse in **all** languages
equally, or is **Cebuano hit harder**? Does it start switching languages, repeating itself or ignoring
the question?

**Thesis link:** this is RQ2 in miniature. The study measures this properly across five levels
(Q8_0, Q6_K, Q4_K_M, Q3_K_M, Q2_K), three languages and several models.

---

## Step 5 — Measure your laptop's speed

**What you're doing:** running llama.cpp's built-in benchmark. The study is about offline use on resource-constrained
devices, so the methodology includes real speed and memory numbers from an ordinary laptop: yours.

First find where llama.cpp saved the downloaded models. They're usually in
`C:\Users\Admin\AppData\Local\llama.cpp\` (`VERIFY` on your machine). Look for a file ending in `Q4_K_M.gguf`.

```bash
llama-bench -m "<full path to the Qwen3-1.7B Q4_K_M .gguf file>"
```

**What the output means:**

| Column | Meaning | Analogy |
|---|---|---|
| `pp512` | **Prompt processing:** tokens per second when reading a 512-token prompt | How fast the student reads the exam passage |
| `tg128` | **Text generation:** tokens per second when writing 128 tokens | How fast the student writes the answer |

For your thesis, **reading speed matters most**: Belebele prompts are a passage plus a question, and the answer is
one letter.

Run it again on the Q2_K file to compare. Smaller files are usually faster.

Paste the tables to Claude, and they'll be recorded in `docs/methodology/compute.md` ("Measured numbers").

---

## If something goes wrong

| Problem | Likely cause | Fix |
|---|---|---|
| `llama-cli` not recognized | Terminal opened before the install finished | Close and reopen the terminal |
| Download stuck or fails | Network or Hugging Face hiccup | Run the command again; it resumes |
| "Address already in use" | A server is still running | Ctrl+C the old one, or close that terminal |
| Very slow, or the laptop freezes | Not enough free RAM | Close Chrome and other apps; the 1.7B model needs about 1.5 GB (estimate) |
| An option isn't recognized | llama.cpp flags change between versions | Paste the error to Claude |

---

## Your notes (fill in)

| Question | Q4_K_M: English | Q4_K_M: Tagalog | Q4_K_M: Cebuano | Q2_K: Cebuano |
|---|---|---|---|---|
| Stayed in the right language? | | | | |
| Natural grammar and verb forms? | | | | |
| Detail and accuracy (1–5) | | | | |
| Anything odd? | | | | |

| Benchmark | pp512 (t/s) | tg128 (t/s) | Device (CPU/Vulkan) | Date |
|---|---|---|---|---|
| Qwen3-1.7B Q4_K_M | | | | |
| Qwen3-1.7B Q2_K | | | | |

---

## What you learned, and what's next

- **You now know** how a model runs locally, what a quantization level looks like in practice, and roughly how
  your laptop performs.
- **Next (Lab 2, on AWS):** download Qwen's **original** weights, compress them yourself to several levels with
  `llama-quantize`, and build a Cebuano calibration file with `llama-imatrix`. That's the real thesis workflow.
