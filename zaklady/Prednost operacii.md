</span><h2>Operator precedence</h2>
<p id="index-92">The following table summarizes the operator precedence in Python, from lowest
precedence (least binding) to highest precedence (most binding).  Operators in
the same box have the same precedence.  Unless the syntax is explicitly given,
operators are binary.  Operators in the same box group left to right (except for
exponentiation, which groups from right to left).</p>
<p>Note that comparisons, membership tests, and identity tests, all have the same
precedence and have a left-to-right chaining feature as described in the
Comparisons section.
<table class="docutils align-default">
<colgroup>
<col style="width: 56%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Operator</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="#lambda"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">lambda</span></code></a></p></td>
<td><p>Lambda expression</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="compound_stmts.html#if"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">if</span></code></a> – <a class="reference internal" href="compound_stmts.html#else"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">else</span></code></a></p></td>
<td><p>Conditional expression</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#or"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">or</span></code></a></p></td>
<td><p>Boolean OR</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#and"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">and</span></code></a></p></td>
<td><p>Boolean AND</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#not"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">not</span></code></a> <code class="docutils literal notranslate"><span class="pre">x</span></code></p></td>
<td><p>Boolean NOT</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#in"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">in</span></code></a>, <a class="reference internal" href="#not-in"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">not</span> <span class="pre">in</span></code></a>,
<a class="reference internal" href="#is"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">is</span></code></a>, <a class="reference internal" href="#is-not"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">is</span> <span class="pre">not</span></code></a>, <code class="docutils literal notranslate"><span class="pre">&lt;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&lt;=</span></code>, <code class="docutils literal notranslate"><span class="pre">&gt;</span></code>, <code class="docutils literal notranslate"><span class="pre">&gt;=</span></code>, <code class="docutils literal notranslate"><span class="pre">!=</span></code>, <code class="docutils literal notranslate"><span class="pre">==</span></code></p></td>
<td><p>Comparisons, including membership
tests and identity tests</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">|</span></code></p></td>
<td><p>Bitwise OR</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">^</span></code></p></td>
<td><p>Bitwise XOR</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">&amp;</span></code></p></td>
<td><p>Bitwise AND</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">&lt;&lt;</span></code>, <code class="docutils literal notranslate"><span class="pre">&gt;&gt;</span></code></p></td>
<td><p>Shifts</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">+</span></code>, <code class="docutils literal notranslate"><span class="pre">-</span></code></p></td>
<td><p>Addition and subtraction</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">&#64;</span></code>, <code class="docutils literal notranslate"><span class="pre">/</span></code>, <code class="docutils literal notranslate"><span class="pre">//</span></code>, <code class="docutils literal notranslate"><span class="pre">%</span></code></p></td>
<td><p>Multiplication, matrix
multiplication, division, floor
division, remainder <a class="footnote-reference brackets" href="#id21" id="id15">5</a></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">+x</span></code>, <code class="docutils literal notranslate"><span class="pre">-x</span></code>, <code class="docutils literal notranslate"><span class="pre">~x</span></code></p></td>
<td><p>Positive, negative, bitwise NOT</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">**</span></code></p></td>
<td><p>Exponentiation <a class="footnote-reference brackets" href="#id22" id="id16">6</a></p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#await"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">await</span></code></a> <code class="docutils literal notranslate"><span class="pre">x</span></code></p></td>
<td><p>Await expression</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">x[index]</span></code>, <code class="docutils literal notranslate"><span class="pre">x[index:index]</span></code>,
<code class="docutils literal notranslate"><span class="pre">x(arguments...)</span></code>, <code class="docutils literal notranslate"><span class="pre">x.attribute</span></code></p></td>
<td><p>Subscription, slicing,
call, attribute reference</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">(expressions...)</span></code>,
<code class="docutils literal notranslate"><span class="pre">[expressions...]</span></code>,
<code class="docutils literal notranslate"><span class="pre">{key:</span> <span class="pre">value...}</span></code>,
<code class="docutils literal notranslate"><span class="pre">{expressions...}</span></code></p></td>
<td><p>Binding or tuple display,
list display,
dictionary display,
set display</p></td>
</tr>
</tbody>
