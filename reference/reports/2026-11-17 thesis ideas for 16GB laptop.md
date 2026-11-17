# Bring the Cebuano Questions to Your Laptop

**The short answer:** with a 16GB Ryzen 7 ThinkPad, your strongest thesis is no longer the chunking study that topped the earlier report. It is a **Cebuano-first measurement study you can run mostly on your own laptop.** The safest version asks how much "shrinking" a small AI model (quantization) hurts it in Cebuano and Tagalog compared to English, then sorts its mistakes into types using your native-speaker judgment. The more ambitious version adds the **first retrieval test for Cebuano**: can search tools find the right Cebuano passage for a Cebuano question? Both gaps are still open in late 2026. FilBench, the main Filipino AI benchmark, has no retrieval category at all ([FilBench](https://arxiv.org/abs/2508.03523v1)). The big 2025 Southeast Asian embedding benchmark has no Cebuano and no Filipino retrieval tasks ([SEA-BED](https://arxiv.org/html/2508.12243v2)). And none of the quantization papers we checked report any Philippine language ([arXiv 2407.03211](https://arxiv.org/html/2407.03211v2); [arXiv 2508.20893](https://arxiv.org/abs/2508.20893)).

Three things changed since the first report. First, the new laptop makes 7–8B models usable at roughly 8–13 tokens per second (about fast-typing speed), so most experiments no longer need the cloud. Second, chunking has become crowded: at least three papers now test it end to end. Third, cross-lingual NER between Philippine languages has been partly started by HiligayNER. My top recommendation (end of this report) combines the quantization study and the Cebuano retrieval test into one pipeline. It needs no judge model, roughly zero API spending, and every piece can be checked against a known right answer.

A note on your typed "2556 gb": I am treating it as a **256GB SSD**. Everything below assumes that.

**How to read the flags.** *(estimate)* means I calculated or extrapolated a number; you should measure it yourself in week 1. *(unverified)* means the claim comes from general knowledge or a source we could not open, so check it before you cite it.

---

## First, a plain-language dictionary

You will see these words in every paper you read. Learn them once here.

| Term | What it means, plainly |
|---|---|
| **LLM** (large language model) | The chatbot-style model that reads text and writes text, like ChatGPT, Qwen, Gemma or Llama. "4B" or "8B" means 4 or 8 billion internal numbers ("parameters"). Bigger is usually smarter but slower and needs more memory. |
| **Token** | The unit models read. Roughly ¾ of an English word. Cebuano usually needs more tokens per word because models saw less of it. |
| **Tokens/s** | Speed. "10 tokens/s" is roughly a fast human typing speed. "Prompt processing" is how fast the model *reads*; "generation" is how fast it *writes*. |
| **Context window** | How much text the model can read at once, like the size of its desk. |
| **RAG** (retrieval-augmented generation) | An "open-book exam" for the AI. Before answering, a search step finds relevant passages and pastes them into the prompt. The model then answers from those pages instead of from memory. |
| **Retriever** | The search part of RAG. It picks which passages go into the prompt. |
| **Embedding** | A list of numbers that captures a text's meaning, like GPS coordinates for ideas. Texts about similar things land near each other. An **embedder** is the small model that makes these numbers. |
| **Dense retrieval** | Searching by embeddings: find passages whose "meaning coordinates" are closest to the question's. Good at paraphrases. |
| **BM25** | Old-school keyword search (1990s math, still strong). It scores passages by shared words, giving rare words more weight. Good at names, numbers and exact terms. It needs no AI model and runs instantly. |
| **Hybrid search / RRF** | Run BM25 and dense search, then merge the two ranked lists. **RRF** (reciprocal rank fusion) is the simplest merge: items ranked high on *either* list float up. |
| **Reranker (cross-encoder)** | A second, slower, more careful judge. The retriever grabs the top 50–100 candidates fast; the reranker reads each one *together with* the question and re-orders them. Like a librarian who pulls 100 books, then actually skims them. |
| **Chunking** | Cutting long documents into smaller pieces ("chunks") before embedding them. Chunk size and cut style (fixed length, by sentence, by topic) are the "knobs." |
| **Recall@k** | Out of all questions, how often the correct passage appears somewhere in the top *k* results. Recall@5 = "was the right page in the top 5?" |
| **nDCG@10, MRR** | Ranking scores that also reward putting the right answer *higher*. MRR is basically "1 divided by the rank of the first correct hit," averaged. |
| **Quantization** | Shrinking a model by storing its numbers with fewer digits. Like saving a photo as a smaller JPEG: much less space, slightly blurrier. "8-bit" is mild; "4-bit" is strong; "2-bit" is very blurry. |
| **GGUF, Q4_K_M, Q8_0** | GGUF is the file format that laptop tools (llama.cpp, LM Studio, Ollama) load. The suffix is the shrink level: Q8_0 ≈ 8-bit, Q4_K_M ≈ 4-bit (the popular default), Q2_K ≈ 2-bit. |
| **llama.cpp / Ollama / LM Studio** | Free programs that run GGUF models on your laptop. LM Studio has a GUI; llama.cpp is the engine underneath with command-line tools. |
| **iGPU, Vulkan, ROCm** | Your laptop's graphics chip is built into the processor ("integrated GPU") and shares the main 16GB of memory. **Vulkan** and **ROCm** are two ways for software to use it. On your chip, Vulkan is the one that works well. |
| **NPU** | A low-power "AI chip" on newer Ryzen AI processors. Only the newest kind runs LLMs today. |
| **LLM-as-judge** | Using one AI model to grade another model's answers. Cheap and scalable, but the grader has its own biases. |
| **Position bias** | A judge preferring whichever answer it sees first (or second), regardless of quality. You test it by swapping the order. |
| **Cohen's kappa (κ)** | Agreement between two graders *after removing lucky agreement by chance*. 1 = perfect, 0 = no better than coin flips. Raw "% agree" always looks better than kappa. |
| **Closed-book baseline** | Asking the model the question with *no* retrieved passage. If it still answers right, the question tests memory, not retrieval. |
| **Contamination** | The test questions leaked into the model's training data, so high scores mean memorization, not skill. |
| **NER** (named entity recognition) | Tagging names in text: people (PER), organizations (ORG), places (LOC). |
| **F1** | One score combining "how many of my tags were right" (precision) and "how many real names did I catch" (recall). |
| **Zero-shot / few-shot transfer** | Train on language A, test on language B with zero (or a few) B examples. |
| **Fine-tuning / LoRA** | Further training an existing model on your data. LoRA is a cheap version that trains a small add-on instead of the whole model. |
| **chrF / COMET** | Automatic translation scores. chrF compares characters with a reference translation; COMET uses a neural model. |
| **Confidence interval (CI) / bootstrap** | The "± margin" around a score. Bootstrap = recompute the score many times on random resamples of your questions to see how much it wobbles. |
| **Ablation** | Change one knob at a time and measure what happens. |
| **Error taxonomy** | A sorted list of mistake types with counts, e.g., "34% answered in Tagalog instead of Cebuano." |

---

## What your laptop can and cannot do

**The headline:** 1–4B models run comfortably and fast. **7–8B at 4-bit (Q4_K_M) is the practical sweet spot.** 12–14B technically fits but leaves almost nothing for anything else. Fine-tuning LLMs is a cloud job.

### Which chip do you have? Check this first

"Ryzen 7 T14" can mean two different chips, and it matters for the NPU only. Open Task Manager → Performance → CPU. If it says **Ryzen 7 7840U / 8840U** (Radeon 780M graphics), ignore the NPU; it has no working LLM software. If it says **Ryzen AI 7 PRO 360** (Radeon 880M), the NPU can run 1–4B models at very low power through AMD's Lemonade Server or FastFlowLM. That is a nice bonus, but your thesis does not need it ([Lemonade review](https://dev.to/jovan_chan_9500711396d4e6/amd-lemonade-review-2026-gpu-npu-and-multi-modal-3gd9); [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM)).

### Memory: about 10GB is really yours

Your graphics chip borrows from the same 16GB as Windows and your browser. After Windows and a few tabs take 4–6GB, **roughly 10GB is realistically free** *(estimate)*. On T14 AMD models the RAM is usually soldered, so 16GB is permanent *(unverified for your exact unit)*. On Windows, users report the graphics chip can use about half of system RAM as "shared" memory ([Framework forum](https://community.frame.work/t/fw13-7640u-760m-only-uses-half-of-available-ram-as-vram-in-lm-studio-under-windows-11/68755)). That is about 8GB for you, which is enough for an 8B model at Q4 (about 4.7GB) but probably not for 14B at Q4 (about 9GB). Linux is more flexible here, but Windows is fine for this thesis.

### Rough sizes and speeds

The best-measured close cousin of your laptop is a 2026 test on a Radeon 890M. There, **Qwen3-8B at Q4_K_M generated 9.9 tokens/s on battery-saver and 13.4 tokens/s plugged in on "performance" mode through Vulkan.** ROCm was only 4.8 tokens/s, and CPU-only on power-saver was just 2.6 ([msf.github.io](https://msf.github.io/blogpost/local-llm-performance-framework13.html)). Older 780M tests found a 7B model at about 10–13 tokens/s on the graphics chip versus about 7.6 on CPU ([Framework forum](https://community.frame.work/t/vram-allocation-for-the-7840u-frameworks/36613?page=2)). The key lesson: **the graphics chip helps most with reading long prompts (2–6× faster than CPU), which is exactly what RAG does.** Writing speed is limited by memory bandwidth, so it gains less.

| Model size | File size at Q4_K_M | File size at Q8_0 | Expected writing speed on your iGPU | Verdict |
|---|---|---|---|---|
| 1B | ~0.8 GB | ~1.3 GB | ~40–60 tok/s | Easy |
| 3–4B | ~2–2.5 GB | ~3.4–4.3 GB | ~18–30 tok/s | Your everyday workhorse |
| 7–8B | ~4.5–5 GB | ~8.5 GB | ~8–13 tok/s | Sweet spot (Q4/Q5); Q8 is borderline |
| 12–14B | ~7.3–9 GB | too big | ~4–7 tok/s | Only with everything else closed; use Kaggle instead |
| "30B-A3B" style MoE models | ~17+ GB | — | — | Does not fit; skip |

*All rows except the 8B anchor are (estimates)* extrapolated from the cited 8B numbers ([msf.github.io](https://msf.github.io/blogpost/local-llm-performance-framework13.html)). Measure your own in week 1. That table becomes your thesis's "experimental setup" section.

### Embeddings on CPU are cheap for small models, slow for big ones

Embedding (turning passages into meaning-coordinates) is light work for small embedders. **Embedding 100,000 passages takes roughly 6–17 minutes with a small 33M-parameter model, 20–55 minutes with a base-size one, and 2–5.5 hours with BGE-M3 or multilingual-e5-large** *(estimates; no measured Ryzen numbers were found)*. Converting the embedder to 8-bit ("INT8") makes CPU embedding about 2.7–3.4× faster while keeping 94–98% of quality ([Vespa](https://blog.vespa.ai/embedding-tradeoffs-quantified/)). Sentence-Transformers supports this through ONNX for AMD chips ([SBERT docs](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)). For reference, BGE-M3 has 568M parameters and is multilingual ([General Compute](https://www.generalcompute.com/blog/embedding-model-benchmarks-speed-vs-quality-for-rag-retrieval)). The search index itself is tiny: 100k passages × 1,024 numbers is only about 0.4GB.

### Fine-tuning: small encoders yes (slowly), LLMs no

Training an XLM-R base model for NER on CPU should take roughly 1–3 hours per pass over 10k sentences *(estimate)*. Kaggle's free T4 GPU is about 10–20× faster. Do not try to fine-tune LLMs (even LoRA) locally. PyTorch's AMD support on your chip is unofficial and error-prone ([PyTorch forum](https://discuss.pytorch.org/t/rocm-hipblaslt-error-with-gfx1103/212721)).

### Storage: 256GB is tight but enough

Windows and apps take roughly 60–100GB. Budget **40–60GB for the thesis**: 3–5 GGUF models at 2–5GB each, a couple of embedders, datasets and indexes *(estimate)*. Delete models you finish with, and park big files on Kaggle Datasets or Google Drive.

### Free cloud and cheap APIs (status as of late 2026)

**Kaggle is your most reliable free GPU**: T4-class GPUs, 12-hour sessions, and commonly about 30 GPU hours per week (Kaggle shows your exact quota in settings). **Colab free** gives a T4 with unpublished, changing limits and sessions of at most 12 hours ([gpuperhour.com](https://gpuperhour.com/blog/free-cloud-gpus-and-credits)). For free judge calls, **Groq's free tier allows 1,000 requests per day per model** on models like gpt-oss-20b and gpt-oss-120b, capped at 200,000 tokens per day. Gemini's free tier was cut sharply in December 2025 (developer reports say about 20 requests per day on Flash), and OpenRouter free gives 50 requests per day ([agentdeals.dev](https://agentdeals.dev/gemini-api-pricing-changes)). These free-tier limits come from aggregator sites, so recheck them when you write your proposal.

Paid judging is very cheap. Assuming 1,000 tokens in and 200 out per judgment, **1,000 judgments cost about $0.65 with GPT-5 mini, about $2 with Claude Haiku 4.5, and about $0.14–0.27 with gpt-oss on Groq** *(arithmetic from listed prices)* ([modelcompare.dev](https://modelcompare.dev/pt/compare/openai-gpt-5-mini-vs-anthropic-claude-haiku-4-5); [agentdeals.dev](https://agentdeals.dev/gemini-api-pricing-changes)). "Reasoning" models can bill hidden thinking tokens, so budget 2–3× for those. **A whole thesis's API cost is a few dollars, not $50.**

### Week-1 setup (do this regardless of topic)

Plug in the charger. Set Windows power mode to "Best performance." In the BIOS, if Lenovo offers a "UMA frame buffer" setting, pick something moderate like 2–4GB *(exact BIOS options unverified)*. Then install one runtime. The safest choice on AMD graphics is either **LM Studio** (GUI with a Vulkan engine) or the **llama.cpp Windows Vulkan zip** from its GitHub releases page. Ollama is simpler, but its late-2026 support for AMD integrated graphics was not verified.

```bash
# 1) Benchmark your laptop (record these numbers; they go in your thesis)
#    -ngl 99 = put all model layers on the graphics chip
llama-bench -m Qwen3-4B-Q4_K_M.gguf -ngl 99
llama-bench -m Qwen3-8B-Q4_K_M.gguf -ngl 99
llama-bench -m Qwen3-8B-Q4_K_M.gguf -ngl 0     # CPU-only, for comparison

# 2) Run a local model as an OpenAI-style API your Python code can call
llama-server -m Qwen3-4B-Q4_K_M.gguf -ngl 99 -c 4096 --port 8080

# 3) Python environment
pip install uv
uv venv && uv pip install "sentence-transformers[onnx]" faiss-cpu bm25s ranx datasets openai pandas sacrebleu
```

Then time embedding 1,000 passages with `intfloat/multilingual-e5-base` and multiply by 100. Create a Kaggle account, verify your phone (historically required for GPU access; *unverified for 2026*), and run one notebook that embeds the same passages with BGE-M3 on a T4. Finally, get free Groq and Google AI Studio API keys.

---

## Seven ideas, re-ranked for 16GB and late 2026

The ranking weighs four things: whether the gap is still open in late 2026, how well it runs on your laptop, how much ML expertise it needs, and how risky it is. The big moves since the earlier report: the two Cebuano ideas rise to the top, a small-judge idea rises, and chunking drops to last.

| Rank | Idea | Still open? (late 2026) | Laptop fit | Cloud needed? | API cost | Difficulty (1–5) | Biggest risk |
|---|---|---|---|---|---|---|---|
| 1 | Quantization damage on Cebuano/Tagalog + error taxonomy | Yes; no PH-language quantization study found | Excellent | No | ~$0 | **2** | Seen as "borrowed method"; small Cebuano test sizes |
| 2 | First Cebuano/Filipino retrieval & RAG benchmark | Yes; most clearly open | Very good | Optional (for BGE-M3) | ~$0–10 | **3** | Building a clean, licensed corpus |
| 3 | Can a small local judge grade RAG faithfulness? | Narrow gap; general judge work is crowded | Good (slow if "thinking") | Helpful | ~$5–20 | **3** | Fast-moving field; JSON parsing failures |
| 4 | RGB noise-robustness refresh on small open models | Yes, modest novelty | Very good | Optional | ~$0 | **2** | Contamination of 2023 questions |
| 5 | Hybrid search: which query types each method wins | Probably; needs a careful lit check | Excellent | No | $0 | **2** | Novelty may be weaker than it looks |
| 6 | Cross-lingual NER transfer among PH languages | Partly; HiligayNER did one row | Fair (CPU slow) | Yes (Kaggle) | $0 | **3** | Label-guideline mismatch; ML training needed |
| 7 | Chunking ablation, end to end | Crowded; only a narrow extension left | Excellent | No | ~$0 | **2** | Panel calls it incremental |

Agents and "build a chatbot" topics stay off the list for the same reasons as before: expensive, flaky to evaluate, and hard to frame as a falsifiable question.

---

### Idea 1 — How much does shrinking a model hurt Cebuano? (Rank 1, difficulty 2/5)

**(a) What it is and why it matters.** People run AI on laptops and phones by quantizing it: shrinking it to 4-bit or even 2-bit. In English the quality loss is small. But research shows the damage is **uneven across languages**. A study of multilingual models found automatic scores dropped only about 1.7% for Japanese, while human raters saw a 16% drop. It also found that the link between "less training data for this language" and "more damage" grew much stronger at 4-bit than at 8-bit, and that smaller models were more sensitive ([arXiv 2407.03211](https://arxiv.org/html/2407.03211v2)). A 2025 translation study on small Qwen3 and Llama models found that low-resource languages degrade much more, especially at 2-bit. It found GGUF the most consistent format, and found that calibrating the shrink with text in the matching language helps at low bit-widths ([arXiv 2508.20893](https://arxiv.org/abs/2508.20893)). **Neither study reports Tagalog or Cebuano**, and no Philippine-language quantization paper turned up. Your question: *does 4-bit or 3-bit quantization hurt Cebuano more than Tagalog, and both more than English? Does calibrating with Cebuano text fix it?* This matters for anyone in the Philippines deploying offline AI on cheap hardware.

The earlier report cited arXiv 2505.20276 for "4-bit hurts non-English more." We could not open that paper this time. Lean on the two papers above instead.

**(b) Example experiment.** Pick 4–5 small models: Qwen3 1.7B and 4B, Gemma 3 4B, Llama 3.2 3B, and SeaLLMs v3 1.5B (FilBench called SeaLLMs v3 1.5B "Pareto-efficient," meaning a good score for its size ([FilBench](https://arxiv.org/html/2508.03523v1))). Make each one at five shrink levels: Q8_0, Q6_K, Q4_K_M, Q3_K_M and Q2_K. Test on Cebuano tasks FilBench already uses. Belebele is multiple-choice reading comprehension (1,800 items shared with Filipino). SIB-200 is topic classification (99 Cebuano items). Tatoeba ceb→en is translation (2,876 items) ([FilBench](https://arxiv.org/html/2508.03523v1)). Run the same Belebele questions in English (control) and Tagalog. Your headline chart: accuracy versus bit-width, one line per language. The "quantization gap" is how much faster the Cebuano line falls. Your extension: build a Cebuano "importance matrix" calibration file and compare it to the default English one. Finally, read about 200–300 wrong answers yourself and sort them. Example types: answered in Tagalog instead of Cebuano, fell back to English, broke verb affixes like *nag-/mag-/gi-*, mangled a name, or made up a cultural fact.

Week-1 steps:

```bash
# Get the full-precision model and convert to GGUF (do this on Kaggle if RAM is tight)
huggingface-cli download Qwen/Qwen3-4B --local-dir qwen3-4b
python convert_hf_to_gguf.py qwen3-4b --outfile qwen3-4b-f16.gguf

# Make the shrink levels yourself (so every model is quantized the same way)
llama-quantize qwen3-4b-f16.gguf qwen3-4b-Q8_0.gguf   Q8_0
llama-quantize qwen3-4b-f16.gguf qwen3-4b-Q4_K_M.gguf Q4_K_M
llama-quantize qwen3-4b-f16.gguf qwen3-4b-Q2_K.gguf   Q2_K

# Extension: Cebuano calibration (feed ~100KB of real Cebuano news text)
llama-imatrix -m qwen3-4b-f16.gguf -f cebuano_calib.txt -o ceb.imatrix
llama-quantize --imatrix ceb.imatrix qwen3-4b-f16.gguf qwen3-4b-Q3_K_M-ceb.gguf Q3_K_M
```

*(The llama.cpp tool names and flags above are from general knowledge; check the current README, since they get renamed occasionally.)* Many Hugging Face uploaders also offer ready-made GGUFs at every level, which saves time. In Python, load Belebele's `ceb_Latn`, `tgl_Latn` and `eng_Latn` splits (dataset ID `facebook/belebele`, *unverified*). Send each passage, question and four choices to `llama-server`, ask for one letter, and score accuracy. By Friday you should have one model at three shrink levels on 100 questions per language.

How long will a full run take? Belebele has about 900 questions per language. Four models × five levels × three languages × 900 is about 54,000 prompts. At roughly one second each on the graphics chip, that is **about 15 hours of laptop time, or two or three overnight runs** *(estimate)*.

**(c) References, beginner first.**

| # | Read | Why |
|---|---|---|
| 1 | [FilBench announcement blog](https://ljvmiranda921.github.io/projects/2025/08/21/filbench) | Friendly intro to the benchmark you will reuse |
| 2 | [Lj Miranda, "On what it takes" (May 2026)](https://ljvmiranda921.github.io/notebook/2026/05/23/on-what-it-takes/) | Where Filipino NLP is heading; names edge/small models as a goal |
| 3 | [Filipino NLP catalog](https://ljvmiranda921.github.io/filipino-nlp) | Map of datasets and people |
| 4 | [Local LLM performance on a Framework 13](https://msf.github.io/blogpost/local-llm-performance-framework13.html) | Hands-on llama.cpp benchmarking on a near-twin of your laptop |
| 5 | [FilBench paper](https://arxiv.org/html/2508.03523v1) | Your baseline numbers and task list |
| 6 | [How Does Quantization Affect Multilingual LLMs?](https://arxiv.org/html/2407.03211v2) | The core prior finding you extend |
| 7 | [The Uneven Impact of Post-Training Quantization in MT](https://arxiv.org/abs/2508.20893) | GGUF and calibration-language results to test on Cebuano |

**(d) Blockers and risks.** The biggest risk is a panel saying "you just applied someone else's method to a new language." The Cebuano-calibration experiment and the native-speaker error taxonomy are your answer, because nobody else can do them as cheaply. Second, Cebuano test sets are small (99 items for SIB-200), so error bars will be wide. Report them honestly and lean on the larger Belebele and Tatoeba sets. Third, automatic scores understate quantization damage ([arXiv 2407.03211](https://arxiv.org/html/2407.03211v2)), which is why your human check of about 100 translations matters. Fourth, the FilBench paper has internal inconsistencies: GPT-4o is listed as both 72.23% and 75.56%, and the text says 12 sub-tasks while the table shows 13 ([FilBench](https://arxiv.org/html/2508.03523v1)). Cite the abstract's number and the final EMNLP version.

**(e) Difficulty 2/5. Laptop fit: excellent.** What makes it hard is bookkeeping, not ML: running dozens of model files consistently and parsing answers reliably. Everything up to 4B runs locally; you only need Kaggle to convert models if memory gets tight.

---

### Idea 2 — The first Cebuano/Filipino retrieval and RAG benchmark (Rank 2, difficulty 3/5)

**(a) What it is and why it matters.** Every Philippine RAG chatbot (for government, health or school documents) depends on one step: the search tool finding the right passage. Nobody has published numbers on how well search works for Cebuano. SEA-BED covers 10 Southeast Asian languages with 169 datasets, but **not Cebuano, Hiligaynon or Waray**, and its retrieval and QA rows have no Filipino entries ([SEA-BED](https://arxiv.org/html/2508.12243v2); [ACL 2026](https://aclanthology.org/2026.acl-long.397/)). FilBench has no retrieval category ([FilBench](https://arxiv.org/abs/2508.03523v1)). So your thesis would **set the first baseline numbers**: does keyword search (BM25) or meaning search (embeddings) work better for Cebuano questions, and how much worse is either than English?

On SEA-BED's overall Filipino average (all task types, not retrieval only), the top embedders were bge-multilingual-gemma2 (79.61), multilingual-e5-large-instruct (79.19) and bge-m3 (75.78) ([SEA-BED](https://arxiv.org/html/2508.12243v2)). That gives you a shortlist of models to test.

Two leads need checking. UP Cebu lists a "CebQA: Cebuano Question Answering System" project; its status and data are unknown ([UP Cebu CVSC](https://cvsc.upcebu.edu.ph/index.php/project/cebqa-cebuano-question-answering-system/)). There are also community Cebuano fine-tunes of Qwen3-Embedding on Hugging Face that nobody has evaluated publicly ([HF](https://huggingface.co/alphaedge-ai/Qwen3-Embedding-ceb-32768)). Those could even become a tested model in your study.

**(b) Example experiment.** Start with the quick win. Belebele gives you Cebuano passages, each with questions about it. Treat every passage as a "document" and every question as a "search query"; the correct document is the passage it came from. No annotation needed. Compare BM25, multilingual-e5-base, BGE-M3, Qwen3-Embedding-0.6B and the Cebuano fine-tune, using Recall@1/5 and nDCG@10. Run the same thing in Tagalog and English to measure the "Cebuano gap." Belebele alone is small (a few hundred passages), so retrieval will be too easy. Make it harder by adding thousands of distractor passages from human-written Cebuano text. Then go end to end: give a 1–4B model the gold passage, the retrieved passage, or no passage (the closed-book baseline), and score its multiple-choice answer. Stretch goal: write and personally check 300–500 fresh Cebuano question–passage pairs from news or government advisories. That is your genuinely new dataset.

Week-1 steps (all on the laptop):

```python
# pip install datasets bm25s sentence-transformers ranx
from datasets import load_dataset
ceb = load_dataset("facebook/belebele", "ceb_Latn")   # dataset ID unverified; check HF
# 1) dedupe passages -> corpus {doc_id: text}; questions -> queries {q_id: text}; qrels {q_id: {doc_id: 1}}
# 2) BM25:  bm25s.tokenize(...), retriever.index(...), retriever.retrieve(...)
# 3) Dense: SentenceTransformer("intfloat/multilingual-e5-base").encode(..., normalize_embeddings=True)
#           (e5 needs "query: " / "passage: " prefixes)
# 4) Score: ranx.evaluate(Qrels(qrels), Run(run), ["recall@1", "recall@5", "ndcg@10"])
```

By Friday you should have a three-row table (BM25, e5-base, then BGE-M3 on Kaggle) for Cebuano, Tagalog and English.

**(c) References, beginner first.**

| # | Read | Why |
|---|---|---|
| 1 | [Pinecone: Rerankers](https://www.pinecone.io/learn/series/rag/rerankers/) | Gentle intro to how retrieval pipelines are built |
| 2 | [Hybrid search explained (BigData Boutique)](https://bigdataboutique.com/blog/hybrid-search-explained) | BM25 vs dense in plain words |
| 3 | [GMA News on Cebuano Wikipedia](https://gmanetwork.com/news/scitech/technology/727785/cebuano-wikipedia-the-world-s-second-largest-wiki-edition-is-almost-entirely-written-by-a-bot-report/story) | Why you must not use Cebuano Wikipedia raw |
| 4 | [SBERT efficiency docs](https://sbert.net/docs/sentence_transformer/usage/efficiency.html) | Running embedders fast on CPU |
| 5 | [How Good is Your Wikipedia?](https://arxiv.org/pdf/2411.05527) | Measured bot-content problem and filtering |
| 6 | [SEA-BED](https://arxiv.org/html/2508.12243v2) | The closest prior work and its gap |
| 7 | [MMTEB (ICLR 2025)](https://arxiv.org/pdf/2502.13595v4) | The big multilingual embedding benchmark; check its Tagalog/Cebuano coverage |

**(d) Blockers and risks.** **Cebuano Wikipedia is about 99% bot-written**; deduplication removes 80% of its roughly 6.1M articles ([arXiv 2411.05527](https://arxiv.org/pdf/2411.05527)). Use human-written news or government text for distractors. Check each source's license; news-site licenses were not verified. Belebele passages are translations of English source texts *(general knowledge, unverified)*, so they are cleaner than real Cebuano. Say so as a limitation, and use your own fresh questions to address it. Questions you write yourself can be biased toward words that appear in the passage, which unfairly helps BM25. Write some as paraphrases. Finally, we did not confirm MMTEB has no Tagalog or Cebuano retrieval tasks; search the MTEB task list for `tgl`, `fil` and `ceb` before claiming "first."

**(e) Difficulty 3/5. Laptop fit: very good.** BM25 and base embedders run locally in minutes. BGE-M3-class models are better done once on Kaggle (a few hours on CPU *(estimate)*). The hard part is dataset craft: a clean corpus, honest question writing, and licenses. That suits a careful software engineer.

---

### Idea 3 — Can a small local model reliably grade RAG answers? (Rank 3, difficulty 3/5)

**(a) What it is and why it matters.** Many RAG projects use an AI judge to grade whether answers are "faithful," meaning supported by the retrieved passage. Using a free local 4–8B judge would be cheap and private, but small judges have well-documented problems. On JudgeBench (350 answer pairs, judged in both orders), Prometheus 2-7B scored 34.86% and JudgeLM-33B scored 35.71%, below the 50% coin-flip baseline under its strict swap rule ([JudgeBench](https://arxiv.org/pdf/2410.12784)). JudgeBoard found small Qwen3 and Gemma 3 judges trail larger models by about 10–13 points and agree with wrong student answers far too readily ([JudgeBoard](https://arxiv.org/html/2511.15958v1)). A June 2026 Berkeley audit of 21 judges found **raw agreement overstates kappa by about 39 points**: "85% agreement" is roughly κ 0.48. Qwen3-8B was the most consistent judge (0.992 test-retest) but also the most position-biased (0.192) ([Reliability without Validity](https://arxiv.org/pdf/2606.19544)). General judge reliability is crowded. The **narrower open gap is small, quantized judges on RAG faithfulness specifically**, measured with kappa and swap tests.

**(b) Example experiment.** Get 300–500 (question, passage, answer) triples with human "faithful/unfaithful" labels. RAGTruth is one possible public source (*existence and size unverified*). Otherwise, label 200 yourself. Judges: Qwen3-4B and 8B (thinking on/off), Gemma 3 4B, Llama 3.2 3B, Prometheus 2-7B, each at Q4 and Q8, plus one cheap API reference judge (under $10). Measure kappa against human labels, position flip rate, correlation with answer length, and agreement across three repeated runs. Follow the Berkeley "minimum viable validation" checklist: chance-corrected agreement, position swaps, replicate runs, at least two benchmarks ([arXiv 2606.19544](https://arxiv.org/pdf/2606.19544)).

Week 1: clone `github.com/ScalerLab/JudgeBench`. Run Qwen3-4B through `llama-server` on its 350 pairs in both orders, and reproduce the paper's scoring rule. Compute kappa (`sklearn.metrics.cohen_kappa_score`) and the flip rate. Separately, wire up a RAGAS faithfulness metric (`pip install ragas`) pointed at your local model *(RAGAS's current local-model setup unverified)*.

**(c) References, beginner first.**

| # | Read | Why |
|---|---|---|
| 1 | [Adding Error Bars to Evals](https://arxiv.org/html/2411.00640v1) | Clear, short statistics recipe you'll use everywhere |
| 2 | [JudgeBench](https://arxiv.org/pdf/2410.12784) | The standard hard test for judges |
| 3 | [JudgeBoard](https://arxiv.org/html/2511.15958v1) | Small-model judges specifically |
| 4 | [Reliability without Validity](https://arxiv.org/pdf/2606.19544) | The protocol to follow |
| 5 | [When the Judge Changes, So Does the Measurement](https://arxiv.org/pdf/2607.08535) | Related 2026 work (not read by us) |

**(d) Blockers and risks.** The field moves monthly, so a similar paper could appear mid-thesis. Small models often break the required output format (for example, invalid JSON). Use retries or constrained output, and report "parse failure" separately from "wrong verdict." "Thinking" mode is slow on a laptop. You also need trustworthy human labels, which may mean labeling 200 yourself.

**(e) Difficulty 3/5. Laptop fit: good.** Non-thinking 4–8B judges run locally overnight; thinking-mode runs belong on Kaggle. Statistics (kappa, swaps) are the conceptual hurdle, but they are simple once learned.

---

### Idea 4 — Do small 2025–2026 models still get fooled by noisy search results? (Rank 4, difficulty 2/5)

**(a) What it is and why it matters.** RAG search sometimes returns junk passages, or no relevant passage at all. RGB (AAAI 2024) tests four abilities: ignoring noise, saying "I don't know" when no passage answers the question ("negative rejection"), combining facts from several passages, and resisting false passages. It found models "still struggle significantly" with the last three ([RGB](https://emergentmind.com/papers/2309.01431)). No paper has cleanly re-run RGB on today's small open models. A 2026 follow-up used only GPT-3.5 and GPT-4o-mini. It found negative-rejection rates below 50% everywhere, and GPT-3.5's fact-combining fell from 55% to 34% as noise rose to 40% ([arXiv 2603.05698](https://arxiv.org/pdf/2603.05698)). A related twist: NoisyBench (ICLR 2026) found small models are hit hardest (one 8B reasoning model dropped 80.6%), and that **longer "thinking" made accuracy worse under distractors** ([NoisyBench](https://arxiv.org/html/2601.07226v1)).

**(b) Example experiment.** Run RGB's English set at noise ratios 0, 0.2, 0.4, 0.6 and 0.8, plus negative rejection and counterfactual subsets. Test 4–6 local models (Qwen3 1.7B/4B/8B, Gemma 3 4B, Llama 3.2 3B). Add two factors nobody has crossed: thinking on vs off (Qwen3), and Q4 vs Q8. Always run a closed-book baseline, and build about 100–200 fresh questions from 2026 news using RGB's recipe to check for contamination. Week 1: `git clone https://github.com/chen700564/RGB`, run Qwen3-1.7B through `llama-server` at noise 0 and 0.4, reproduce the repo's exact-match scoring, and time it.

**(c) References, beginner first.** Start with the [Emergent Mind RGB summary](https://emergentmind.com/papers/2309.01431). Then read the [RGB repo](https://github.com/chen700564/RGB), the [2026 RGB GraphRAG follow-up](https://arxiv.org/pdf/2603.05698), [NoisyBench](https://arxiv.org/html/2601.07226v1), and finally the [Pandora's Box / NoiserBench paper](https://arxiv.org/html/2408.13533v1), which argues some noise can even help.

**(d) Blockers and risks.** RGB's 2023 news questions may now be inside 2025 models' training data. That inflates scores and especially breaks the "say I don't know" test, because the model already knows. The fresh-question set fixes this. RGB's exact size (about 600 base questions per language) and whether its rejection scoring needs an OpenAI key are *unverified*; check the repo. Novelty is modest; the thinking × quantization factors are what lift it.

**(e) Difficulty 2/5. Laptop fit: very good** for models up to 8B at Q4. Use Kaggle for the full grid if overnight runs get long.

---

### Idea 5 — Which kinds of questions does keyword search still win? (Rank 5, difficulty 2/5)

**(a) What it is and why it matters.** Practitioners say BM25 still beats meaning search on questions with names, numbers or IDs ([tianpan.co](https://tianpan.co/blog/2026-04-12-hybrid-search-production-bm25-dense-embeddings), an opinion piece). A 2025 VLDB study benchmarked hybrid search across 11 datasets. It found a "weakest link" effect, where one bad search path drags down the merged result, and found no single best setup. But it showed no breakdown by question type ([Balancing the Blend](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf)). The classic study of how to merge ranked lists is older ([Bruch et al.](https://arxiv.org/pdf/2210.11934)). A careful "which method wins for which question type" study with small open models appears unpublished.

**(b) Example experiment.** Use 4–5 small BEIR datasets: SciFact, NFCorpus, FiQA, ArguAna, SciDocs. Compare BM25 (`bm25s`), small dense embedders (bge-small, e5-small), hybrid (RRF via `ranx`), and each with or without a reranker on the top 100 (`BAAI/bge-reranker-base`). Tag each question automatically by length, share of rare words, presence of numbers or names, and word overlap with the answer. Hand-check a sample of the tags. Report nDCG@10 per type with bootstrap CIs. Week 1: install the tools, run BM25 and dense on SciFact, and confirm your BM25 nDCG@10 is within about 1 point of the published BEIR number.

**(c) References, beginner first.** [BigData Boutique hybrid explained](https://bigdataboutique.com/blog/hybrid-search-explained), [Denser.ai hybrid guide](https://denser.ai/blog/hybrid-search-for-rag/), [Pinecone rerankers](https://www.pinecone.io/learn/series/rag/rerankers/), [BGE reranking tutorial](https://bge-model.com/tutorial/5_Reranking/5.1.html), [open hybrid/reranking notes](https://pendu.github.io/Advanced-Retreival-and-Re-ranking/stage1_retrieval/hybrid.html), [BEIR repo](https://github.com/beir-cellar/beir), then [Bruch et al.](https://arxiv.org/pdf/2210.11934) and [Balancing the Blend](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf).

**(d) Blockers and risks.** The IR community has discussed this informally for years, so do a Semantic Scholar search for "query type" + "hybrid retrieval" before committing. BEIR's answer labels are incomplete, so some "wrong" results are actually right. Embedders may have trained on BEIR-like data (check model cards). Rerankers are slow on CPU, so cap at top 50–100.

**(e) Difficulty 2/5. Laptop fit: excellent.** It needs no LLM at all. This is the easiest idea, but also the one with the weakest novelty. It becomes much stronger if you **run it on your Cebuano benchmark from Idea 2**, where "does BM25 win for Cebuano names and places?" is a genuinely new question.

---

### Idea 6 — Does training on Tagalog or Hiligaynon help tag names in Cebuano? (Rank 6, difficulty 3/5)

**(a) What it is and why it matters.** Each Philippine language has only a small NER dataset. Can a model trained on one language tag names in another? All three datasets share PER/ORG/LOC labels. TLUnified-NER is Tagalog, about 7k documents, GPL-3.0 license ([HF card](https://huggingface.co/datasets/ljvmiranda921/tlunified-ner/blob/main/README.md?code=true)). HiligayNER has about 8,082 sentences ([HiligayNER](https://arxiv.org/html/2510.10776v1)). The third is CebuaNER ([CebuaNER](https://cs.paperswithcode.com/paper/cebuaner-a-new-baseline-cebuano-named-entity)). **This idea is now partly done.** HiligayNER found that zero-shot transfer from Hiligaynon to Cebuano reaches only about 0.46 macro F1 (and 0.44 to Tagalog), versus 0.86 in-language ([HiligayNER](https://arxiv.org/html/2510.10776v1)). A Cambridge paper tested transfer from English, Slovak and Croatian into Tagalog and Cebuano, gaining only 2–6 F1 points ([arXiv 2509.02160](https://arxiv.org/pdf/2509.02160v2)). What remains open is the **full 3×3 matrix between Philippine languages, with few-shot learning curves**.

**(b) Example experiment.** Fine-tune XLM-R base and mBERT on each source language. Test on each target with 0, 10, 50, 100 and 500 target sentences added. Add multi-source training (Tagalog + Hiligaynon → Cebuano). Include GLiNER (calamanCy's Tagalog GLiNER scores about 85 F1 on TLUnified-NER ([calamanCy](https://ljvmiranda921.github.io/calamanCy/news/gliner))) and a prompted LLM baseline. Week 1, on Kaggle: run the Hugging Face token-classification example script with `xlm-roberta-base` on TLUnified-NER, evaluate zero-shot on CebuaNER with `seqeval` (entity-level F1), and log the time.

**(c) References, beginner first.** [calamanCy GLiNER post](https://ljvmiranda921.github.io/calamanCy/news/gliner), [TLUnified-NER card](https://huggingface.co/datasets/ljvmiranda921/tlunified-ner/blob/main/README.md?code=true), [calamanCy paper](https://arxiv.org/pdf/2311.07171), [HiligayNER](https://arxiv.org/html/2510.10776v1), [Meta-Pretraining for PH NER](https://arxiv.org/pdf/2509.02160v2).

**(d) Blockers and risks.** Datasets made under different labeling guidelines cause fake "transfer failures." For example, calamanCy's GLiNER dropped to about 50% on Universal NER for exactly this reason ([calamanCy](https://ljvmiranda921.github.io/calamanCy/news/gliner)). Licenses also need care: TLUnified-NER is GPL-3.0, HiligayNER's license is unnamed, and CebuaNER's is unverified. This is the only idea that requires model *training*, which is the part you know least.

**(e) Difficulty 3/5. Laptop fit: fair.** CPU training works but is slow; use Kaggle. A strong add-on, since you're in Leyte: annotating about 300 Waray sentences would be a genuinely new resource. But that is data collection, which you wanted to minimize.

---

### Idea 7 — Chunking, end to end (Rank 7, difficulty 2/5; demoted from #1)

**(a) What it is and why it matters.** How you cut documents into chunks affects what search finds. The earlier report's top pick extended a 2025 paper that tested only fixed-size chunks with no answer generation ([arXiv 2505.21700](https://arxiv.org/html/2505.21700v2)). **That gap has mostly closed.** Vectara found answer quality nearly identical across chunkers, and that the embedding model mattered more ([arXiv 2410.13070](https://arxiv.org/html/2410.13070v1)). A January 2026 paper with proper confidence intervals found sentence and semantic chunking statistically tied, found 10–20% overlap gave no gain, and found a "context cliff" where quality drops after about 2.5k tokens of context ([arXiv 2601.14123](https://arxiv.org/html/2601.14123v1)). A May 2026 paper compared 8 chunkers and found fixed-size nearly as good as the best (87.71 vs 89.36 Acc@5) while taking under a second instead of 8–15 hours ([arXiv 2606.00881](https://arxiv.org/pdf/2606.00881)). The field's answer is converging on "simple chunking is fine."

**(b) Example experiment (the narrow gap that remains).** Use chunks normalized to equal size, which the 2026 paper admits it lacked. Add a reranker on/off factor (which the January paper excluded), late chunking ([Jina](https://arxiv.org/html/2409.04701v1)), and 2–3 small generators instead of one, on the 2505.21700 datasets (TechQA, COVID-QA, NarrativeQA). Fix the number of context *tokens* rather than chunks, to avoid the context cliff. Week 1: `git clone https://github.com/fraunhofer-iais/chunking-strategies` and reproduce SQuAD* Recall@1 at 64/128/256 tokens.

**(c) References, beginner first.** [Vectara blog](https://vectara.com/blog/is-semantic-chunking-worth-the-computational-cost), [Chroma chunking report](https://trychroma.com/research/evaluating-chunking), [NVIDIA chunking blog](https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/), [Jina late-chunking blog](https://jina.ai/news/late-chunking-in-long-context-embedding-models/), then the papers: [2505.21700](https://arxiv.org/html/2505.21700v2), [2601.14123](https://arxiv.org/html/2601.14123v1), [2606.00881](https://arxiv.org/pdf/2606.00881).

**(d) Blockers and risks.** The main risk is being called incremental. Technical traps include "stitched" synthetic documents that unfairly favor semantic chunkers ([Vectara](https://arxiv.org/html/2410.13070v1)), unequal chunk counts across methods, and slow LLM-based chunkers. Even the baseline paper has an internal inconsistency about which size peaks on NQ ([arXiv 2505.21700](https://arxiv.org/html/2505.21700v2)).

**(e) Difficulty 2/5. Laptop fit: excellent.** Easy to run, hard to make novel. Pick it only if your adviser explicitly prefers English-only RAG work.

---

## Rules that apply to every idea

Three habits separate a thesis from a demo. First, **run a closed-book baseline** for any RAG test, so you know which questions the model answers from memory. Second, **report a ± margin on every score.** When comparing two systems on the same questions, use paired differences. When many questions share one document, use "clustered" errors, which can be about 3× larger ([Miller 2024](https://arxiv.org/html/2411.00640v1)). Proper intervals often erase apparent wins: the January 2026 chunking paper found many chunkers statistically tied once it added them ([arXiv 2601.14123](https://arxiv.org/html/2601.14123v1)). Third, if you use an AI judge, **report kappa, not raw agreement, and swap answer order** ([arXiv 2606.19544](https://arxiv.org/pdf/2606.19544)). Keep the earlier report's rule: one benchmark slice, one main comparison, a 3×3-sized grid. Reproduce one published number in month 1 so you have a guaranteed result banked.

---

## Top recommendation: one Cebuano pipeline, two clean questions

**Combine Ideas 1 and 2 into one thesis**, with Idea 5's query-type analysis as an optional chapter. A working title: *"Search and Shrink: Measuring Retrieval and Quantization Losses in a Small Cebuano Question-Answering Pipeline on Consumer Hardware."*

The research questions are falsifiable and separate. **RQ1 (retrieval):** On Cebuano questions, how do BM25 and multilingual embedders compare in Recall@k, and how large is the gap versus Tagalog and English? **RQ2 (reading):** When a small model answers from a gold passage, a retrieved passage, or no passage, how much accuracy does each quantization level cost in Cebuano versus English, and does Cebuano calibration recover it? **RQ3 (errors):** What kinds of mistakes dominate? You sort them using native-speaker judgment.

This combination wins for four reasons. **Every score has an objective right answer**: Belebele is multiple choice and retrieval has a known gold passage, so you need no AI judge, no judge-bias chapter, and essentially no API budget. It runs on your laptop end to end, with Kaggle only for BGE-M3 embedding and model conversion. It produces two "firsts" (Cebuano retrieval baselines and Philippine-language quantization numbers) without heavy annotation. And it fails safely: if RQ1 turns out unremarkable, RQ2 still stands, and vice versa.

| Month | Milestone |
|---|---|
| 1 | Benchmark laptop (`llama-bench` table). Reproduce one FilBench Belebele number for one model. Lock RQs and licenses. Email the FilBench network ([filbench.github.io](https://filbench.github.io/)) to check nobody is already doing this. |
| 2 | RQ1: BM25 vs 3–4 embedders on Belebele ceb/tgl/eng, then with distractors |
| 3 | RQ2: 4 models × 5 quant levels × 3 languages × {gold, retrieved, none}, as overnight runs |
| 4 | Cebuano-calibration extension; optional 300 fresh Cebuano Q–passage pairs; error bars |
| 5 | Error taxonomy on 200–300 failures; write methods and results |
| 6 | Writing, figures, defense |

Before committing, spend one afternoon on two checks. Search the MTEB task list for `tgl`, `fil` and `ceb` retrieval tasks, and open the CebQA page at UP Cebu. If either already provides Cebuano retrieval baselines, shift the weight to RQ2 and RQ3; the thesis still holds.

## Conclusion

The new laptop changes less about *what* is worth studying than about *where* you can run it. The late-2026 literature has done the real re-ranking. English-only RAG knobs like chunking now have the "simple methods are fine" answer, backed by confidence intervals. Meanwhile, the Philippine side still lacks basic measurements: retrieval baselines, quantization effects, a Cebuano error profile. That makes your native Cebuano a sharper research asset than it was a year ago, because what remains open is exactly what a well-equipped English-speaking lab cannot cheaply check.

Measuring small, quantized models on a mid-range laptop also produces a nice irony: your hardware limit becomes part of the contribution. Results that say "here is what a Filipino developer on a 16GB laptop can actually expect in Cebuano" are directly useful to the people building offline government, health and school tools in the Visayas. Frame the thesis that way and the machine you own stops being a constraint and becomes the experimental setting.
