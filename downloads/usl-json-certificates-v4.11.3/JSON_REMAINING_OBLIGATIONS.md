# JSON: completed review and remaining qualification work

The complete published RFC8259 text was read and checked against the existing
candidate inventory. Its 28,360 bytes match SHA-256
`61a5378f4255c720beb2a4b4a63b29540147c140f36988bf086291989b4cd2d7`.
`JSON_NORMATIVE_REVIEW.json` gives separate reasoning and source citations for
each of the 30 local grammar productions, 10 operative uppercase statements and
22 candidate prose rows. It also reviews the rest of the document, records seven
findings and makes eight additional dependency/integration obligations explicit.
These are review records, not 62 proved implementation properties.

The selected target is **the December2017 published RFC text**. It accepts raw
solidus according to that text. The archived official errata snapshot marks5318
Verified Editorial but changes the solidus range; this package does not silently
apply that change or claim conformance to a current-errata target. No official
certification or external standards-body approval is claimed.

## Follow-through work

| Priority | Required work | Completion evidence |
| --- | --- | --- |
| 1 | Close relevant normative-reference dependencies: RFC5234 core DIGIT/HEXDIG and used ABNF operators, RFC3629 UTF-8, RFC2119/RFC8174 force, Unicode interpretation and the special ECMA-404 alignment reference. Record IEEE754 applicability. | Exact authoritative source/version/hash, cited applicable clauses, interpretation rationale and independent review. Existing retrieval metadata alone does not pass this gate. |
| 2 | Finalize the actual resource profile and justify node-count/number-lexeme limits as size/resource metrics. Correct the old depth label. | Reviewed contract, at/below/above-bound tests and consistent resource-refusal classifications. Root-zero value recursion depth40 is the current predicate:41empty nested containers can pass, while a scalar under41containers cannot. |
| 3 | Complete rule-to-code-to-test traceability over each applicable source/dependency obligation and each chosen policy. | Exact source locations, independent test/oracle identities, fresh receipts and a report of every unmapped or unresolved rule. Candidate implementation claims are not self-validating evidence. |
| 4 | Establish parser correctness for the claimed domain. | A checked correspondence/progress argument or mechanized proof of grammar acceptance, complete input consumption, representation and resource behavior; independent malformed-input, encoding and boundary evidence remains necessary. Tests alone retain their finite scope. |
| 5 | Establish generator correctness over validated canonical IR. | Checked validity/preservation/termination arguments, including recursive structure, numeric lexemes, mandatory escapes, lone surrogates, duplicate policy and no-BOM output. Rejected malformed caller IR is separate from malformed output. |
| 6 | Check the concrete JSON-to-USL data translation and the runtime assumptions. | Independently validated AST restricted to one data assignment, exact-type structural preservation, artifact bindings and fresh execution under the pinned runtime. A concrete-literal certificate does not prove the parser, generator or USL interpreter correct. |
| 7 | Re-run and independently review native interoperability on the exact claimed platform/runtime builds. | Fresh native and generated observations with binary/library/source/environment identities; keep number, duplicate and surrogate policy differences explicit. A matching host parser does not replace the RFC oracle. |
| 8 | Review deployment and release behavior separately from RFC syntax. | Capability/resource checks, exact Python/USL interface contracts, clean extraction/build/regression receipts, source/dependency hashes and applicable distribution notices. |
| 9 | Implement media/protocol handling only for an explicitly claimed transport integration. | Separate tests for application/json, the selected parameter/charset policy, transport encoding and actual server behavior. The pure bytes API supplies no HTTP or MIME stack. |
| 10 | Make the final scoped qualification decision after independent review of every applicable requirement. | Reviewed exact-build claim with all mandatory gaps closed; retain separate language-format conformance, translation, intent-proof and project release decisions. |

## Interpretation corrections that matter

- A SHOULD about unique names does not make duplicate-member text grammar-invalid.
  Default duplicate rejection during generation is a local policy; preservation
  mode requires a deliberate documented interoperability exception.
- The RFC permits implementation limits; it does not turn every unsupported
  feature into a resource limit. Conforming over-limit text remains conforming
  JSON, with a distinct resource refusal in this implementation.
- No normalization, avoiding eval and allocation checks are useful project
  policies. They are not additional uppercase RFC MUST statements hidden in
  sections8.3,10or12. The normative audit must preserve the actual force and scope.
- The format has no defined programming-language execution model, executable
  standard library, thread semantics or language ABI. Python/USL host APIs still
  need their own project integration checks; this category distinction does not
  automatically complete the original project obligations.
- Source roundtripping preserves the chosen typed IR, not original whitespace,
  escape spelling, BOM or bytes. Object pair order/duplicates and number spellings
  are deliberately retained as representation information, without claiming that
  arbitrary foreign receivers preserve them.

Full-format qualification remains **open**. The review improves the exact
inventory and target contract; it does not promote the JSON profile or any other
catalog entry automatically.
