function LLM(prompt):
    # 1. Tokenization
    tokens = tokenize(prompt)  # e.g., ["The", "cat", "sat"] → [1012, 403, 712]

    # 2. Convert tokens to embeddings
    embeddings = lookup_embedding(tokens)

    # 3. Add positional encodings
    inputs = embeddings + positional_encoding(len(tokens))

    # 4. Pass through N Transformer layers
    for layer in 1..N:
        # 4a. Self-Attention
        Q = inputs * Wq   # Queries
        K = inputs * Wk   # Keys
        V = inputs * Wv   # Values

        attention_scores = softmax((Q * Kᵀ) / sqrt(d_k))
        context = attention_scores * V

        # 4b. Residual + Normalization
        inputs = LayerNorm(inputs + context)

        # 4c. Feed-Forward Network (FFN)
        ff_output = Activation(inputs * W1 + b1) * W2 + b2

        # 4d. Residual + Normalization
        inputs = LayerNorm(inputs + ff_output)

    # 5. Project final hidden state to vocabulary space
    logits = inputs * W_vocab

    # 6. Convert logits to probabilities
    probs = softmax(logits)

    # 7. Pick next token (sampling / greedy / top-k)
    next_token = sample(probs)

    return next_token
