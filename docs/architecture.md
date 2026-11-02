# Architecture

Vendor adapters translate platform data into a shared domain model.
Services orchestrate exchanges independently of vendor SDKs.
The initial service only previews objects from an injected source.

Before enabling writes, define object ownership, stable identifiers,
mapping validation, revision rules, idempotency, conflict handling,
retry behavior, audit requirements, and recovery procedures.

No exchange direction or vendor endpoint is assumed by this scaffold.
